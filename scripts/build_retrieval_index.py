"""Build a portable semantic-retrieval index over a knowledge base.

Indexes one record per cross-paper insight (an `insight.md` table row -> its
`references/{slug}.md`), i.e. one distilled technique + its actionable guidance.

Supports both KB layouts:
  - Flat:   {kb}/category/insight.md            (e.g. experience_kb/)
  - Nested: {kb}/venue-year/category/insight.md (e.g. methodology_kb/paperinsight/)

Writes {kb}/index/:
  - records.jsonl    one record per line (no vectors)
  - embeddings.npy   float32 [N, dim], row-aligned to records.jsonl
  - manifest.json    {embedding_model, dim, count, built_at, kb_content_hash, schema_version}

The consumer (MLEvolve engine/coldstart/methodology_agent.py) reads the manifest to
instantiate the SAME embedding model, then builds its FAISS index from embeddings.npy.
Build and query MUST use the same model — the manifest is the contract.

Usage:
    python scripts/build_retrieval_index.py --kb experience_kb
    python scripts/build_retrieval_index.py --kb methodology_kb/paperinsight --model BAAI/bge-m3
"""
import argparse
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Iterator, List, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent

# bge-m3 is multilingual: the experience_kb insights are partly Chinese while task
# descriptions are English, so cross-lingual matching matters. Use an English-only
# model (e.g. BAAI/bge-base-en-v1.5) only for an English-only KB.
DEFAULT_MODEL = "BAAI/bge-m3"
SCHEMA_VERSION = 1


# ---------------------------------------------------------------- KB traversal

def scan_categories(kb_base: Path) -> List[str]:
    """Return category paths relative to kb_base (flat and nested layouts)."""
    categories: List[str] = []
    for entry in sorted(kb_base.iterdir()):
        if not entry.is_dir() or entry.name.startswith("."):
            continue
        if (entry / "insight.md").exists():
            categories.append(entry.name)
            continue
        for sub in sorted(entry.iterdir()):
            if not sub.is_dir() or sub.name.startswith("."):
                continue
            if (sub / "insight.md").exists():
                categories.append(f"{entry.name}/{sub.name}")
    return categories


def parse_insight_table(insight_md: Path) -> List[dict]:
    """Parse rows of `| # | Insight | Papers-or-Evidence | Confidence | File |`.

    Both KB flavours share the column positions: title=1, papers/evidence=2,
    confidence=3, file=4.
    """
    rows = []
    in_table = False
    for line in insight_md.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if line.startswith("| # |") or line.startswith("|---|"):
            in_table = True
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            break
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 5 or not re.fullmatch(r"\d+", cells[0]):
            continue
        rows.append({
            "num": int(cells[0]),
            "title": cells[1],
            "papers": [p.strip() for p in re.split(r"[,;]", cells[2]) if p.strip()],
            "confidence": cells[3].upper(),
            "file": cells[4],
        })
    return rows


def resolve_reference(cat_dir: Path, row: dict) -> Optional[Path]:
    """Resolve a table row's File cell to an actual reference file (with fuzzy fallback)."""
    refs_dir = cat_dir / "references"
    if not refs_dir.is_dir():
        return None
    ref_path = refs_dir / row["file"].rsplit("/", 1)[-1]
    if ref_path.exists():
        return ref_path
    slug = re.sub(r"[^a-z0-9-]", "", row["title"].lower().replace(" ", "-"))[:30]
    if len(slug) >= 15:
        candidates = [p for p in sorted(refs_dir.glob("*.md")) if slug[:15] in p.stem]
        if candidates:
            return candidates[0]
    return None


# ---------------------------------------------------------------- text shaping

def strip_ref_noise(text: str) -> str:
    """Drop frontmatter, `Papers & Evidence`, and Delta lines — mirrors the consumer."""
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    text = re.sub(r"## Papers & Evidence.*?(?=\n## |\Z)", "", text, flags=re.DOTALL)
    text = re.sub(r"\*\*Delta\*\*:.*?\n", "", text)
    return text.strip()


