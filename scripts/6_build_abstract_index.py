"""Build the ABSTRACT-level retrieval index (cheap: zero LLM calls).

One record per paper (title + abstract from output/{venue}-{year}/*/references/*.md),
embedded locally. This is the first stage of lazy methodology retrieval: at cold-start,
MLEvolve queries this index with a low threshold (high recall), then runs the expensive
per-paper extraction (plugin A logic) ONLY on the retrieved papers, caching results into
methodology_kb/ so later tasks reuse them.

Writes --out (default output/abstract_index/):
  - records.jsonl    one paper per line (id, venue, category, title, source, pdf_url,
                     tldr, abstract, embed_text)
  - embeddings.npy   float32 [N, dim], row-aligned
  - manifest.json    {level: "abstract", embedding_model, dim, count, built_at, schema_version}

Usage:
    python scripts/6_build_abstract_index.py --venues all
    python scripts/6_build_abstract_index.py --venues neurips-2024,acl-2024 --model BAAI/bge-m3
"""
import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MODEL = "BAAI/bge-m3"
SCHEMA_VERSION = 1


def _fm(content: str, field: str) -> str:
    m = re.search(rf'{field}:\s*"([^"]*)"', content)
    return m.group(1) if m else ""


def _abstract(content: str) -> str:
    m = re.search(r"##\s+Abstract\s*\n(.*)$", content, flags=re.DOTALL)
    return m.group(1).strip() if m else ""


def iter_paper_records(output_root: Path, venues: List[str]) -> List[Dict]:
    """One record per (venue, paper); a paper in several categories keeps the first as
    primary (used for the methodology cache path) and lists the rest."""
    seen: Dict[tuple, Dict] = {}
    for venue in venues:
        vdir = output_root / venue
        if not vdir.is_dir():
            print(f"  WARN: no output dir for {venue}, skipping")
            continue
        for cat_dir in sorted(p for p in vdir.iterdir() if p.is_dir()):
            refs = cat_dir / "references"
            if not refs.is_dir():
                continue
            for ref in sorted(refs.glob("*.md")):
                key = (venue, ref.stem)
                if key in seen:
                    seen[key]["categories"].append(cat_dir.name)
                    continue
                content = ref.read_text(encoding="utf-8", errors="replace")
                title = _fm(content, "title")
                abstract = _abstract(content)
                if not title or not abstract:
                    continue
                tldr = _fm(content, "tldr")
                seen[key] = {
                    "id": f"{venue}/{ref.stem}",
                    "venue": venue,
                    "category": cat_dir.name,          # primary (cache path)
                    "categories": [cat_dir.name],
                    "title": title,
                    "source": _fm(content, "source"),
                    "pdf_url": _fm(content, "pdf_url"),
                    "tldr": tldr,
                    "abstract": abstract[:4000],
                    "embed_text": f"{title}. {tldr} {abstract[:2000]}".strip(),
                }
    return list(seen.values())


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--venues", default="all",
                    help="'all' or comma-separated venue dirs (e.g. neurips-2024,acl-2024)")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--out", default=str(REPO_ROOT / "output" / "abstract_index"))
    args = ap.parse_args()

    output_root = REPO_ROOT / "output"
    if args.venues == "all":
        venues = sorted(d.name for d in output_root.iterdir()
                        if d.is_dir() and d.name != "abstract_index")
    else:
        venues = [v.strip() for v in args.venues.split(",") if v.strip()]

    records = iter_paper_records(output_root, venues)
    if not records:
        raise SystemExit(f"No paper records found under {output_root} for venues={venues}")
    print(f"Parsed {len(records)} papers from {len(venues)} venue(s): {venues}")

    from sentence_transformers import SentenceTransformer
    import numpy as np
    print(f"Embedding with {args.model} ...")
    model = SentenceTransformer(args.model)
    vecs = model.encode([r["embed_text"] for r in records],
                        normalize_embeddings=True, show_progress_bar=True,
                        batch_size=64)
    vecs = np.asarray(vecs, dtype="float32")

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "records.jsonl", "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    np.save(out / "embeddings.npy", vecs)
    (out / "manifest.json").write_text(json.dumps({
        "level": "abstract",
        "embedding_model": args.model,
        "dim": int(vecs.shape[1]),
        "count": len(records),
        "venues": venues,
        "built_at": datetime.now().isoformat(timespec="seconds"),
        "schema_version": SCHEMA_VERSION,
    }, indent=2), encoding="utf-8")

    with_pdf = sum(1 for r in records if r["pdf_url"] or "aclanthology.org" in r["source"]
                   or "openreview.net" in r["source"])
    print(f"\nIndex -> {out}")
    print(f"  {len(records)} papers, dim={vecs.shape[1]}, resolvable-PDF≈{with_pdf}")


if __name__ == "__main__":
    main()
