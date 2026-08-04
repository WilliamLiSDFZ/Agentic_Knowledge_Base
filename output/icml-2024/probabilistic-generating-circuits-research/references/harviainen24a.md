---
title: "Estimating the Permanent by Nesting Importance Sampling"
source: "https://proceedings.mlr.press/v235/harviainen24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/harviainen24a/harviainen24a.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'probabilistic-generating-circuits-research']
tags: ['importance-sampling', 'permanent-estimation', 'sequential-monte-carlo']
venue: "ICML 2024"
tldr: "A nested importance sampling approach is proposed for efficiently estimating the permanent of nonnegative matrices."
---

# Estimating the Permanent by Nesting Importance Sampling

**Source**: [https://proceedings.mlr.press/v235/harviainen24a.html](https://proceedings.mlr.press/v235/harviainen24a.html)

**TLDR**: A nested importance sampling approach is proposed for efficiently estimating the permanent of nonnegative matrices.

## Abstract

Sequential importance sampling (SIS) is one of the prominent methods for estimating high-dimensional integrals. For example, it is empirically the most efficient method known for estimating the permanent of nonnegative matrices, a notorious problem with numerous applications in computer science, statistics, and other fields. Unfortunately, SIS typically fails to provide accuracy guarantees due to difficulties in bounding the variance of the importance weights; for estimating the permanent with accuracy guarantees, the most efficient practical methods known are based on rejection sampling. Taking the best of both worlds, we give a variant of SIS, in which sampling is proportional to the upper bound used in rejection sampling. We show that this method is provably more efficient than its rejection sampling counterpart, particularly in high accuracy regimes. On estimating the permanent, we empirically obtain up to two orders-of-magnitude speedups over a state-of-the-art rejection sampling method.