"""Offline evidence and non-scoring contracts for parent-to-child assessments."""

import copy
import contextlib
import csv
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from vendi_assessment import assessment_text, parse_assessment, preserve_assessment_status
from vendi_changes import build_change_packet
import compare_vendi as cv


# Minimal reproductions of the two source-level errors found in the S61 audit:
# an already defined sampler becomes used, and ranking leaves the update boundary.
SAMPLER_PARENT = """class IdentityCellBatchSampler:
    def __init__(self, dataset):
        self.dataset = dataset

train_loader = DataLoader(dataset, batch_size=32, shuffle=True)
for batch in train_loader:
    train_step(batch)
"""
SAMPLER_CHILD = """class IdentityCellBatchSampler:
    def __init__(self, dataset):
        self.dataset = dataset

train_batch_sampler = IdentityCellBatchSampler(dataset)
train_loader = DataLoader(dataset, batch_sampler=train_batch_sampler)
for batch in train_loader:
    train_step(batch)
"""
MICRO_PARENT = """def train_microbatch(logits, targets, accumulation, enabled, is_update_boundary):
    ranking_is_active = enabled and is_update_boundary
    ranking_loss = ranking(logits, targets) if ranking_is_active else logits.sum() * 0
    loss = classification(logits, targets) / accumulation + ranking_loss
    loss.backward()
"""
MICRO_CHILD = """def train_microbatch(logits, targets, accumulation, enabled, is_update_boundary):
    ranking_is_active = enabled
    ranking_loss = ranking(logits, targets) if ranking_is_active else logits.sum() * 0
    loss = (classification(logits, targets) + ranking_loss) / accumulation
    loss.backward()
"""


def evidence(packet, side, line):
    matches = [ref for ref, raw in packet["evidence_lines"].items()
               if ref.startswith(side + ":") and raw.strip() == line.strip()]
    if len(matches) != 1:
        raise AssertionError(f"Expected exactly one displayed source line: {side}: {line}")
    return {"ref": matches[0], "quote": line}


def sampler_case():
    packet = build_change_packet(SAMPLER_PARENT, SAMPLER_CHILD)
    parent = evidence(packet, "PARENT", "train_loader = DataLoader(dataset, batch_size=32, shuffle=True)")
    child = evidence(packet, "CHILD", "train_loader = DataLoader(dataset, batch_sampler=train_batch_sampler)")
    result = dict(status="changed", reason="The child connects the existing sampler to the training loader.",
                  changes=[dict(kind="activation", description="Activate identity-cell batch sampling in the training DataLoader.",
                                evidence=[parent, child], execution="connected", execution_evidence=[child["ref"]])])
    return packet, result


def parse(result, packet):
    return parse_assessment(json.dumps(result), packet)


