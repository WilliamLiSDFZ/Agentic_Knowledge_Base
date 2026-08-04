---
title: "Individual Fairness in Graph Decomposition"
source: "https://proceedings.mlr.press/v235/munagala24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/munagala24a/munagala24a.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'graph-clustering-and-matching-algorithms']
tags: ['individual-fairness', 'graph-decomposition', 'low-diameter-clustering', 'planar-graphs']
venue: "ICML 2024"
tldr: "Individual fairness constraints are incorporated into randomized low-diameter graph decomposition procedures for planar graphs, ensuring nearby nodes are treated equitably."
---

# Individual Fairness in Graph Decomposition

**Source**: [https://proceedings.mlr.press/v235/munagala24a.html](https://proceedings.mlr.press/v235/munagala24a.html)

**TLDR**: Individual fairness constraints are incorporated into randomized low-diameter graph decomposition procedures for planar graphs, ensuring nearby nodes are treated equitably.

## Abstract

In this paper, we consider classic randomized low diameter decomposition procedures for planar graphs that obtain connected clusters that are cohesive in that close by pairs of nodes are assigned to the same cluster with high probability. We consider the additional aspect of individual fairness – pairs of nodes at comparable distances should be separated with comparable probability. We show that classic decomposition procedures do not satisfy this property. We present novel algorithms that achieve various trade-offs between this property and additional desiderata of connectivity of the clusters and optimality in number of clusters. We show that our individual fairness bounds may be difficult to improve by tying the improvement to resolving a major open question in metric embeddings. We finally show the efficacy of our algorithms on real planar networks modeling Congressional redistricting.