---
title: "Improving Sharpness-Aware Minimization by Lookahead"
source: "https://proceedings.mlr.press/v235/yu24q.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yu24q/yu24q.pdf"
categories: ['optimization-algorithms-convergence-theory', 'neural-network-learning-dynamics-theory']
tags: ['sharpness-aware-minimization', 'lookahead', 'optimization', 'generalization']
venue: "ICML 2024"
tldr: "Combines lookahead optimization with SAM to address convergence instability and improve generalization performance."
---

# Improving Sharpness-Aware Minimization by Lookahead

**Source**: [https://proceedings.mlr.press/v235/yu24q.html](https://proceedings.mlr.press/v235/yu24q.html)

**TLDR**: Combines lookahead optimization with SAM to address convergence instability and improve generalization performance.

## Abstract

Sharpness-Aware Minimization (SAM), which performs gradient descent on adversarially perturbed weights, can improve generalization by identifying flatter minima. However, recent studies have shown that SAM may suffer from convergence instability and oscillate around saddle points, resulting in slow convergence and inferior performance. To address this problem, we propose the use of a lookahead mechanism to gather more information about the landscape by looking further ahead, and thus find a better trajectory to converge. By examining the nature of SAM, we simplify the extrapolation procedure, resulting in a more efficient algorithm. Theoretical results show that the proposed method converges to a stationary point and is less prone to saddle points. Experiments on standard benchmark datasets also verify that the proposed method outperforms the SOTAs, and converge more effectively to flat minima.