class AssessmentEvidenceTests(unittest.TestCase):
    def test_preexisting_sampler_activation_is_supported_by_actual_loader_diff(self):
        packet, result = sampler_case()
        self.assertFalse(packet["ast_equal"])
        self.assertIn("batch_sampler=train_batch_sampler", packet["diff"])
        # The declaration is unchanged; the actual new connection must carry the evidence.
        self.assertNotIn("CHILD:1", packet["changed_refs"])
        use = result["changes"][0]["execution_evidence"][0]
        self.assertIn(use, packet["changed_refs"])
        self.assertIn(use, packet["usage_refs"])
        checked = parse(result, packet)
        self.assertEqual(checked["status"], "changed")
        self.assertEqual(assessment_text(checked), result["changes"][0]["description"])
        self.assertNotIn("source", assessment_text(checked))

    def test_microbatch_gradient_coverage_and_scaling_use_raw_changed_lines(self):
        packet = build_change_packet(MICRO_PARENT, MICRO_CHILD)
        old_gate = evidence(packet, "PARENT", "ranking_is_active = enabled and is_update_boundary")
        new_gate = evidence(packet, "CHILD", "ranking_is_active = enabled")
        old_loss = evidence(packet, "PARENT", "loss = classification(logits, targets) / accumulation + ranking_loss")
        new_loss = evidence(packet, "CHILD", "loss = (classification(logits, targets) + ranking_loss) / accumulation")
        backward = evidence(packet, "CHILD", "loss.backward()")
        for item in (old_gate, new_gate, old_loss, new_loss):
            self.assertIn(item["ref"], packet["changed_refs"])
        self.assertIn(backward["ref"], packet["usage_refs"])
        result = dict(status="changed", reason="The raw diff changes both the ranking gate and gradient scaling.",
                      changes=[dict(kind="bug_fix",
                                    description="Apply ranking on every enabled microbatch and scale its gradient by accumulation.",
                                    evidence=[old_gate, new_gate, old_loss, new_loss, backward],
                                    execution="connected", execution_evidence=[backward["ref"]])])
        checked = parse(result, packet)
        self.assertEqual(checked["status"], "changed")
        self.assertIn("microbatch", assessment_text(checked))
        self.assertNotIn("reason", assessment_text(checked))

    def test_fabricated_quote_and_unseen_reference_are_rejected(self):
        packet, original = sampler_case()
        for bad_item, message in (({"ref": "CHILD:6", "quote": "train_loader = fake_loader(dataset)"}, "does not match"),
                                  ({"ref": "CHILD:999", "quote": "train_loader = fake_loader(dataset)"}, "not displayed")):
            result = copy.deepcopy(original)
            result["changes"][0]["evidence"][1] = bad_item
            with self.subTest(bad_item=bad_item), self.assertRaisesRegex(ValueError, message):
                parse(result, packet)

    def test_unchanged_context_cannot_become_an_evidenced_change(self):
        packet, result = sampler_case()
        parent = evidence(packet, "PARENT", "train_step(batch)")
        child = evidence(packet, "CHILD", "train_step(batch)")
        result["changes"][0].update(evidence=[parent, child], execution_evidence=[child["ref"]])
        self.assertNotIn(parent["ref"], packet["changed_refs"])
        self.assertNotIn(child["ref"], packet["changed_refs"])
        with self.assertRaisesRegex(ValueError, "actual non-comment changed line"):
            parse(result, packet)

    def test_changed_comment_does_not_certify_a_mechanism(self):
        packet = build_change_packet("# old explanation\nx = model(data)\n", "# new mechanism\nx = model(data)\n")
        result = dict(status="changed", reason="This claim is unsupported.", changes=[dict(
            kind="new_mechanism", description="Invented mechanism.",
            evidence=[evidence(packet, "PARENT", "# old explanation"),
                      evidence(packet, "CHILD", "# new mechanism"),
                      evidence(packet, "CHILD", "x = model(data)")],
            execution="connected", execution_evidence=["CHILD:2"])])
        with self.assertRaisesRegex(ValueError, "actual non-comment changed line"):
            parse(result, packet)

    def test_one_sided_evidence_is_rejected(self):
        packet, result = sampler_case()
        result["changes"][0]["evidence"] = result["changes"][0]["evidence"][1:]
        with self.assertRaisesRegex(ValueError, "BOTH parent and child"):
            parse(result, packet)

    def test_function_declaration_cannot_impersonate_a_connection(self):
        packet = build_change_packet("def sampler():\n    return 1\n", "def new_sampler():\n    return 1\n")
        result = dict(status="changed", reason="Only a function is defined.", changes=[dict(
            kind="new_mechanism", description="Use a new sampler.",
            evidence=[evidence(packet, "PARENT", "def sampler():"),
                      evidence(packet, "CHILD", "def new_sampler():")],
            execution="connected", execution_evidence=["CHILD:1"])])
        with self.assertRaisesRegex(ValueError, "CHILD use/call"):
            parse(result, packet)

    def test_execution_reference_must_also_be_quoted_in_this_change(self):
        packet, result = sampler_case()
        extra = evidence(packet, "CHILD", "train_step(batch)")
        result["changes"][0]["execution_evidence"] = [extra["ref"]]
        with self.assertRaisesRegex(ValueError, "quoted evidence"):
            parse(result, packet)

    def test_parent_only_execution_reference_cannot_claim_child_connection(self):
        packet, result = sampler_case()
        result["changes"][0]["execution_evidence"] = [result["changes"][0]["evidence"][0]["ref"]]
        with self.assertRaisesRegex(ValueError, "CHILD use/call"):
            parse(result, packet)

    def test_unconnected_changes_are_non_scoring_but_keep_audit_evidence(self):
        for execution in ("definition_only", "uncertain"):
            packet, result = sampler_case()
            result["changes"][0].update(execution=execution, execution_evidence=[])
            with self.subTest(execution=execution):
                checked = parse(result, packet)
                self.assertEqual(checked["status"], "insufficient_evidence")
                self.assertEqual(checked["changes"], [])
                self.assertEqual(checked["unverified_changes"], result["changes"])
                self.assertEqual(assessment_text(checked), "")


