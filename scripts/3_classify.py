"""
Re-classify each paper using the LLM against the auto-generated cluster names.

Batches are classified concurrently (thread pool, --workers). Paper order is
preserved (results are filled by global index, not append-on-completion), and the
run is resumable via a sparse checkpoint in cache/. The final, in-order result is
written to cache/{venue}_{year}_classified.json (what step 4 consumes).
"""
import argparse
import concurrent.futures as cf
import json
import os
import random
import re
import time
from tqdm import tqdm

from llm import client, MODEL

CACHE_DIR = os.path.join(os.path.dirname(__file__), "../cache")

DEFAULT_BATCH_SIZE = 30
DEFAULT_WORKERS = 8


def llm(prompt, max_tokens=512, attempts=4):
    for attempt in range(attempts):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": prompt}],
            )
            return resp.choices[0].message.content
        except Exception:
            if attempt == attempts - 1:
                raise
            # exponential backoff + jitter; matters when many threads hit rate limits
            time.sleep(min(2 ** attempt + random.uniform(0, 1.5), 30))


def _parse_line(body, categories):
    cats, tags, tldr = [], [], ""
    for part in body.split("|"):
        part = part.strip()
        if part.startswith("CATS:"):
            for token in part[5:].split(","):
                try:
                    cidx = int(token.strip()) - 1
                    if 0 <= cidx < len(categories):
                        cats.append(categories[cidx])
                except ValueError:
                    pass
        elif part.startswith("TAGS:"):
            tags = [t.strip() for t in part[5:].split(",") if t.strip()]
        elif part.startswith("TLDR:"):
            tldr = part[5:].strip()
    return {"categories": cats or [categories[0]], "tags": tags, "tldr": tldr}


def classify_batch(papers, categories):
    cat_list = "\n".join(f"{i+1}. {c}" for i, c in enumerate(categories))
    entries = "\n\n".join(
        f"[{i+1}] {p['title']}\n{p['abstract'][:300]}"
        for i, p in enumerate(papers)
    )
    text = llm(
        f"Categories:\n{cat_list}\n\n"
        f"For each paper, output exactly one line, prefixed with the paper's number "
        f"in square brackets, in this format:\n"
        f"[1] CATS:1,3 | TAGS:tag1,tag2,tag3 | TLDR:one sentence summary\n\n"
        f"Emit one line per paper for all {len(papers)} papers, and keep each [n] "
        f"index matching the paper it describes.\n\n"
        f"{entries}",
        # Scale output budget with batch size so the last papers in the batch are not
        # truncated away (the previous fixed 1024 silently dropped batch tails).
        max_tokens=max(1024, 110 * len(papers)),
    )

    # Match each output line back to its paper by the explicit [n] index, so a
    # missing/extra/reordered line cannot shift any other paper's labels. Papers with
    # no matching line are flagged `unparsed`; the caller aggregates and reports them.
    parsed = {}
    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        m = re.match(r"\[(\d+)\]\s*(.*)", line)
        if not m:
            continue
        idx = int(m.group(1)) - 1
        if 0 <= idx < len(papers):
            parsed[idx] = _parse_line(m.group(2), categories)

    results = []
    for i in range(len(papers)):
        if i in parsed:
            results.append(parsed[i])
        else:
            results.append({"categories": [categories[0]], "tags": [], "tldr": "", "unparsed": True})
    return results


def _flush(ckpt_path, results):
    """Atomically write the (possibly still-sparse) results array to the checkpoint."""
    tmp = ckpt_path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(results, f)
    os.replace(tmp, ckpt_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--venue", default="neurips")
    parser.add_argument("--year", type=int, default=2024)
    parser.add_argument("--workers", type=int, default=DEFAULT_WORKERS,
                        help="concurrent API calls (raise carefully; watch rate limits)")
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE,
                        help="papers classified per LLM call")
    args = parser.parse_args()

    papers_path = os.path.join(CACHE_DIR, f"{args.venue}_{args.year}_papers.json")
    clusters_path = os.path.join(CACHE_DIR, f"{args.venue}_{args.year}_clusters.json")
    output_path = os.path.join(CACHE_DIR, f"{args.venue}_{args.year}_classified.json")
    ckpt_path = os.path.join(CACHE_DIR, f"{args.venue}_{args.year}_classify_ckpt.json")

    with open(papers_path) as f:
        papers = json.load(f)
    with open(clusters_path) as f:
        clusters_data = json.load(f)
    categories = list(clusters_data["clusters"].keys())

    # Resume from the checkpoint if it exists and is shaped to this corpus.
    results = [None] * len(papers)
    if os.path.exists(ckpt_path):
        try:
            saved = json.load(open(ckpt_path))
            if isinstance(saved, list) and len(saved) == len(papers):
                results = saved
                print(f"Resuming: {sum(r is not None for r in results)}/{len(papers)} already done")
            else:
                print("Checkpoint shape doesn't match corpus; starting fresh")
        except Exception as e:
            print(f"Ignoring unreadable checkpoint ({e})")

    pending = [i for i in range(len(papers)) if results[i] is None]
    batch_size = max(1, args.batch_size)
    batches = [pending[k:k + batch_size] for k in range(0, len(pending), batch_size)]

    if batches:
        print(f"Classifying {len(pending)} papers in {len(batches)} batches "
              f"({args.workers} workers, batch_size={batch_size})")
        done = 0
        with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
            fut2idx = {
                ex.submit(classify_batch, [papers[i] for i in b], categories): b
                for b in batches
            }
            try:
                for fut in tqdm(cf.as_completed(fut2idx), total=len(batches), desc="Classifying"):
                    gidx = fut2idx[fut]
                    try:
                        batch_results = fut.result()
                    except Exception as e:
                        # One batch failing every retry must not kill the pool; its
                        # papers stay None and get picked up on the next run.
                        print(f"  batch @paper {gidx[0]+1} failed after retries: {e}; left for re-run")
                        continue
                    for k, gi in enumerate(gidx):
                        results[gi] = batch_results[k]
                    done += 1
                    if done % 10 == 0:
                        _flush(ckpt_path, results)
            finally:
                _flush(ckpt_path, results)

    # Assemble the final output in paper order. Any slot still None (a batch that
    # failed every retry) is written with the default category and flagged so a
    # re-run can fill it.
    classified = []
    missing, unparsed = [], []
    for i, p in enumerate(papers):
        r = results[i]
        if r is None:
            missing.append(i + 1)
            r = {"categories": [categories[0]], "tags": [], "tldr": "", "unparsed": True}
        elif r.get("unparsed"):
            unparsed.append(i + 1)
        classified.append({**p, **r})

    with open(output_path, "w") as f:
        json.dump(classified, f, indent=2)

    def _preview(xs):
        return xs if len(xs) <= 40 else xs[:40] + ["..."]

    print(f"Classified {len(classified)} papers into {len(categories)} categories -> {output_path}")
    if unparsed:
        print(f"  {len(unparsed)} papers had no parseable line; defaulted to "
              f"'{categories[0]}'. Positions: {_preview(unparsed)}")
    if missing:
        print(f"  {len(missing)} papers are in failed batches and still need a re-run: "
              f"{_preview(missing)}")
    else:
        print("  All batches completed (checkpoint kept; re-running is a cheap no-op).")


if __name__ == "__main__":
    main()
