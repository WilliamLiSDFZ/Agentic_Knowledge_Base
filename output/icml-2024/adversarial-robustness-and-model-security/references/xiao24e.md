---
title: "Uniformly Stable Algorithms for Adversarial Training and Beyond"
source: "https://proceedings.mlr.press/v235/xiao24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xiao24e/xiao24e.pdf"
categories: ['adversarial-robustness-and-model-security', 'optimization-algorithms-convergence-theory']
tags: ['adversarial-training', 'uniform-stability', 'robust-overfitting']
venue: "ICML 2024"
tldr: "Proposes uniformly stable algorithms for adversarial training to mitigate robust overfitting via stability-based generalization bounds."
---

# Uniformly Stable Algorithms for Adversarial Training and Beyond

**Source**: [https://proceedings.mlr.press/v235/xiao24e.html](https://proceedings.mlr.press/v235/xiao24e.html)

**TLDR**: Proposes uniformly stable algorithms for adversarial training to mitigate robust overfitting via stability-based generalization bounds.

## Abstract

In adversarial machine learning, neural networks suffer from a significant issue known as robust overfitting, where the robust test accuracy decreases over epochs (Rice et al., 2020). Recent research conducted by Xing et al., 2021;Xiao et al., 2022 has focused on studying the uniform stability of adversarial training. Their investigations revealed that SGD-based adversarial training fails to exhibit uniform stability, and the derived stability bounds align with the observed phenomenon of robust overfitting in experiments. This finding motivates us to develop uniformly stable algorithms specifically tailored for adversarial training. To this aim, we introduce Moreau envelope-$\mathcal{A}$ (ME-$\mathcal{A}$), a variant of the Moreau Envelope-type algorithm. We employ a Moreau envelope function to reframe the original problem as a min-min problem, separating the non-strong convexity and non-smoothness of the adversarial loss. Then, this approach alternates between solving the inner and outer minimization problems to achieve uniform stability without incurring additional computational overhead. In practical scenarios, we demonstrate the efficacy of ME-$\mathcal{A}$ in mitigating the issue of robust overfitting. Beyond its application in adversarial training, this represents a fundamental result in uniform stability analysis, as ME-$\mathcal{A}$ is the first algorithm to exhibit uniform stability for weakly-convex, non-smooth problems.