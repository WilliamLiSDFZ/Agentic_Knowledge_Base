---
title: "Individualized Privacy Accounting via Subsampling with Applications in Combinatorial Optimization"
source: "https://proceedings.mlr.press/v235/ghazi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ghazi24a/ghazi24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'submodular-optimization-and-combinatorial-algorithms']
tags: ['differential-privacy', 'subsampling', 'combinatorial-optimization']
venue: "ICML 2024"
tldr: "Introduces individualized privacy accounting via subsampling to obtain improved private combinatorial optimization algorithms."
---

# Individualized Privacy Accounting via Subsampling with Applications in Combinatorial Optimization

**Source**: [https://proceedings.mlr.press/v235/ghazi24a.html](https://proceedings.mlr.press/v235/ghazi24a.html)

**TLDR**: Introduces individualized privacy accounting via subsampling to obtain improved private combinatorial optimization algorithms.

## Abstract

In this work, we give a new technique for analyzing individualized privacy accounting via the following simple observation: if an algorithm is one-sided add-DP, then its subsampled variant satisfies two-sided DP. From this, we obtain several improved algorithms for private combinatorial optimization problems, including decomposable submodular maximization and set cover. Our error guarantees are asymptotically tight and our algorithm satisfies pure-DP while previously known algorithms (Gupta et al., 2010; Chaturvedi et al., 2021) are approximate-DP. We also show an application of our technique beyond combinatorial optimization by giving a pure-DP algorithm for the shifting heavy hitter problem in a stream; previously, only an approximate-DP algorithm was known (Kaplan et al., 2021; Cohen & Lyu, 2023).