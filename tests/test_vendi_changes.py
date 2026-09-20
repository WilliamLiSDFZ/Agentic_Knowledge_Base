"""Source-grounded change packets preserve wiring and loss-update evidence."""

from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from vendi_changes import build_change_packet


class ChangePacketTests(unittest.TestCase):
    def test_sampler_definition_and_actual_loader_wiring(self):
        common = ("class BalancedSampler:\n"
                  "    def __iter__(self):\n"
                  "        return iter([1, 3, 2, 0])\n\n" + "# unrelated\n" * 30 +
                  "sampler = BalancedSampler()\n" + "# unrelated\n" * 30)
        parent = common + "loader = DataLoader(dataset, shuffle=True)\n"
        child = common + "loader = DataLoader(dataset, batch_sampler=sampler)\n"
        packet = build_change_packet(parent, child)
        self.assertEqual(packet["status"], "complete")
        self.assertIn("shuffle=True", packet["diff"])
        self.assertIn("batch_sampler=sampler", packet["diff"])
        self.assertIn("class BalancedSampler:", packet["context"])
        self.assertIn("sampler = BalancedSampler()", packet["context"])
        self.assertIn("not prove runtime", " ".join(packet["limitations"]))

    def test_ranking_gate_and_scaling_are_both_preserved(self):
        parent = ("def train(loss, rank_loss, step, accumulation):\n"
                  "    if (step + 1) % accumulation == 0:\n"
                  "        loss = loss + rank_loss\n"
                  "    loss.backward()\n")
        child = ("def train(loss, rank_loss, step, accumulation):\n"
                 "    loss = loss + rank_loss / accumulation\n"
                 "    loss.backward()\n")
        packet = build_change_packet(parent, child)
        self.assertEqual(packet["evidence_lines"]["PARENT:2"],
                         "    if (step + 1) % accumulation == 0:")
        self.assertEqual(packet["evidence_lines"]["CHILD:2"],
                         "    loss = loss + rank_loss / accumulation")
        self.assertIn("PARENT:2", packet["changed_refs"])
        self.assertIn("CHILD:2", packet["changed_refs"])

    def test_changed_function_includes_distant_callsite(self):
        parent = "def objective(x):\n    return x\n" + "# separator\n" * 50 + "loss = objective(batch)\n"
        child = parent.replace("return x", "return x.square()")
        packet = build_change_packet(parent, child)
        self.assertIn("loss = objective(batch)", packet["context"])
        unused = build_change_packet(parent.replace("loss = objective(batch)", "loss = batch"),
                                     child.replace("loss = objective(batch)", "loss = batch"))
        self.assertNotIn("objective(batch)", unused["context"] + unused["diff"])
        self.assertNotIn("active", unused)

    def test_removed_usage_remains_in_parent_evidence(self):
        parent = "def penalty(x):\n    return x.abs()\n" + "# padding\n" * 30 + "loss = penalty(x)\n"
        child = parent.replace("loss = penalty(x)", "loss = x")
        packet = build_change_packet(parent, child)
        self.assertIn("loss = penalty(x)", packet["diff"])
        self.assertIn("def penalty(x):", packet["context"])

    def test_module_grouping_connects_full_block_constructor_and_distant_step(self):
        parent = (
            "groups = {'backbone': [], 'head': []}\n"
            "for parameter_name, parameter in model.named_parameters():\n"
            "    is_backbone = parameter_name.startswith('encoder.')\n"
            + "    # grouping context\n" * 12 +
            "    if is_backbone:\n"
            "        group_name = 'backbone'\n"
            "    else:\n"
            "        group_name = 'head'\n"
            "    groups[group_name].append(parameter)\n"
            + "# unrelated\n" * 35 +
            "optimizer = AdamW(\n"
            "    [\n"
            "        {'params': groups['backbone'], 'lr': 8e-6},\n"
            "        {'params': groups['head'], 'lr': 6e-5},\n"
            "    ],\n"
            + "    # constructor context\n" * 12 +
            "    eps=1e-8,\n"
            ")\n"
            + "# unrelated\n" * 35 +
            "scaler.step(optimizer)\n"
            + "# unrelated\n" * 35 +
            "wrapper = wrap(optimizer)\n"
            + "# unrelated\n" * 35 +
            "consume(wrapper)\n"
        )
        child = parent.replace("'encoder.'", "'pretrained_model.roberta.'")
        packet = build_change_packet(parent, child)
        self.assertEqual(packet["version"], "vendi-change-packet-v2")
        shown = packet["diff"] + packet["context"]
        for source in ("groups[group_name].append(parameter)", "optimizer = AdamW(",
                       "eps=1e-8", "scaler.step(optimizer)"):
            self.assertIn(source, shown)
        step_line = child.splitlines().index("scaler.step(optimizer)") + 1
        self.assertIn(f"CHILD:{step_line}", packet["usage_refs"])
        self.assertNotIn("consume(wrapper)", shown)
        self.assertEqual(packet["omitted_context_lines"], 0)

    def test_short_local_control_block_not_entire_large_function(self):
        parent = ("def train():\n"
                  "    if enabled:\n"
                  "        weight = 1\n" + "        # context\n" * 12 +
                  "        loss.backward(weight)\n" + "    # unrelated\n" * 100 +
                  "    unrelated_call()\n")
        child = parent.replace("weight = 1", "weight = 2")
        packet = build_change_packet(parent, child)
        shown = packet["diff"] + packet["context"]
        self.assertIn("loss.backward(weight)", shown)
        self.assertNotIn("unrelated_call()", shown)

    def test_large_diff_does_not_return_truncated_success(self):
        parent = "x = 0\n" * 60
        child = "y = 1\n" * 60
        packet = build_change_packet(parent, child, max_chars=200)
        self.assertEqual(packet["status"], "insufficient_evidence")
        self.assertEqual(packet["reason"], "complete_diff_exceeds_budget")
        self.assertGreater(packet["required_diff_chars"], 200)
        self.assertEqual(packet["diff"], "")
        self.assertEqual(packet["evidence_lines"], {})

    def test_diff_complete_when_optional_context_does_not_fit(self):
        parent = "def objective(x):\n    return x\n" + "# padding\n" * 40 + "loss = objective(x)\n"
        child = parent.replace("return x", "return x.square()")
        complete = build_change_packet(parent, child)
        packet = build_change_packet(parent, child, max_chars=len(complete["diff"]))
        self.assertEqual(packet["status"], "complete")
        self.assertEqual(packet["diff"], complete["diff"])
        self.assertGreater(packet["omitted_context_lines"], 0)
        self.assertEqual(packet["context"], "")

    def test_exact_references_only_for_sent_lines(self):
        parent = "def objective(x):\n    return x\n" + "# padding\n" * 40 + "loss = objective(x)\n"
        child = parent.replace("return x", "return x + 1")
        packet = build_change_packet(parent, child)
        sources = {"PARENT": parent.splitlines(), "CHILD": child.splitlines()}
        sent = packet["diff"] + packet["context"]
        for ref, raw in packet["evidence_lines"].items():
            side, number = ref.split(":")
            self.assertEqual(raw, sources[side][int(number) - 1])
            self.assertIn(ref + ": " + raw, sent)
        self.assertTrue(set(packet["changed_refs"]) <= packet["evidence_lines"].keys())

    def test_all_separated_hunks_are_present(self):
        parent = "a = 1\n" + "# padding\n" * 40 + "b = 2\n"
        child = parent.replace("a = 1", "a = 3").replace("b = 2", "b = 4")
        packet = build_change_packet(parent, child)
        self.assertEqual(packet["diff"].count("@@ PARENT"), 2)
        self.assertIn("CHILD:1", packet["changed_refs"])
        self.assertIn("CHILD:42", packet["changed_refs"])

    def test_identical_and_final_newline_changes(self):
        same = build_change_packet("x = 1\n", "x = 1\n")
        self.assertTrue(same["identical"])
        self.assertEqual(same["diff"], "")
        changed = build_change_packet("x = 1\n", "x = 1")
        self.assertFalse(changed["identical"])
        self.assertIn("[no newline]", changed["diff"])
        self.assertTrue(changed["ast_equal"])
        self.assertNotEqual(changed["source_hashes"]["parent"], changed["source_hashes"]["child"])

    def test_ast_only_formatting_changes_and_static_usage_refs(self):
        parent = "def f(x):\n    return x + 1\n\ny = f(2)\n"
        child = "def f(x):\n    return x+1  # same operation\n\ny = f(2)\n"
        packet = build_change_packet(parent, child)
        self.assertTrue(packet["ast_equal"])
        self.assertIn("CHILD:4", packet["usage_refs"])
        self.assertNotIn("CHILD:1", packet["usage_refs"])
        self.assertTrue(set(packet["usage_refs"]) <= packet["evidence_lines"].keys())
        changed = build_change_packet(parent, child.replace("x+1", "x+2"))
        self.assertFalse(changed["ast_equal"])

    def test_syntax_error_has_explicit_fallback(self):
        packet = build_change_packet("def broken(\n", "def still_broken(\n")
        self.assertEqual(packet["status"], "complete")
        self.assertTrue(any("AST unavailable" in text for text in packet["limitations"]))
        self.assertIsNone(packet["ast_equal"])
        self.assertEqual(packet["evidence_lines"]["PARENT:1"], "def broken(")

    def test_source_is_not_executed(self):
        with tempfile.TemporaryDirectory() as directory:
            sentinel = Path(directory) / "should-not-exist"
            code = f"__import__('pathlib').Path({str(sentinel)!r}).touch()\n"
            packet = build_change_packet("pass\n", code)
            self.assertEqual(packet["status"], "complete")
            self.assertFalse(sentinel.exists())

    def test_invalid_arguments(self):
        for budget in (0, -1, True, 1.5):
            with self.subTest(budget=budget), self.assertRaises(ValueError):
                build_change_packet("", "", budget)
        with self.assertRaises(TypeError):
            build_change_packet(None, "")


if __name__ == "__main__":
    unittest.main()
