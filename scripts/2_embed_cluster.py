"""
Embed abstracts, hierarchical cluster, then use LLM to name each cluster.
Saves to cache/clusters.json

Tune: N_CLUSTERS (bigger = finer granularity)
"""
import json
import os
import time

# Fail fast instead of hanging forever when HuggingFace is unreachable/blocked, and
# surface download progress. MUST be set BEFORE importing sentence_transformers.
os.environ.setdefault("HF_HUB_ETAG_TIMEOUT", "10")      # metadata/HEAD request timeout (s)
os.environ.setdefault("HF_HUB_DOWNLOAD_TIMEOUT", "30")  # per-download request timeout (s)
os.environ.setdefault("HF_HUB_VERBOSITY", "info")

import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

from llm import client, MODEL

CACHE_DIR = os.path.join(os.path.dirname(__file__), "../cache")

N_CLUSTERS = 80  # <-- adjust for granularity


def embed_abstracts(papers):
    endpoint = os.environ.get("HF_ENDPOINT", "https://huggingface.co (default)")
    print(f"[step2] loading model 'all-MiniLM-L6-v2' from {endpoint} "
          f"(first run downloads ~80MB) ...", flush=True)
    t0 = time.time()
    model = SentenceTransformer("all-MiniLM-L6-v2")
    print(f"[step2] model ready in {time.time() - t0:.1f}s; embedding {len(papers)} papers ...", flush=True)
    texts = [f"{p['title']}. {p['abstract']}" for p in papers]
    t1 = time.time()
    embeddings = model.encode(texts, show_progress_bar=True, batch_size=64)
    print(f"[step2] embedded {len(texts)} papers in {time.time() - t1:.1f}s", flush=True)
    return embeddings


def cluster(embeddings):
    print(f"[step2] clustering {len(embeddings)} papers into {N_CLUSTERS} topics ...", flush=True)
    t0 = time.time()
    clustering = AgglomerativeClustering(n_clusters=N_CLUSTERS, metric="cosine", linkage="average")
    labels = clustering.fit_predict(embeddings)
    print(f"[step2] clustered in {time.time() - t0:.1f}s; naming clusters via LLM ...", flush=True)
    return labels


def name_cluster(client, titles):
    sample = "\n".join(f"- {t}" for t in titles[:20])
    resp = client.chat.completions.create(
        model=MODEL,
        max_tokens=64,
        messages=[{"role": "user", "content": (
            "Given these paper titles from the same research cluster, "
            "give a concise category name (3-7 words, lowercase, hyphen-separated):\n"
            f"{sample}\n\nCategory name:"
        )}]
    )
    return resp.choices[0].message.content.strip().strip('"`').lower().replace(" ", "-")


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--venue", default="neurips")
    parser.add_argument("--year", type=int, default=2024)
    args = parser.parse_args()

    papers_path = os.path.join(CACHE_DIR, f"{args.venue}_{args.year}_papers.json")
    clusters_path = os.path.join(CACHE_DIR, f"{args.venue}_{args.year}_clusters.json")

    with open(papers_path) as f:
        papers = json.load(f)

    print(f"Loaded {len(papers)} papers")
    print(f"[step2] HF_ENDPOINT={os.environ.get('HF_ENDPOINT', '(unset — using huggingface.co)')}", flush=True)
    embeddings = embed_abstracts(papers)
    labels = cluster(embeddings)

    clusters = {}
    for i, (paper, label) in enumerate(zip(papers, labels)):
        clusters.setdefault(label, []).append(i)

    named = {}
    for label, indices in tqdm(clusters.items(), desc="Naming clusters"):
        titles = [papers[i]["title"] for i in indices]
        name = name_cluster(client, titles)
        if name in named:
            # Two distinct clusters were given the same LLM-generated name.
            # Merge their papers instead of overwriting (overwriting silently
            # dropped every paper from the first cluster).
            print(f"  Name collision on '{name}': merging {len(indices)} papers into existing cluster")
            named[name].extend(indices)
        else:
            named[name] = indices

    with open(clusters_path, "w") as f:
        json.dump({"clusters": named, "paper_count": len(papers)}, f, indent=2)

    print(f"Saved {len(named)} clusters -> {clusters_path}")


if __name__ == "__main__":
    main()
