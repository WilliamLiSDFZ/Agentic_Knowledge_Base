---
title: "Handling Heterogeneous Curvatures in Bandit LQR Control"
source: "https://proceedings.mlr.press/v235/yan24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yan24f/yan24f.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['bandit-feedback', 'LQR-control', 'heterogeneous-curvature']
venue: "ICML 2024"
tldr: "Investigates online LQR control with bandit feedback and heterogeneous cost curvatures, enabling adaptation to varying convexity conditions."
---

# Handling Heterogeneous Curvatures in Bandit LQR Control

**Source**: [https://proceedings.mlr.press/v235/yan24f.html](https://proceedings.mlr.press/v235/yan24f.html)

**TLDR**: Investigates online LQR control with bandit feedback and heterogeneous cost curvatures, enabling adaptation to varying convexity conditions.

## Abstract

We investigate online Linear Quadratic Regulator (LQR) with bandit feedback and semi-adversarial disturbances. Previous works assume costs with homogeneous curvatures (i.e., with a uniform strong convexity lower bound), which can be hard to satisfy in many real scenarios and prohibits adapting to true curvatures for better performance. In this paper, we initiate the study of bandit LQR control with heterogeneous cost curvatures, aiming to strengthen the algorithm’s adaptivity. To achieve this, we reduce the problem to bandit convex optimization with memory via a “with-history” reduction to avoid hard-to-control truncation errors. Then we provide a novel analysis for an important stability term that appeared in both regret and memory, using Newton decrement developed in interior-point methods. The analysis enables us to guarantee memory-related terms introduced in the reduction and also provide a simplified analysis for handling heterogeneous curvatures in bandit convex optimization. Finally, we achieve interpolated guarantees that can not only recover existing bounds for convex and quadratic costs but also attain new implications for cases of corrupted and decaying quadraticity.