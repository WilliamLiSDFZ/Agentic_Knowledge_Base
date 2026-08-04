---
title: "Shifted Interpolation for Differential Privacy"
source: "https://proceedings.mlr.press/v235/bok24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bok24a/bok24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'optimization-algorithms-convergence-theory']
tags: ['differential-privacy', 'noisy-gradient-descent', 'privacy-leakage', 'shifted-interpolation']
venue: "ICML 2024"
tldr: "This paper introduces shifted interpolation to tighten privacy analysis of noisy gradient descent for differentially private machine learning with convex losses."
---

# Shifted Interpolation for Differential Privacy

**Source**: [https://proceedings.mlr.press/v235/bok24a.html](https://proceedings.mlr.press/v235/bok24a.html)

**TLDR**: This paper introduces shifted interpolation to tighten privacy analysis of noisy gradient descent for differentially private machine learning with convex losses.

## Abstract

Noisy gradient descent and its variants are the predominant algorithms for differentially private machine learning. It is a fundamental question to quantify their privacy leakage, yet tight characterizations remain open even in the foundational setting of convex losses. This paper improves over previous analyses by establishing (and refining) the “privacy amplification by iteration” phenomenon in the unifying framework of $f$-differential privacy—which tightly captures all aspects of the privacy loss and immediately implies tighter privacy accounting in other notions of differential privacy, e.g., $(\varepsilon,\delta)$-DP and Rényi DP. Our key technical insight is the construction of shifted interpolated processes that unravel the popular shifted-divergences argument, enabling generalizations beyond divergence-based relaxations of DP. Notably, this leads to the first exact privacy analysis in the foundational setting of strongly convex optimization. Our techniques extend to many settings: convex/strongly convex, constrained/unconstrained, full/cyclic/stochastic batches, and all combinations thereof. As an immediate corollary, we recover the $f$-DP characterization of the exponential mechanism for strongly convex optimization in Gopi et al. (2022), and moreover extend this result to more general settings.