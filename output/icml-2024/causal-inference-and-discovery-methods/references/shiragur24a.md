---
title: "Causal Discovery with Fewer Conditional Independence Tests"
source: "https://proceedings.mlr.press/v235/shiragur24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shiragur24a/shiragur24a.pdf"
categories: ['causal-inference-and-discovery-methods']
tags: ['causal-discovery', 'conditional-independence-tests', 'PC-algorithm']
venue: "ICML 2024"
tldr: "Presents a causal discovery algorithm that requires fewer conditional independence tests than classical approaches like the PC algorithm."
---

# Causal Discovery with Fewer Conditional Independence Tests

**Source**: [https://proceedings.mlr.press/v235/shiragur24a.html](https://proceedings.mlr.press/v235/shiragur24a.html)

**TLDR**: Presents a causal discovery algorithm that requires fewer conditional independence tests than classical approaches like the PC algorithm.

## Abstract

Many questions in science center around the fundamental problem of understanding causal relationships. However, most constraint-based causal discovery algorithms, including the well-celebrated PC algorithm, often incur an exponential number of conditional independence (CI) tests, posing limitations in various applications. Addressing this, our work focuses on characterizing what can be learned about the underlying causal graph with a reduced number of CI tests. We show that it is possible to a learn a coarser representation of the hidden causal graph with a polynomial number of tests. This coarser representation, named Causal Consistent Partition Graph (CCPG), comprises of a partition of the vertices and a directed graph defined over its components. CCPG satisfies consistency of orientations and additional constraints which favor finer partitions. Furthermore, it reduces to the underlying causal graph when the causal graph is identifiable. As a consequence, our results offer the first efficient algorithm for recovering the true causal graph with a polynomial number of tests, in special cases where the causal graph is fully identifiable through observational data and potentially additional interventions.