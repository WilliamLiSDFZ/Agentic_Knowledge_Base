---
title: "Harnessing Hierarchical Label Distribution Variations in Test Agnostic Long-tail Recognition"
source: "https://proceedings.mlr.press/v235/yang24af.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24af/yang24af.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['long-tail-recognition', 'distribution-shift', 'hierarchical']
venue: "ICML 2024"
tldr: "A hierarchical approach to test-agnostic long-tail recognition that decomposes unknown test label distribution variations into global and local levels."
---

# Harnessing Hierarchical Label Distribution Variations in Test Agnostic Long-tail Recognition

**Source**: [https://proceedings.mlr.press/v235/yang24af.html](https://proceedings.mlr.press/v235/yang24af.html)

**TLDR**: A hierarchical approach to test-agnostic long-tail recognition that decomposes unknown test label distribution variations into global and local levels.

## Abstract

This paper explores test-agnostic long-tail recognition, a challenging long-tail task where the test label distributions are unknown and arbitrarily imbalanced. We argue that the variation in these distributions can be broken down hierarchically into global and local levels. The global ones reflect a broad range of diversity, while the local ones typically arise from milder changes, often focused On a particular neighbor. Traditional methods predominantly use a Mixture-of-Expert (MoE) approach, targeting a few fixed test label distributions that exhibit substantial global variations. However, the local variations are left unconsidered. To address this issue, we propose a new MoE strategy, $\mathsf{DirMixE}$, which assigns experts to different Dirichlet meta-distributions of the label distribution, each targeting a specific aspect of local variations. Additionally, the diversity among these Dirichlet meta-distributions inherently captures global variations. This dual-level approach also leads to a more stable objective function, allowing us to sample different test distributions better to quantify the mean and variance of performance outcomes. Theoretically, we show that our proposed objective benefits from enhanced generalization by virtue of the variance-based regularization. Comprehensive experiments across multiple benchmarks confirm the effectiveness of $\mathsf{DirMixE}$.