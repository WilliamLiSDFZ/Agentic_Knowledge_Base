"""Build the PAPER CORPUS that MLEvolve's analogy agent searches with BM25 (zero LLM, zero GPU).

One record per paper (title + tldr + abstract from output/{venue}-{year}/*/references/*.md).
There is deliberately no preprocessing beyond parsing the reference files: no embeddings, no
technique extraction, no clustering. The consumer (MLEvolve `engine/analogy/corpus.py`)
tokenizes and builds BM25 at load time, so this script only has to be re-run when `output/`
changes.

Writes --out (default output/paper_corpus/):
  - records.jsonl    one paper per line (id, venue, category, categories, title, source,
                     pdf_url, tldr, abstract)
  - manifest.json    {level: "paper", count, venues: {venue: n}, records_sha1, built_at,
                     schema_version}

`records_sha1` is the identity of the corpus: MLEvolve copies it into each run's
`logs/kb_snapshot.json`, so "did these two runs search the same papers?" is one comparison.

Usage:
    python scripts/6_build_paper_corpus.py                       # all venues under output/
    python scripts/6_build_paper_corpus.py --venues neurips-2024,acl-2024
"""
import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Dict, List

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_VERSION = 2


def _fm(content: str, field: str) -> str:
    m = re.search(rf'{field}:\s*"([^"]*)"', content)
    return m.group(1) if m else ""


def _abstract(content: str) -> str:
    m = re.search(r"##\s+Abstract\s*\n(.*)$", content, flags=re.DOTALL)
    return m.group(1).strip() if m else ""


def iter_paper_records(output_root: Path, venues: List[str]) -> List[Dict]:
    """One record per (venue, paper); a paper in several categories keeps the first as
    primary and lists the rest."""
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
                seen[key] = {
                    "id": f"{venue}/{ref.stem}",
                    "venue": venue,
                    "category": cat_dir.name,
                    "categories": [cat_dir.name],
                    "title": title,
                    "source": _fm(content, "source"),
                    "pdf_url": _fm(content, "pdf_url"),
                    "tldr": _fm(content, "tldr"),
                    "abstract": abstract[:4000],
                }
    return list(seen.values())


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--venues", default="all",
                    help="'all' or comma-separated venue dirs (e.g. neurips-2024,acl-2024)")
    ap.add_argument("--out", default=str(REPO_ROOT / "output" / "paper_corpus"))
    args = ap.parse_args()

    output_root = REPO_ROOT / "output"
    if args.venues == "all":
        venues = sorted(d.name for d in output_root.iterdir()
                        if d.is_dir() and d.name not in ("abstract_index", "paper_corpus"))
    else:
        venues = [v.strip() for v in args.venues.split(",") if v.strip()]

    records = iter_paper_records(output_root, venues)
    if not records:
        raise SystemExit(f"No paper records found under {output_root} for venues={venues}")
    print(f"Parsed {len(records)} papers from {len(venues)} venue(s): {venues}")

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    sha = hashlib.sha1()
    with open(out / "records.jsonl", "w", encoding="utf-8") as f:
        for r in records:
            line = json.dumps(r, ensure_ascii=False) + "\n"
            f.write(line)
            sha.update(line.encode("utf-8"))
    venue_counts = Counter(r["venue"] for r in records)
    (out / "manifest.json").write_text(json.dumps({
        "level": "paper",
        "count": len(records),
        "venues": dict(sorted(venue_counts.items())),
        "records_sha1": sha.hexdigest()[:12],
        "built_at": datetime.now().isoformat(timespec="seconds"),
        "schema_version": SCHEMA_VERSION,
    }, indent=2), encoding="utf-8")

    print(f"\nCorpus -> {out}")
    print(f"  {len(records)} papers, sha1 {sha.hexdigest()[:12]}")
    for v, n in sorted(venue_counts.items()):
        print(f"  {v:<16}{n:>7}")


if __name__ == "__main__":
    main()
