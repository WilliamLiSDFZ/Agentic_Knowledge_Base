---
title: "Novel Spectral Algorithms for the Partial Credit Model"
source: "https://proceedings.mlr.press/v235/nguyen24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nguyen24k/nguyen24k.pdf"
categories: ['matrix-geometry-optimization-for-spectral-learning', 'sampling-compression-and-dimensionality-reduction']
tags: ['partial-credit-model', 'spectral-algorithms', 'psychometrics']
venue: "ICML 2024"
tldr: "Presents novel spectral algorithms for parameter estimation in the Partial Credit Model used in psychometrics."
---

# Novel Spectral Algorithms for the Partial Credit Model

**Source**: [https://proceedings.mlr.press/v235/nguyen24k.html](https://proceedings.mlr.press/v235/nguyen24k.html)

**TLDR**: Presents novel spectral algorithms for parameter estimation in the Partial Credit Model used in psychometrics.

## Abstract

The Partial Credit Model (PCM) of Andrich (1978) and Masters (1982) is a fundamental model within the psychometric literature with wide-ranging modern applications. It models the integer-valued response that a subject gives to an item where there is a natural notion of monotonic progress between consecutive response values, such as partial scores on a test and customer ratings of a product. In this paper, we introduce a novel, time-efficient and accurate statistical spectral algorithm for inference under the PCM model. We complement our algorithmic contribution with in-depth non-asymptotic statistical analysis, the first of its kind in the literature. We show that the spectral algorithm enjoys the optimal error guarantee under three different metrics, all under reasonable sampling assumptions. We leverage the efficiency of the spectral algorithm to propose a novel EM-based algorithm for learning mixtures of PCMs. We perform comprehensive experiments on synthetic and real-life datasets covering education testing, recommendation systems, and financial investment applications. We show that the proposed spectral algorithm is competitive with previously introduced algorithms in terms of accuracy while being orders of magnitude faster.