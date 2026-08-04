---
title: "GATE: How to Keep Out Intrusive Neighbors"
source: "https://proceedings.mlr.press/v235/mustafa24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mustafa24a/mustafa24a.pdf"
categories: ['graph-neural-networks-and-topology']
tags: ['graph-attention-networks', 'neighborhood-aggregation', 'over-smoothing']
venue: "ICML 2024"
tldr: "GATs are analytically and empirically shown to fail at suppressing task-irrelevant neighbor aggregation, revealing a fundamental limitation in their design."
---

# GATE: How to Keep Out Intrusive Neighbors

**Source**: [https://proceedings.mlr.press/v235/mustafa24a.html](https://proceedings.mlr.press/v235/mustafa24a.html)

**TLDR**: GATs are analytically and empirically shown to fail at suppressing task-irrelevant neighbor aggregation, revealing a fundamental limitation in their design.

## Abstract

Graph Attention Networks (GATs) are designed to provide flexible neighborhood aggregation that assigns weights to neighbors according to their importance. In practice, however, GATs are often unable to switch off task-irrelevant neighborhood aggregation, as we show experimentally and analytically. To address this challenge, we propose GATE, a GAT extension that holds three major advantages: i) It alleviates over-smoothing by addressing its root cause of unnecessary neighborhood aggregation. ii) Similarly to perceptrons, it benefits from higher depth as it can still utilize additional layers for (non-)linear feature transformations in case of (nearly) switched-off neighborhood aggregation. iii) By down-weighting connections to unrelated neighbors, it often outperforms GATs on real-world heterophilic datasets. To further validate our claims, we construct a synthetic test bed to analyze a model’s ability to utilize the appropriate amount of neighborhood aggregation, which could be of independent interest.