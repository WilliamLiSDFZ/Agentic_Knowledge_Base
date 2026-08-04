---
title: "Unmasking Vulnerabilities: Cardinality Sketches under Adaptive Inputs"
source: "https://proceedings.mlr.press/v235/ahmadian24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ahmadian24a/ahmadian24a.pdf"
categories: ['adversarial-robustness-and-model-security']
tags: ['cardinality-sketches', 'adaptive-inputs', 'adversarial-robustness', 'data-structures']
venue: "ICML 2024"
tldr: "Reveals vulnerabilities in cardinality sketches under adaptive queries and proposes robust alternatives."
---

# Unmasking Vulnerabilities: Cardinality Sketches under Adaptive Inputs

**Source**: [https://proceedings.mlr.press/v235/ahmadian24a.html](https://proceedings.mlr.press/v235/ahmadian24a.html)

**TLDR**: Reveals vulnerabilities in cardinality sketches under adaptive queries and proposes robust alternatives.

## Abstract

Cardinality sketches are popular data structures that enhance the efficiency of working with large data sets. The sketches are randomized representations of sets that are only of logarithmic size but can support set merges and approximate cardinality (i.e., distinct count) queries. When queries are not adaptive, that is, they do not depend on preceding query responses, the design provides strong guarantees of correctly answering a number of queries exponential in the sketch size $k$. In this work, we investigate the performance of cardinality sketches in adaptive settings and unveil inherent vulnerabilities. We design an attack against the “standard” estimators that constructs an adversarial input by post-processing responses to a set of simple non-adaptive queries of size linear in the sketch size $k$. Empirically, our attack used only $4k$ queries with the widely used HyperLogLog (HLL++) Flajolet et al., 2007; Heule et al., 2013) sketch. The simple attack technique suggests it can be effective with post-processed natural workloads. Finally and importantly, we demonstrate that the vulnerability is inherent as any estimator applied to known sketch structures can be attacked using a number of queries that is quadratic in $k$, matching a generic upper bound.