class AssessmentDecisionTests(unittest.TestCase):
    def test_no_change_claim_on_both_real_bug_fixtures_is_downgraded(self):
        for parent, child in ((SAMPLER_PARENT, SAMPLER_CHILD), (MICRO_PARENT, MICRO_CHILD)):
            packet = build_change_packet(parent, child)
            result = dict(status="no_change", reason="No substantive changes were found.", changes=[])
            checked = parse(result, packet)
            self.assertEqual(checked["status"], "insufficient_evidence")
            self.assertIn(result["reason"], checked["reason"])
            self.assertEqual(assessment_text(checked), "")

    def test_identical_and_ast_equivalent_sources_keep_no_change_without_embedding_text(self):
        for parent, child in ((SAMPLER_PARENT, SAMPLER_PARENT),
                              ("x = model(data)\n", "# clarified comment\nx=model(data)\n")):
            packet = build_change_packet(parent, child)
            self.assertTrue(packet["ast_equal"])
            checked = parse(dict(status="no_change", reason="The computational AST is unchanged.", changes=[]), packet)
            self.assertEqual(checked["status"], "no_change")
            self.assertEqual(assessment_text(checked), "")

    def test_insufficient_context_never_becomes_a_mechanism_card(self):
        packet, _ = sampler_case()
        result = dict(status="insufficient_evidence", reason="Required dependency is not available.", changes=[])
        self.assertEqual(parse(result, packet), result)
        self.assertEqual(assessment_text(result), "")

    def test_three_statuses_have_mutually_exclusive_change_contracts(self):
        packet, good = sampler_case()
        for status in ("no_change", "insufficient_evidence"):
            result = copy.deepcopy(good)
            result["status"] = status
            with self.subTest(status=status), self.assertRaisesRegex(ValueError, "must have no changes"):
                parse(result, packet)
        good["changes"] = []
        with self.assertRaisesRegex(ValueError, "requires at least one"):
            parse(good, packet)

    def test_invalid_status_reason_and_word_budget_are_rejected(self):
        packet, good = sampler_case()
        for field, value, message in (("status", "unknown", "status must"), ("reason", " ", "reason must")):
            result = copy.deepcopy(good)
            result[field] = value
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, message):
                parse(result, packet)
        good["changes"][0]["description"] = " ".join(["word"] * 161)
        with self.assertRaisesRegex(ValueError, "160-word"):
            parse(good, packet)

    def test_import_and_reembedding_guard_clears_refusal_text_and_vector(self):
        for status in ("no_change", "insufficient_evidence"):
            for explicit_status in (False, True):
                card = dict(status=status, reason="Original audited reason must survive.", changes=[])
                row = dict(text="No substantive change was confirmed.", embedding=[1.0, 0.0],
                           embedding_model="old-model", extraction_status="ok", mechanism_card=copy.deepcopy(card))
                if explicit_status:
                    row["assessment_status"] = status
                with self.subTest(status=status, explicit_status=explicit_status):
                    self.assertTrue(preserve_assessment_status(row))
                    self.assertEqual(row["assessment_status"], status)
                    self.assertEqual(row["extraction_status"], status)
                    self.assertEqual(row["text"], "")
                    self.assertNotIn("embedding", row)
                    self.assertNotIn("embedding_model", row)
                    self.assertEqual(row["mechanism_card"], card)
                    self.assertTrue(preserve_assessment_status(row))  # Repeated import is idempotent.

    def test_ordinary_summaries_and_evidenced_changed_records_are_untouched(self):
        for row in (dict(text="Classifier with balanced sampling.", extraction_status="ok"),
                    dict(assessment_status="changed", text="Activate balanced sampling.",
                         extraction_status="ok", embedding=[1.0, 0.0], embedding_model="test")):
            original = copy.deepcopy(row)
            self.assertFalse(preserve_assessment_status(row))
            self.assertEqual(row, original)

    def test_card_only_changed_status_is_available_to_coverage(self):
        row = dict(task="t", run_id="r", arm="A", stage="improve", view="implementation",
                   text="Activate sampler.", extraction_status="ok", mechanism_card={"status": "changed"})
        self.assertFalse(preserve_assessment_status(row))
        self.assertEqual(cv.coverage_rows([row], [])[0]["n_changed"], 1)

    def test_malformed_status_reports_a_validation_error(self):
        for value in ({"status": "changed"}, [], True):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "Unknown mechanism assessment status"):
                preserve_assessment_status({"assessment_status": value})


class AssessmentIntegrationTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)

    def test_unknown_or_conflicting_import_states_are_rejected(self):
        for row in (dict(assessment_status="changed", mechanism_card={"status": "no_change"}),
                    dict(assessment_status="uncertain"),
                    dict(mechanism_card={"status": "unrecognized"})):
            original = copy.deepcopy(row)
            with self.subTest(row=row), self.assertRaisesRegex(ValueError, "Unknown|Conflicting"):
                preserve_assessment_status(row)
            self.assertEqual(row, original)

    def test_reembed_preserves_card_only_empty_non_scoring_rows(self):
        rows = [dict(text="", mechanism_card=dict(status=status, reason="Keep this reason.", changes=[]),
                     embedding=[1, 0], embedding_model="stale", extraction_status="ok")
                for status in ("no_change", "insufficient_evidence")]
        rows.append(dict(text="A measured mechanism.", assessment_status="changed",
                         embedding=[0, 1], embedding_model="old", extraction_status="ok"))
        cv.prepare_reembedding(rows)
        for row, status in zip(rows, ("no_change", "insufficient_evidence")):
            self.assertEqual(row["assessment_status"], status)
            self.assertEqual(row["extraction_status"], status)
            self.assertEqual(row["text"], "")
            self.assertEqual(row["mechanism_card"]["reason"], "Keep this reason.")
            self.assertNotIn("embedding", row)
        self.assertEqual(rows[-1]["text"], "A measured mechanism.")
        self.assertNotIn("embedding", rows[-1])
        self.assertNotIn("extraction_status", rows[-1])

    def test_cli_scores_only_changed_vectors_and_preserves_all_no_change_run(self):
        def record(candidate, arm, status, vector):
            return dict(task="task", run_id="run-" + arm, arm=arm, candidate_id=candidate,
                        stage="improve", view="implementation", representation_version=cv.CHANGE_VERSION,
                        text="Measured mechanism." if status == "changed" else "Refusal must never be embedded.",
                        assessment_status=status, extraction_status="ok", embedding=vector,
                        embedding_model="fixture-vectors")

        for insufficient in (False, True):
            rows = [record("a1", "A", "changed", [1, 0]), record("a2", "A", "changed", [0, 1]),
                    record("a3", "A", "no_change", [1, 1]),
                    record("f1", "F", "no_change", [1, 1]), record("f2", "F", "no_change", [1, -1])]
            if insufficient:
                rows.append(record("a4", "A", "insufficient_evidence", [-1, 1]))
            source = self.root / f"input-{insufficient}.jsonl"
            out = self.root / f"out-{insufficient}"
            source.write_text("".join(json.dumps(row) + "\n" for row in rows))
            with self.subTest(insufficient=insufficient), patch.object(cv, "Summarizer") as summarizer, \
                    patch.dict(sys.modules, {"sentence_transformers": None}), contextlib.redirect_stdout(io.StringIO()):
                result = cv.main(["--input", str(source), "--out", str(out), "--no-plots"])
                self.assertEqual(result, 2 if insufficient else 0)
            summarizer.assert_not_called()
            with (out / "run_scores.csv").open() as stream:
                scores = list(csv.DictReader(stream))
            self.assertEqual(len(scores), 1)
            self.assertEqual(scores[0]["run_id"], "run-A")
            self.assertEqual(int(scores[0]["n_total"]), 2)
            self.assertAlmostEqual(float(scores[0]["vendi"]), 2.0)
            with (out / "coverage.csv").open() as stream:
                coverage = {row["run_id"]: row for row in csv.DictReader(stream)}
            a, f = coverage["run-A"], coverage["run-F"]
            self.assertEqual(int(a["n_available"]), 2)
            self.assertEqual(int(a["n_changed"]), 2)
            self.assertEqual(int(a["n_no_change"]), 1)
            self.assertEqual(int(a["n_insufficient"]), int(insufficient))
            self.assertEqual(int(a["n_errors"]), 0)
            self.assertAlmostEqual(float(a["changed_fraction"]), 2 / (4 if insufficient else 3))
            self.assertEqual(int(f["n_candidates"]), 2)
            self.assertEqual(int(f["n_available"]), 0)
            self.assertEqual(int(f["n_no_change"]), 2)
            self.assertEqual(f["issue"], "no_measurable_changes")
            exported = [json.loads(line) for line in (out / "samples.jsonl").read_text().splitlines()]
            for row in exported:
                if row["assessment_status"] != "changed":
                    self.assertEqual(row["text"], "")
                    self.assertNotIn("embedding", row)
            self.assertIn("CONDITIONAL", (out / "REPORT.md").read_text())
            self.assertIn("| run-F | F | 2 | 0 | 0 | 2 | 0 |", (out / "REPORT.md").read_text())
            self.assertEqual(json.loads((out / "manifest.json").read_text())["summary_api_calls"], 0)

    def test_representation_versions_reject_mixed_estimands_within_a_group_only(self):
        base = dict(task="task", stage="improve", view="implementation")
        old = base | {"representation_version": "summary-v1"}
        new = base | {"representation_version": cv.CHANGE_VERSION}
        for other in (old, base):
            with self.subTest(other=other), self.assertRaisesRegex(ValueError, "Mixed representation versions"):
                cv.validate_representation_versions([new, other])
        cv.validate_representation_versions([new, old | {"stage": "draft"}, old | {"view": "proposal"}])
        cv.validate_representation_versions([base, base.copy()])  # Legacy-only inputs still work.

    def test_diff_cache_is_separate_from_legacy_summary_cache_and_is_reused(self):
        packet, result = sampler_case()
        old = {field: "" for field in cv.FIELDS}
        old.update(model="linear classifier", evidence=["CHILD:1"])
        legacy_ask, change_ask = Mock(return_value=json.dumps(old)), Mock(return_value=json.dumps(result))
        cache = self.root / "cache"
        summarizer = cv.Summarizer(cache, model="fixture", ask=legacy_ask)
        self.assertEqual(summarizer.extract("legacy single-candidate summary"), old)
        legacy_paths = list((cache / "summaries").glob("*.json"))
        self.assertEqual(len(legacy_paths), 1)
        original_bytes = legacy_paths[0].read_bytes()
        self.assertEqual(summarizer.assess_change(packet, ask=change_ask), result)
        self.assertEqual(summarizer.calls, 2)
        self.assertEqual(len(list((cache / "changes").glob("*.json"))), 1)
        self.assertEqual(legacy_paths[0].read_bytes(), original_bytes)
        no_call = Mock(side_effect=AssertionError("Successful cached calls must not repeat."))
        reloaded = cv.Summarizer(cache, model="fixture", ask=no_call)
        self.assertEqual(reloaded.assess_change(packet, ask=no_call), result)
        self.assertEqual(reloaded.extract("legacy single-candidate summary"), old)
        self.assertEqual(reloaded.calls, 0)
        no_call.assert_not_called()

    def test_invalid_quote_retry_supplies_feedback_with_original_diff(self):
        packet, valid = sampler_case()
        invalid = copy.deepcopy(valid)
        invalid["changes"][0]["evidence"][1]["quote"] = "fake_loader(dataset)"
        ask = Mock(side_effect=[json.dumps(invalid), json.dumps(valid)])
        summarizer = cv.Summarizer(self.root / "cache", ask=ask)
        self.assertEqual(summarizer.assess_change(packet, ask=ask), valid)
        self.assertEqual(summarizer.calls, 2)
        prompts = [call.args[0] for call in ask.call_args_list]
        self.assertNotIn("Your previous JSON was rejected", prompts[0])
        self.assertIn("does not match source", prompts[1])
        self.assertIn("Previous JSON:", prompts[1])
        self.assertIn(packet["diff"], prompts[1])
        cached = list((self.root / "cache" / "changes").glob("*.json"))
        self.assertEqual(len(cached), 1)
        self.assertEqual(json.loads(cached[0].read_text()), valid)

    def test_identical_equivalent_and_oversized_packets_need_no_llm(self):
        packets = [build_change_packet(SAMPLER_PARENT, SAMPLER_PARENT),
                   build_change_packet("x = model(data)\n", "# unchanged computation\nx=model(data)\n"),
                   build_change_packet(SAMPLER_PARENT, SAMPLER_CHILD, max_chars=1)]
        ask = Mock(side_effect=AssertionError("Deterministic decisions must not call the model."))
        summarizer = cv.Summarizer(self.root / "cache", ask=ask)
        with patch.object(summarizer, "request", ask):
            for packet, status in zip(packets, ("no_change", "no_change", "insufficient_evidence")):
                result = summarizer.assess_change(packet, ask=ask)
                self.assertEqual(result["status"], status)
                self.assertEqual(assessment_text(result), "")
        ask.assert_not_called()
        self.assertEqual(summarizer.calls, 0)

    def test_repeated_invalid_quotes_are_bounded_and_never_cached(self):
        packet, invalid = sampler_case()
        invalid["changes"][0]["evidence"][1]["quote"] = "invented source"
        ask = Mock(return_value=json.dumps(invalid))
        summarizer = cv.Summarizer(self.root / "cache", ask=ask)
        with self.assertRaisesRegex(ValueError, "Change evidence validation failed"):
            summarizer.assess_change(packet, ask=ask)
        self.assertEqual(ask.call_count, 3)
        self.assertEqual(list((self.root / "cache").rglob("*.json")), [])

    def test_transport_timeout_retries_same_prompt_and_caches_recovery(self):
        packet, valid = sampler_case()
        ask = Mock(side_effect=[TimeoutError("private transport details"), json.dumps(valid)])
        summarizer = cv.Summarizer(self.root / "cache", ask=ask)
        with patch.object(cv.time, "sleep") as sleep:
            self.assertEqual(summarizer.assess_change(packet, ask=ask), valid)
        self.assertEqual(summarizer.calls, 2)
        sleep.assert_called_once_with(1)
        self.assertEqual(ask.call_args_list[0], ask.call_args_list[1])
        self.assertNotIn("private transport details", ask.call_args_list[1].args[0])
        no_call = Mock(side_effect=AssertionError("Recovered assessment must be cached"))
        self.assertEqual(summarizer.assess_change(packet, ask=no_call), valid)
        no_call.assert_not_called()

    def test_transport_and_validation_share_a_bounded_retry_budget(self):
        packet, invalid = sampler_case()
        invalid["changes"][0]["evidence"][1]["quote"] = "invented source"
        ask = Mock(side_effect=[TimeoutError(), json.dumps(invalid), TimeoutError()])
        summarizer = cv.Summarizer(self.root / "cache", ask=ask)
        with patch.object(cv.time, "sleep") as sleep, self.assertRaises(TimeoutError):
            summarizer.assess_change(packet, ask=ask)
        self.assertEqual(ask.call_count, 3)
        self.assertEqual(summarizer.calls, 3)
        sleep.assert_called_once_with(1)
        self.assertEqual(list((self.root / "cache").rglob("*.json")), [])
        self.assertIn("does not match source", ask.call_args_list[2].args[0])
        self.assertNotIn("TimeoutError", ask.call_args_list[2].args[0])


if __name__ == "__main__":
    unittest.main()
