"""Probe the paper corpus the way the analogy agent will search it: does a structural query
retrieve the right MECHANISM FAMILY?

Runs BM25 alone — no LLM calls, no run — so a change to the corpus, the tokenizer, or the
query style can be judged in seconds. It imports the production tokenizer and BM25 from
MLEvolve (`engine/analogy/corpus.py`) rather than re-implementing them, so what it measures is
what the agent gets; point --mlevolve at the checkout if it is not the sibling directory.

The cases are the ten retrospective MLE-bench/Kaggle cases from the structural-analogy memo
(`structural_analogy_retrieval_mlebench_cases_zh.docx`, 2026-08-31). Each has two queries:
  structural  the memo's "how the agent would ask" sentence, in English — what a naive
              agent writes;
  mechanism   3-8 mechanism terms in another subfield's vocabulary — what the prompt asks
              the agent to write;
and a keyword list naming the expected mechanism family. A case is a hit when at least one of
the top-k titles/tldrs contains one of its keywords.

Measured 2026-09-02 on the local 12.8k-paper corpus (5 venues, 2024), k=10: mechanism queries
9/10, structural sentences 7/10. A stricter manual read of the top-8 (is the paper's mechanism
the memo's mechanism, not just a keyword) gave 7/10 vs 3/10 — the gap that fixed the "3-6 terms
per query, other subfields' vocabulary" rule in the agent prompt. The persistent miss is Jigsaw:
test-time augmentation / orbit averaging is rarely named in abstracts of this corpus, so the
agent has to reach it by rewording (consistency regularization, augmentation invariance).
Keyword lists are deliberately narrow; a hit here is evidence, not proof — read the titles.

Usage:
    python scripts/probe_analogy.py --corpus output/paper_corpus
    python scripts/probe_analogy.py --corpus output/paper_corpus --k 10 --show 5
    python scripts/probe_analogy.py --corpus ... --query "coarse-to-fine region proposal gigapixel"
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

CASES = [
    ("LMSYS position bias", ["equivarian", "symmetriz", "permutation", "group averag", "canonicaliz", "frame averag"],
     "model predicts over an ordered pair of candidates; swapping the two inputs should permute the output distribution but the model violates this symmetry; enforce the symmetry while keeping probabilities calibrated",
     "permutation equivariance symmetrization pairwise comparison antisymmetry group averaging swap augmentation consistency"),
    ("Jigsaw invariance", ["test-time augmentation", "test time augmentation", "orbit", "consistency regulari", "paraphras", "back-translation", "augmentation consistency"],
     "target label should be invariant under a set of meaning-preserving input transformations but predictions are sensitive to them; use the whole transformation orbit to stabilize predictions",
     "invariance test-time augmentation orbit averaging consistency regularization paraphrase back-translation invariant prediction"),
    ("Essay ordinal", ["ordinal", "ordinality", "ordered label", "kappa"],
     "labels are ordered grades and the evaluation cost grows with the distance between predicted and true grade but the classification objective ignores label geometry",
     "ordinal regression distance-aware loss threshold optimization quadratic weighted kappa ordered labels"),
    ("Essay domain shift", ["domain adapt", "domain shift", "label shift", "pseudo-label", "pseudo label", "pseudo-labell"],
     "same input to output task but the large source data and the small target data have different labeling rules; use the source data without imposing its labeling rule on the target",
     "domain adaptation source target label shift pseudo-labeling relabeling two-stage fine-tuning annotation guideline mismatch"),
    ("Contrails temporal fusion", ["temporal fusion", "temporal feature", "video semantic segmentation", "video segmentation", "multi-frame", "registration", "misalign", "spatio-temporal", "temporal consistency"],
     "multiple adjacent unregistered observations provide extra evidence for a thin elongated target but fusing them at full resolution blurs pixel-level localization due to large displacement; at what scale to fuse temporal information",
     "coarse scale temporal fusion low resolution feature aggregation multi-frame segmentation misalignment registration video thin structures"),
    ("RSNA cascade", ["multiple instance", "multi-instance", "multi instance", "whole slide", "coarse-to-fine", "weakly supervised localization", "weakly-supervised localization", "cascade", "patch-level", "proposal"],
     "a huge ordered volume composed of known repeated units; anomalies are tiny and local; only few samples have localization labels; narrow the support first then classify local instances at high resolution and aggregate",
     "coarse-to-fine detection localize then classify multiple instance learning weakly supervised localization cascade whole slide patch aggregation"),
    ("Vesuvius depth nuisance", ["invarian", "nuisance", "marginali", "pooling"],
     "2D target supported by a local 3D pattern along a short depth axis whose absolute offset is a nuisance variable; exploit 3D context while making the 2D prediction insensitive to absolute depth",
     "nuisance variable invariance marginalization shift invariant pooling 3D to 2D projection aggregation depth invariant"),
    ("NFL gating", ["cascade", "two-stage", "early exit", "early-exit", "gating", "screening", "rerank", "coarse-to-fine", "hard negative"],
     "huge candidate set with extremely sparse positives; cheap structured features can reject most negatives at high recall and an expensive perceptual model only helps on ambiguous candidates; how to combine screening expensive recognition and calibration",
     "cascade classifier early rejection two-stage screening expensive model gating reranking calibration rare positives"),
    ("Lyft rotation", ["equivarian", "rotation", "group averag", "symmetriz", "test-time augmentation"],
     "task should be equivariant under known rigid transformations but the detector predictions do not obey it; approximate the structure at inference without rewriting the network to be strictly equivariant",
     "rotation equivariance test-time augmentation group averaging rotated bounding box detection symmetrization inference"),
    ("Breast ROI", ["region proposal", "coarse-to-fine", "gigapixel", "cropping", "two-stage", "region of interest", "spatial redundancy", "patch selection"],
     "discriminative signal exists only in a tiny unknown region of a huge high-resolution input; global downsampling destroys it and full-resolution computation is too expensive; let a cheap model decide where expensive computation happens",
     "region proposal coarse-to-fine high resolution attention cropping compute allocation two-stage detection classification gigapixel"),
]


def _import_corpus(mlevolve: Path):
    sys.path.insert(0, str(mlevolve))
    try:
        from engine.analogy.corpus import load_corpus  # noqa: WPS433
    except ImportError as e:
        raise SystemExit(f"cannot import MLEvolve's engine/analogy/corpus.py from {mlevolve} "
                         f"({e}); pass --mlevolve <checkout>") from e
    return load_corpus


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--corpus", default=str(REPO_ROOT / "output" / "paper_corpus"))
    ap.add_argument("--mlevolve", default=str(REPO_ROOT.parent / "MLEvolve"),
                    help="MLEvolve checkout (default: sibling directory)")
    ap.add_argument("--k", type=int, default=10, help="hits per query")
    ap.add_argument("--show", type=int, default=5, help="titles printed per query")
    ap.add_argument("--query", help="run one ad-hoc query instead of the cases")
    args = ap.parse_args()

    load_corpus = _import_corpus(Path(args.mlevolve))
    t0 = time.time()
    corpus = load_corpus(args.corpus)
    if corpus is None:
        return 1
    print(f"corpus {args.corpus}: {len(corpus)} papers, sha1 {corpus.digest}, "
          f"loaded in {time.time() - t0:.1f}s\n")

    def show(query: str, keywords: list[str] | None) -> bool:
        hits = corpus.search(query, k=args.k)
        hit_rows = []
        for h in hits:
            text = (h["title"] + " " + h["tldr"]).lower()
            hit_rows.append((h, any(kw in text for kw in (keywords or []))))
        family = any(f for _, f in hit_rows)
        for h, f in hit_rows[:args.show]:
            print(f"      {'*' if f else ' '} {h['score']:6.2f}  [{h['venue']}] {h['title'][:92]}")
        return family

    if args.query:
        print(f"query: {args.query}")
        show(args.query, None)
        return 0

    hits_struct = hits_mech = 0
    for name, keywords, structural, mechanism in CASES:
        print("=" * 100)
        print(f"{name}   (family keywords: {', '.join(keywords)})")
        print(f"  -- structural sentence")
        fs = show(structural, keywords)
        print(f"  -- mechanism terms: {mechanism}")
        fm = show(mechanism, keywords)
        hits_struct += fs
        hits_mech += fm
        print(f"  => family hit@{args.k}: structural {'yes' if fs else 'NO'}, mechanism {'yes' if fm else 'NO'}")
    print("=" * 100)
    print(f"family hit@{args.k}: mechanism queries {hits_mech}/{len(CASES)}, "
          f"structural sentences {hits_struct}/{len(CASES)}   (* marks a keyword hit)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
