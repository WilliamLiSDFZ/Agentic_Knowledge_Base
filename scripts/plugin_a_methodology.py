"""Plugin A: Download PDFs, extract methodology via LLM, save to methodology_kb/"""
import os, re, time, json, argparse
import urllib.request
import pymupdf4llm
from pathlib import Path

from llm import client, MODEL

REPO_ROOT = Path(__file__).resolve().parent.parent   # scripts/ -> repo root

PROMPT = """Extract techniques from this ML/NLP paper. For each technique or design choice, identify whether it had a positive, negative, or neutral effect on results.

Return JSON with a "techniques" array. Each item:
- name: short technique name
- description: what it is
- effect: "positive" | "negative" | "neutral"
- delta: quantitative change if mentioned (e.g. "+2.3 F1"), or descriptive ("outperforms baseline")
- evidence: direct quote from paper supporting the claim
- condition: when/where this applies

Paper text:
{text}

Return only valid JSON: {{"techniques": [...]}}"""


def get_pdf_url(source_url: str) -> str:
    # https://aclanthology.org/2024.naacl-long.113/ -> .pdf
    return source_url.rstrip("/") + ".pdf"


def resolve_pdf_url(source_url: str, pdf_url: str = "") -> str:
    """Best downloadable PDF URL for a paper, across venues. "" if none found.

    Priority: (1) the fetcher-captured pdf_url (nips/icml/cvpr/iccv/iclr/aaai when
    available), then (2) a source-URL convention for venues with a clean rule.
    """
    if (pdf_url or "").strip():
        return pdf_url.strip()
    if "aclanthology.org" in source_url:                    # ACL / NAACL / EMNLP
        return source_url.rstrip("/") + ".pdf"
    if "openreview.net" in source_url:                      # ICLR: forum?id=X -> pdf?id=X
        m = re.search(r"[?&]id=([^&]+)", source_url)
        if m:
            return f"https://openreview.net/pdf?id={m.group(1)}"
    return ""


def _read_frontmatter_field(content: str, field: str) -> str:
    m = re.search(rf'{field}:\s*"([^"]*)"', content)
    return m.group(1) if m else ""


def extract_abstract(content: str) -> str:
    """Pull the abstract body from a reference .md (text after '## Abstract')."""
    m = re.search(r"##\s+Abstract\s*\n(.*)$", content, flags=re.DOTALL)
    return m.group(1).strip() if m else ""


def download_pdf(url: str, dest: Path, retries: int = 3, timeout: int = 30) -> bool:
    # urlopen with an explicit timeout + UA — urlretrieve has no timeout and hangs
    # forever on a flaky/blocked connection.
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for i in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                dest.write_bytes(r.read())
            return True
        except Exception as e:
            if i < retries - 1:
                time.sleep(2 ** i)
            else:
                print(f"  Download failed {url}: {e}")
    return False


def extract_text(pdf_path: Path) -> str:
    text = pymupdf4llm.to_markdown(str(pdf_path))
    return text[:64000]


def render_methodology(title: str, source: str, techniques: list) -> str:
    lines = [f"# {title}\n", f"**Source**: {source}\n"]
    for t in techniques:
        if not t.get("name"):
            continue
        effect = t.get("effect", "neutral").upper()
        lines.append(f"## [{effect}] {t['name']}")
        lines.append(f"{t.get('description', '')}\n")
        lines.append(f"**Delta**: {t.get('delta', 'N/A')}")
        lines.append(f"**Condition**: {t.get('condition', 'N/A')}\n")
        lines.append(f"**Evidence**: \"{t.get('evidence', '')}\"\n")
    return "\n".join(lines)


def extract_methodology(text: str, retries: int = 3) -> list:
    last = None
    for i in range(retries):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": PROMPT.format(text=text)}],
                temperature=0,
            )
            raw = resp.choices[0].message.content
            raw = re.sub(r"^```json\s*|```$", "", raw.strip(), flags=re.MULTILINE)
            return json.loads(raw).get("techniques", [])
        except Exception as e:   # API error OR malformed JSON — retry with backoff
            last = e
            if i < retries - 1:
                time.sleep(2 ** i + 1)
    raise last


def process_category(category_dir: Path, output_dir: Path, abstract_fallback: bool = False):
    refs_dir = category_dir / "references"
    if not refs_dir.exists():
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    tmp = REPO_ROOT / "cache" / "plugin_a_pdfs"
    tmp.mkdir(parents=True, exist_ok=True)

    ref_files = sorted(refs_dir.glob("*.md"))
    total = len(ref_files)
    done = skipped = failed = 0

    for i, ref_file in enumerate(ref_files, 1):
        out_file = output_dir / ref_file.name.replace(".md", "_methodology.md")
        prefix = f"[{i}/{total}]"
        if out_file.exists():
            skipped += 1
            print(f"{prefix} Skip: {ref_file.name}")
            continue

        content = ref_file.read_text()
        source_url = _read_frontmatter_field(content, "source")
        pdf_url = resolve_pdf_url(source_url, _read_frontmatter_field(content, "pdf_url"))

        text = None
        if pdf_url:
            pdf_path = tmp / (ref_file.stem + ".pdf")
            print(f"{prefix} Downloading {ref_file.name}...", end=" ", flush=True)
            if download_pdf(pdf_url, pdf_path):
                print("OK", end=" ", flush=True)
                text = extract_text(pdf_path)
                pdf_path.unlink(missing_ok=True)
            else:
                print("DL FAILED", end=" ", flush=True)

        if not text and abstract_fallback:
            text = extract_abstract(content)
            if text:
                print("(abstract fallback)", end=" ", flush=True)

        if not text:
            skipped += 1
            print("Skip (no PDF)")
            continue

        try:
            techniques = extract_methodology(text)
        except Exception as e:
            failed += 1
            print(f"LLM FAILED: {e}")
            continue

        title = _read_frontmatter_field(content, "title") or ref_file.stem
        out_file.write_text(render_methodology(title, source_url, techniques))
        done += 1
        print(f"saved ({len(techniques)} techniques)")
        time.sleep(0.5)

    print(f"\nDone: {done} saved, {skipped} skipped, {failed} failed / {total} total")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--venue", required=True)
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--category", required=True, help="category folder name")
    parser.add_argument("--allow-abstract-fallback", action="store_true",
                        help="when no PDF is available, extract from the abstract (lower quality)")
    args = parser.parse_args()

    base = REPO_ROOT / "output" / f"{args.venue}-{args.year}"
    category_dir = base / args.category
    output_dir = REPO_ROOT / "methodology_kb" / f"{args.venue}-{args.year}" / args.category

    process_category(category_dir, output_dir, abstract_fallback=args.allow_abstract_fallback)
    print("Done.")
