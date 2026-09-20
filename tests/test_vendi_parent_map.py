"""Read actual MLEvolve parent maps without silently measuring whole improvements."""

import csv
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import compare_vendi as cv


class ParentMapTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.journal = self.root / "runs" / "run" / "logs" / "journal.json"
        self.journal.parent.mkdir(parents=True)
        self.inventory = self.root / "inventory.csv"
        with self.inventory.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=["name", "task", "arm", "verdict"])
            writer.writeheader()
            writer.writerow(dict(name="run", task="task", arm="A", verdict="ok"))
        self.nodes = [dict(id="root", stage="root", parent=None),
                      dict(id="parent", stage="draft", parent=None, code="loss = mse", plan="Use MSE"),
                      dict(id="child", stage="improve", parent=None, code="loss = huber", plan="Change loss")]

    def load(self, **data):
        self.journal.write_text(json.dumps(dict(nodes=self.nodes, **data)))
        records, issues = cv.load_runs(self.root / "runs", self.inventory, "*",
                                      ["implementation", "proposal"])
        self.assertEqual(issues, [])
        return {(row["candidate_id"], row["view"]): row for row in records}

    def test_actual_journal_map_with_null_inline_parents(self):
        rows = self.load(node2parent={"parent": "root", "child": "parent"})
        child = rows["child", "implementation"]
        self.assertEqual(child["parent_id"], "parent")
        self.assertEqual(child["parent_status"], "available")
        self.assertEqual(child["extraction_status"], "pending")
        self.assertIn("PARENT:1: loss = mse", child["parent_source"])
        self.assertIn("CHILD:1: loss = huber", child["source"])
        self.assertTrue(child["source_refs"][-1].endswith("#node_id=parent"))
        draft = rows["parent", "implementation"]
        self.assertEqual(draft["parent_status"], "not_applicable")
        self.assertEqual(draft["extraction_status"], "pending")
        self.assertEqual(draft["parent_source"], "")

    def test_legacy_inline_parent_and_agreeing_map(self):
        self.nodes[-1]["parent"] = "parent"
        legacy = self.load()["child", "implementation"]
        mapped = self.load(node2parent={"child": "parent"})["child", "implementation"]
        self.assertEqual(legacy["parent_source"], mapped["parent_source"])
        self.assertEqual(legacy["source_hash"], mapped["source_hash"])

    def test_conflicting_parent_ids_fail_clearly(self):
        self.nodes[-1]["parent"] = "root"
        with self.assertRaisesRegex(ValueError, "conflicting parent IDs for node child"):
            self.load(node2parent={"child": "parent"})

    def test_malformed_maps_fail_clearly(self):
        for mapping, message in [([], "node2parent must be an object"),
                                 ({"absent": "parent"}, "unknown child ID"),
                                 ({"child": ["parent"]}, "must be a string or null"),
                                 ({"child": "child"}, "cannot be its own parent")]:
            with self.subTest(mapping=mapping), self.assertRaisesRegex(ValueError, message):
                self.load(node2parent=mapping)

    def test_malformed_inline_parent_fails_clearly(self):
        self.nodes[-1]["parent"] = {"id": "parent"}
        with self.assertRaisesRegex(ValueError, "parent for node child must be a string or null"):
            self.load()

    def test_missing_parent_does_not_fall_back_to_whole_candidate(self):
        for mapping in ({}, {"child": "missing"}, {"child": "root"}):
            with self.subTest(mapping=mapping):
                rows = self.load(node2parent=mapping)
                child = rows["child", "implementation"]
                self.assertEqual(child["parent_status"], "missing")
                self.assertEqual(child["extraction_status"], "missing_source")
                self.assertEqual(child["error"], "parent_code_unavailable")
                self.assertEqual(child["representation_version"], cv.CHANGE_VERSION)
                cv.validate_representation_versions([child, child | {"candidate_id": "other", "representation_version": cv.CHANGE_VERSION}])
                self.assertEqual(rows["child", "proposal"]["extraction_status"], "pending")
                self.assertEqual(cv.coverage_rows([child], [])[0]["n_missing"], 1)

    def test_blank_parent_code_is_missing(self):
        self.nodes[1]["code"] = " \n "
        child = self.load(node2parent={"child": "parent"})["child", "implementation"]
        self.assertEqual(child["extraction_status"], "missing_source")
        self.assertEqual(child["error"], "parent_code_unavailable")

    def test_parent_changes_invalidate_source_hash(self):
        before = self.load(node2parent={"child": "parent"})["child", "implementation"]
        self.nodes[1]["code"] = "loss = l1"
        after = self.load(node2parent={"child": "parent"})["child", "implementation"]
        self.assertNotEqual(before["source_hash"], after["source_hash"])
        self.assertEqual(before["source"], after["source"])


if __name__ == "__main__":
    unittest.main()
