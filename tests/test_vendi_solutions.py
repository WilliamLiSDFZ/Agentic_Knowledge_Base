"""Offline contracts for complete-solution evidence, coverage and cache identity."""
import json
from pathlib import Path
import re
import sys
import tempfile
import types
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from vendi import runtime as vs


def card(evidence=None, **changes):
    return dict(title="Linear classifier", summary="Fit a linear classifier with cross entropy.",
                evidence=evidence if evidence is not None else ["SOURCE:1"]) | changes


def numbered_source(text):
    return "\n".join(f"SOURCE:{i}: {line}" for i, line in enumerate(text.splitlines(), 1))


class SolutionCardTests(unittest.TestCase):
    def test_schema_limits_and_line_ranges(self):
        good = card(["SOURCE:1", "SOURCE:3-4"])
        self.assertEqual(vs.validate_solution_card(json.dumps(good), {1, 3, 4}), good)
        invalid = [card([]), card(["CHILD:1"]), card(["SOURCE:0"]), card(["SOURCE:4-3"]),
                   card(["SOURCE:1-4"]), card(["SOURCE:9"]), card(["SOURCE:1-9999999999"]),
                   card(summary=""), card(title=" "), card(summary="word " * 161),
                   card(title="word " * 13), card(title="x" * 161), card(extra="unsupported")]
        for value in invalid:
            with self.subTest(value=value), self.assertRaises(ValueError):
                vs.validate_solution_card(json.dumps(value), {1, 3, 4})


class SolutionExtractionTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.cache = Path(directory.name)

    def extractor(self, ask, **options):
        return vs.SolutionSummarizer(self.cache, ask=ask, **options)

    def test_invalid_numbered_source_and_chunk_sizes_fail_before_calls(self):
        ask = Mock()
        for source in ("", "pass", "SOURCE:2: pass", "SOURCE:1: pass\nSOURCE:3: x"):
            with self.subTest(source=source), self.assertRaises(ValueError):
                self.extractor(ask).summarize_solution(source)
        for limit in (0, -1, True, 1.5):
            with self.subTest(limit=limit), self.assertRaises(ValueError):
                self.extractor(ask, chunk_chars=limit)
        ask.assert_not_called()

    def test_complete_chunk_coverage_including_long_line_tail_and_bounded_merges(self):
        fragments, merge_sizes = [], []

        def ask(prompt):
            if prompt.startswith("Solution source fragment"):
                fragments.append(prompt.split("\n", 2)[2])
                start, end = re.search(r"Available source lines: SOURCE:(\d+)-(\d+)", prompt).groups()
                return json.dumps(card([f"SOURCE:{start}-{end}"]))
            cards = json.loads(prompt.split("\n", 1)[1])
            merge_sizes.append(len(cards))
            return json.dumps(card(sorted(set(reference for item in cards for reference in item["evidence"]))))

        source = numbered_source("prefix\n" + "x" * 2000 + "_long_line_tail\nlast_line")
        result, count = self.extractor(ask, chunk_chars=100).summarize_solution(source)
        self.assertEqual("".join(fragments), source)
        self.assertEqual(count, len(fragments))
        self.assertGreater(count, 16)
        self.assertGreater(len(merge_sizes), 4)
        self.assertTrue(all(1 <= size <= 4 for size in merge_sizes))
        self.assertIn(3, vs._evidence_lines(result["evidence"], {1, 2, 3}))

    def test_fragment_cannot_cite_lines_only_present_in_other_fragments(self):
        source = numbered_source("first" + "x" * 100 + "\nsecond")
        ask = Mock(return_value=json.dumps(card(["SOURCE:2"])))
        with self.assertRaisesRegex(ValueError, "after 3 attempts"):
            self.extractor(ask, chunk_chars=40).summarize_solution(source)
        self.assertEqual(ask.call_count, 3)
        self.assertIn("unavailable source lines", ask.call_args.args[0])

    def test_merge_may_only_cite_lines_cited_in_input_cards(self):
        source = numbered_source("first\nuncited\n" + "x" * 60 + "\ntail")
        merges = []

        def ask(prompt):
            if prompt.startswith("Solution source fragment"):
                start = re.search(r"Available source lines: SOURCE:(\d+)-", prompt).group(1)
                return json.dumps(card([f"SOURCE:{start}"]))
            merges.append(prompt)
            return json.dumps(card(["SOURCE:2"]))

        with self.assertRaisesRegex(ValueError, "after 3 attempts"):
            self.extractor(ask, chunk_chars=60).summarize_solution(source)
        self.assertEqual(len(merges), 3)

    def test_retries_share_budget_and_do_not_copy_transport_error_into_prompt(self):
        responses = [TimeoutError("secret endpoint detail"), json.dumps(card(["SOURCE:99"])), json.dumps(card())]
        ask = Mock(side_effect=responses)
        with patch.object(vs.time, "sleep"):
            result, count = self.extractor(ask).summarize_solution("SOURCE:1: model.fit(x, y)")
        self.assertEqual(result, card())
        self.assertEqual(count, 1)
        self.assertEqual(ask.call_count, 3)
        self.assertNotIn("secret endpoint detail", str(ask.call_args_list))
        self.assertIn("Your previous JSON was rejected", ask.call_args.args[0])

    def test_transport_failure_stops_after_three_attempts_without_cached_card(self):
        ask = Mock(side_effect=TimeoutError("secret endpoint detail"))
        with patch.object(vs.time, "sleep"), self.assertRaisesRegex(RuntimeError, r"TimeoutError; attempts=3") as error:
            self.extractor(ask).summarize_solution("SOURCE:1: pass")
        self.assertNotIn("secret endpoint detail", str(error.exception))
        self.assertEqual(ask.call_count, 3)
        self.assertEqual(list(self.cache.rglob("*.json")), [])

    def test_cache_reuses_same_code_and_isolates_other_namespaces(self):
        source = "SOURCE:1: model.fit(x, y)"
        # The identical key in another namespace must never supply a solution card.
        key = "19117d179573dee16665972604085e6c34bc92f838f5bf16a707facae3a1c19f"
        vs.write_json(self.cache / "summaries" / f"{key}.json", {"unrelated": True})
        ask = Mock(return_value=json.dumps(card()))
        first = self.extractor(ask)
        result = first.summarize_solution(source)
        self.assertEqual(first.calls, 1)
        second = self.extractor(Mock(side_effect=AssertionError("must use cache")))
        self.assertEqual(second.summarize_solution(source), result)
        self.assertEqual(second.calls, 0)
        self.assertEqual(len(list((self.cache / "summaries").glob("*.json"))), 1)
        self.assertEqual(len(list((self.cache / "solution_summaries").glob("*.json"))), 1)

    def test_existing_solution_cache_survives_package_move(self):
        # Generated by the pre-package implementation for this source/model/endpoint.
        key = "19117d179573dee16665972604085e6c34bc92f838f5bf16a707facae3a1c19f"
        vs.write_json(self.cache / "solution_summaries" / f"{key}.json", card())
        ask = Mock(side_effect=AssertionError("cached result must not request a model"))
        result, count = self.extractor(ask).summarize_solution("SOURCE:1: model.fit(x, y)")
        self.assertEqual(result, card())
        self.assertEqual(count, 1)
        ask.assert_not_called()

    def test_cache_identity_includes_whole_source_model_endpoint_api_and_prompt(self):
        ask = Mock(return_value=json.dumps(card()))
        source = "SOURCE:1: train()"
        extractor = self.extractor(ask, model="model-a")
        extractor.summarize_solution(source)
        for attribute, value in (("model", "model-b"), ("endpoint", "other"), ("api", "responses")):
            setattr(extractor, attribute, value)
            extractor.summarize_solution(source)
        with patch.object(vs, "SOLUTION_PROMPT", vs.SOLUTION_PROMPT + " revised"):
            extractor.summarize_solution(source)
        extractor.summarize_solution(source + "\nSOURCE:2: infer()")
        self.assertEqual(ask.call_count, 6)

    def test_shared_first_fragment_does_not_collide_between_distinct_whole_sources(self):
        ask = Mock(return_value=json.dumps(card()))
        extractor = self.extractor(ask, chunk_chars=40)
        first = "SOURCE:1: " + "x" * 60 + "first"
        second = "SOURCE:1: " + "x" * 60 + "second"
        extractor.summarize_solution(first)
        previous = ask.call_count
        extractor.summarize_solution(second)
        self.assertEqual(ask.call_count, previous * 2)

    def test_request_reuses_llm_configuration_and_solution_system_prompt(self):
        configured = types.ModuleType("llm")
        configured.MODEL, configured.BASE_URL = "gpt-5.6-terra", "test-endpoint"
        configured.client = Mock()
        client = configured.client.with_options.return_value
        client.chat.completions.create.return_value = types.SimpleNamespace(
            choices=[types.SimpleNamespace(message=types.SimpleNamespace(content="reply"))])
        client.responses.create.return_value = types.SimpleNamespace(output_text="response")
        with patch.dict(sys.modules, {"llm": configured}):
            extractor = vs.SolutionSummarizer(self.cache)
            self.assertEqual(extractor.request("source"), "reply")
            extractor.api = "responses"
            self.assertEqual(extractor.request("source"), "response")
        configured.client.with_options.assert_called_once_with(max_retries=0, timeout=120)
        self.assertEqual(extractor.endpoint, "test-endpoint")
        client.chat.completions.create.assert_called_once_with(
            model="gpt-5.6-terra", messages=[{"role": "system", "content": vs.SOLUTION_PROMPT},
                                           {"role": "user", "content": "source"}],
            max_completion_tokens=4096)
        client.responses.create.assert_called_once_with(
            model="gpt-5.6-terra", instructions=vs.SOLUTION_PROMPT, input="source", max_output_tokens=4096)


if __name__ == "__main__":
    unittest.main()
