---
title: "On the Universality of Volume-Preserving and Coupling-Based Normalizing Flows"
source: "https://proceedings.mlr.press/v235/draxler24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/draxler24a/draxler24a.pdf"
categories: ['generative-models-and-variational-inference']
tags: ['normalizing-flows', 'universality', 'volume-preserving', 'coupling-layers']
venue: "ICML 2024"
tldr: "A novel theoretical framework is presented proving universality of volume-preserving and coupling-based normalizing flows without requiring unrestricted architectures."
---

# On the Universality of Volume-Preserving and Coupling-Based Normalizing Flows

**Source**: [https://proceedings.mlr.press/v235/draxler24a.html](https://proceedings.mlr.press/v235/draxler24a.html)

**TLDR**: A novel theoretical framework is presented proving universality of volume-preserving and coupling-based normalizing flows without requiring unrestricted architectures.

## Abstract

We present a novel theoretical framework for understanding the expressive power of normalizing flows. Despite their prevalence in scientific applications, a comprehensive understanding of flows remains elusive due to their restricted architectures. Existing theorems fall short as they require the use of arbitrarily ill-conditioned neural networks, limiting practical applicability. We propose a distributional universality theorem for well-conditioned coupling-based normalizing flows such as RealNVP. In addition, we show that volume-preserving normalizing flows are not universal, what distribution they learn instead, and how to fix their expressivity. Our results support the general wisdom that affine and related couplings are expressive and in general outperform volume-preserving flows, bridging a gap between empirical results and theoretical understanding.