"""Merged methodology-KB builder: plugin A (per-paper) + plugin A2 (cross-paper), concurrent.

Runs a whole venue/year in two concurrent stages, reusing the existing plugin functions:

  Stage 1 (plugin A):  per-paper methodology extraction for EVERY paper across ALL
                       categories, parallel over papers (--paper-workers).
  Stage 2 (plugin A2): cross-paper insight.md synthesis per category, parallel over
                       categories (--category-workers). Per-agent git is disabled;
                       one git commit is made at the end (avoids concurrent-commit races).
  Then optionally the retrieval index (--build-index).

Resumable: Stage 1 skips papers whose *_methodology.md exists; Stage 2 skips categories
whose insight.md exists. Safe to re-run after a crash / flaky network.

Usage:
    python scripts/5_build_methodology.py --venue naacl --year 2024
    python scripts/5_build_methodology.py --venue naacl --year 2024 \
        --paper-workers 8 --category-workers 3 --build-index

Note: plugin A currently only handles aclanthology.org PDFs, so use acl / naacl.
"""
import argparse
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # import sibling plugin modules
import plugin_a_methodology as pa          # noqa: E402
import plugin_a2_insighter as a2           # noqa: E402
from tqdm import tqdm                       # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent


# ----------------------------------------------------------------- Stage 1: plugin A

def _iter_paper_tasks(venue, year, categories):
    """Yield (category, ref_file, out_file, source_url) for papers still needing extraction."""
    out_root = REPO_ROOT / "output" / f"{venue}-{year}"
    for cat in categories:
        ref_dir = out_root / cat / "references"
        if not ref_dir.is_dir():
            continue
        out_dir = REPO_ROOT / "methodology_kb" / f"{venue}-{year}" / cat
        out_dir.mkdir(parents=True, exist_ok=True)
        for ref in sorted(ref_dir.glob("*.md")):
            out_file = out_dir / ref.name.replace(".md", "_methodology.md")
            if out_file.exists():
                continue  # resume
            content = ref.read_text(encoding="utf-8", errors="replace")
            m = re.search(r'source:\s*"([^"]+)"', content)
            if not m or "aclanthology.org" not in m.group(1):
                continue  # ACL-only (unchanged)
            yield cat, ref, out_file, m.group(1)


def _do_paper(task, tmp_dir):
    cat, ref, out_file, source_url = task
    pdf_path = tmp_dir / (ref.stem + ".pdf")
    if not pa.download_pdf(pa.get_pdf_url(source_url), pdf_path):
        return ("fail", cat, ref.name, "download")
    try:
        text = pa.extract_text(pdf_path)
        techniques = pa.extract_methodology(text)   # retries internally
    except Exception as e:
        return ("fail", cat, ref.name, f"llm:{type(e).__name__}")
    finally:
        pdf_path.unlink(missing_ok=True)            # don't accumulate GBs of PDFs
    content = ref.read_text(encoding="utf-8", errors="replace")
    tm = re.search(r'title:\s*"([^"]+)"', content)
    title = tm.group(1) if tm else ref.stem
    out_file.write_text(pa.render_methodology(title, source_url, techniques), encoding="utf-8")
    return ("done", cat, ref.name, len(techniques))


def stage_a(venue, year, categories, workers):
    tasks = list(_iter_paper_tasks(venue, year, categories))
    if not tasks:
        print("[stage A] nothing to do (all extracted, or non-ACL)")
        return
    tmp_dir = REPO_ROOT / "cache" / "plugin_a_pdfs"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    print(f"[stage A] {len(tasks)} papers to extract, {workers} workers", flush=True)
    done = fail = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(_do_paper, t, tmp_dir): t for t in tasks}
        for f in tqdm(as_completed(futs), total=len(futs), desc="Stage A (papers)"):
            try:
                status, cat, name, info = f.result()
            except Exception as e:
                fail += 1
                print(f"  ERROR: {e}")
                continue
            if status == "done":
                done += 1
            else:
                fail += 1
                print(f"  FAIL [{cat}] {name}: {info}")
    print(f"[stage A] done={done} fail={fail}", flush=True)


# ---------------------------------------------------------------- Stage 2: plugin A2

def _iter_a2_categories(venue, year, categories):
    for cat in categories:
        mkb = REPO_ROOT / "methodology_kb" / f"{venue}-{year}" / cat
        insight = REPO_ROOT / "methodology_kb" / "paperinsight" / f"{venue}-{year}" / cat / "insight.md"
        if insight.exists():
            continue  # resume
        if not mkb.is_dir() or not any(mkb.glob("*_methodology.md")):
            continue  # nothing to synthesize (e.g. all papers were non-ACL)
        yield cat, mkb, insight


def _do_a2(item, venue, year):
    cat, mkb, insight = item
    try:
        a2.run_agent(mkb, insight, venue, year, cat, allow_git=False)
        return ("done", cat, "")
    except Exception as e:
        return ("fail", cat, f"{type(e).__name__}: {e}")


def stage_a2(venue, year, categories, workers):
    items = list(_iter_a2_categories(venue, year, categories))
    if not items:
        print("[stage A2] nothing to do")
        return
    print(f"[stage A2] {len(items)} categories to synthesize, {workers} workers", flush=True)
    done = fail = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(_do_a2, it, venue, year): it for it in items}
        for f in tqdm(as_completed(futs), total=len(futs), desc="Stage A2 (categories)"):
            status, cat, info = f.result()
            if status == "done":
                done += 1
            else:
                fail += 1
                print(f"  FAIL [{cat}]: {info}")
    print(f"[stage A2] done={done} fail={fail}", flush=True)


def commit_paperinsight():
    repo = REPO_ROOT / "methodology_kb" / "paperinsight"
    if repo.is_dir():
        msg = f"build_methodology: batch update {time.strftime('%Y-%m-%d %H:%M')}"
        print("[git]", a2.git_commit(str(repo), msg))


# ----------------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--venue", required=True)
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--categories", default="all", help="'all' or comma-separated category slugs")
    ap.add_argument("--paper-workers", type=int, default=8, help="Stage A concurrency (per-paper)")
    ap.add_argument("--category-workers", type=int, default=3, help="Stage A2 concurrency (per-category)")
    ap.add_argument("--skip-a", action="store_true", help="skip Stage A (per-paper extraction)")
    ap.add_argument("--skip-a2", action="store_true", help="skip Stage A2 (cross-paper synthesis)")
    ap.add_argument("--build-index", action="store_true", help="build the retrieval index at the end")
    args = ap.parse_args()

    out_root = REPO_ROOT / "output" / f"{args.venue}-{args.year}"
    if not out_root.is_dir():
        sys.exit(f"No {out_root} — run: bash run_all.sh {args.venue} {args.year} first")

    if args.categories == "all":
        categories = sorted(d.name for d in out_root.iterdir() if d.is_dir())
    else:
        categories = [c.strip() for c in args.categories.split(",") if c.strip()]
    print(f"Venue {args.venue}-{args.year}: {len(categories)} categories", flush=True)

    if not args.skip_a:
        stage_a(args.venue, args.year, categories, args.paper_workers)
    if not args.skip_a2:
        stage_a2(args.venue, args.year, categories, args.category_workers)
        commit_paperinsight()

    if args.build_index:
        print("[index] building retrieval index over methodology_kb/paperinsight", flush=True)
        subprocess.run([sys.executable, str(REPO_ROOT / "scripts" / "build_retrieval_index.py"),
                        "--kb", "methodology_kb/paperinsight"], check=False)

    print("All done.")


if __name__ == "__main__":
    main()