def _section(body: str, header: str) -> str:
    m = re.search(rf"^##\s+{re.escape(header)}\s*$\n(.*?)(?=^##\s|\Z)", body,
                  re.MULTILINE | re.DOTALL)
    return m.group(1).strip() if m else ""


def build_embed_text(title: str, body: str) -> str:
    """What we embed: the 'what/when' of the technique, not the whole paper dump."""
    parts = [title]
    guidance = _section(body, "Actionable Guidance")
    if guidance:
        parts.append(guidance)
    m = re.search(r"\*\*Condition\*\*:\s*(.+)", body)
    if m:
        parts.append(f"Condition: {m.group(1).strip()}")
    if not guidance:
        # Fallback for references without an Actionable Guidance section.
        parts.append(strip_ref_noise(body)[:800])
    return "\n".join(parts)


# ---------------------------------------------------------------- record build

def iter_records(kb_base: Path, source: str) -> Iterator[dict]:
    for cat_path in scan_categories(kb_base):
        cat_dir = kb_base / cat_path
        category = cat_dir.name
        venue = cat_path.split("/")[0] if "/" in cat_path else ""
        for row in parse_insight_table(cat_dir / "insight.md"):
            ref = resolve_reference(cat_dir, row)
            if ref is None:
                continue
            body = ref.read_text(encoding="utf-8", errors="replace")
            yield {
                "id": f"{cat_path}/{ref.stem}",
                "venue": venue,
                "category": category,
                "title": row["title"],
                "confidence": row["confidence"],
                "papers": row["papers"],
                "source": source,
                "embed_text": build_embed_text(row["title"], body),
                "guidance_text": strip_ref_noise(body),
            }


def hash_kb(kb_base: Path) -> str:
    h = hashlib.sha256()
    for p in sorted(kb_base.rglob("*.md")):
        if "/index/" in str(p):
            continue
        h.update(p.name.encode())
        h.update(p.read_bytes())
    return h.hexdigest()[:16]


# ---------------------------------------------------------------- entrypoint

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kb", required=True,
                    help="KB root to index, e.g. experience_kb or methodology_kb/paperinsight")
    ap.add_argument("--model", default=DEFAULT_MODEL, help=f"embedding model (default {DEFAULT_MODEL})")
    ap.add_argument("--out", default=None, help="index dir (default {kb}/index)")
    args = ap.parse_args()

    kb_base = Path(args.kb)
    if not kb_base.is_absolute():
        kb_base = (REPO_ROOT / kb_base).resolve()
    if not kb_base.is_dir():
        raise SystemExit(f"KB not found: {kb_base}")

    out = Path(args.out) if args.out else kb_base / "index"

    records = list(iter_records(kb_base, source=kb_base.name))
    if not records:
        raise SystemExit(f"No insight records found under {kb_base} "
                         f"(expected category dirs with insight.md + references/)")
    print(f"Parsed {len(records)} insight records from {kb_base}")

    from sentence_transformers import SentenceTransformer
    print(f"Embedding with {args.model} ...")
    model = SentenceTransformer(args.model)
    vecs = model.encode([r["embed_text"] for r in records],
                        normalize_embeddings=True,
                        show_progress_bar=True,
                        batch_size=32)
    import numpy as np
    vecs = np.asarray(vecs, dtype="float32")

    out.mkdir(parents=True, exist_ok=True)
    with open(out / "records.jsonl", "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    np.save(out / "embeddings.npy", vecs)
    manifest = {
        "embedding_model": args.model,
        "dim": int(vecs.shape[1]),
        "count": len(records),
        "built_at": datetime.now().isoformat(timespec="seconds"),
        "kb_content_hash": hash_kb(kb_base),
        "schema_version": SCHEMA_VERSION,
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    by_conf = {}
    for r in records:
        by_conf[r["confidence"]] = by_conf.get(r["confidence"], 0) + 1
    print(f"\nIndex -> {out}")
    print(f"  {len(records)} records, dim={manifest['dim']}, confidence={by_conf}")


if __name__ == "__main__":
    main()
