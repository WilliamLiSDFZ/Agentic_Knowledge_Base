"""Generate Skill files from classified papers."""
import json
import os
import re
import argparse
from tqdm import tqdm

from llm import client, MODEL

CACHE_DIR = os.path.join(os.path.dirname(__file__), "../cache")


def slugify(text):
    s = re.sub(r"[^a-z0-9-]", "", str(text).lower().replace(" ", "-"))
    return s or "untitled"


def generate_description(category, papers):
    titles = "\n".join(f"- {p['title']}" for p in papers[:15])
    resp = client.chat.completions.create(
        model=MODEL,
        max_tokens=80,
        messages=[{"role": "user", "content": (
            f"Given these paper titles from the '{category}' research area, "
            f"write a 1-2 sentence description of what this skill covers. "
            f"Be specific about methods, tasks, and applications. No fluff:\n{titles}"
        )}]
    )
    return resp.choices[0].message.content.strip()


def make_reference(paper):
    url = paper.get("url") or paper.get("forum", "")
    categories = paper.get("categories") or [paper.get("category", "")]
    tags = paper.get("tags", [])
    tldr = paper.get("tldr", "")
    venue = paper.get("venue", "")
    year = paper.get("year", "")
    title = paper.get("title", "Untitled")
    abstract = paper.get("abstract", "")

    return f"""---
title: "{title.replace('"', "'")}"
source: "{url}"
categories: {categories}
tags: {tags}
venue: "{venue} {year}"
tldr: "{tldr}"
---

# {title}

**Source**: [{url}]({url})

**TLDR**: {tldr}

## Abstract

{abstract}"""


def make_skill_md(category, papers, description, fnames):
    rows = "\n".join(
        f"| {i + 1} | {p.get('title', '')[:60]} | {', '.join(p.get('tags', [])[:3])} | {fname}.md |"
        for i, (p, fname) in enumerate(zip(papers, fnames))
    )
    return f"""---
name: {category}
description: >-
  {description}
---

# {category.replace("-", " ").title()}

{description}

## Entry Index

| # | Title | Tags | File |
|---|-------|------|------|
{rows}
"""


def generate(classified_path, output_root):
    with open(classified_path) as f:
        papers = json.load(f)

    by_category = {}
    for p in papers:
        for cat in p.get("categories", [p.get("category", "uncategorized")]):
            by_category.setdefault(cat, []).append(p)

    for category, cat_papers in tqdm(by_category.items(), desc="Generating skills"):
        cat_slug = slugify(category)
        cat_dir = os.path.join(output_root, cat_slug)
        ref_dir = os.path.join(cat_dir, "references")
        os.makedirs(ref_dir, exist_ok=True)

        # Assign a unique reference filename per paper within this category, so two
        # papers whose ids slugify to the same string no longer overwrite each other
        # (and the SKILL.md index row points at the matching unique file).
        used_names, fnames = set(), []
        for p in cat_papers:
            base = slugify(p.get("id") or p.get("title", "untitled"))
            fname, n = base, 1
            while fname in used_names:
                fname = f"{base}-{n}"
                n += 1
            used_names.add(fname)
            fnames.append(fname)

        description = generate_description(category, cat_papers)
        with open(os.path.join(cat_dir, "SKILL.md"), "w") as f:
            f.write(make_skill_md(category, cat_papers, description, fnames))

        for paper, fname in zip(cat_papers, fnames):
            with open(os.path.join(ref_dir, fname + ".md"), "w") as f:
                f.write(make_reference(paper))

    print(f"Generated {len(by_category)} skills in {output_root}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--venue", default="neurips")
    parser.add_argument("--year", type=int, default=2024)
    args = parser.parse_args()

    classified_path = os.path.join(CACHE_DIR, f"{args.venue}_{args.year}_classified.json")
    output_root = os.path.join(os.path.dirname(__file__), "../output", f"{args.venue}-{args.year}")
    generate(classified_path, output_root)
