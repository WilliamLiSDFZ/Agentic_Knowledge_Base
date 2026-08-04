---
title: "Scaling Exponents Across Parameterizations and Optimizers"
source: "https://proceedings.mlr.press/v235/everett24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/everett24a/everett24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'optimization-algorithms-convergence-theory']
tags: ['scaling-laws', 'parameterization', 'optimizers', 'neural-network-width', 'hyperparameter-transfer']
venue: "ICML 2024"
tldr: "Investigates how scaling exponents vary across parameterizations and optimizers to enable more robust and consistent model scaling."
---

# Scaling Exponents Across Parameterizations and Optimizers

**Source**: [https://proceedings.mlr.press/v235/everett24a.html](https://proceedings.mlr.press/v235/everett24a.html)

**TLDR**: Investigates how scaling exponents vary across parameterizations and optimizers to enable more robust and consistent model scaling.

## Abstract

Robust and effective scaling of models from small to large width typically requires the precise adjustment of many algorithmic and architectural details, such as parameterization and optimizer choices. In this work, we propose a new perspective on parameterization by investigating a key assumption in prior work about the alignment between parameters and data and derive new theoretical results under weaker assumptions and a broader set of optimizers. Our extensive empirical investigation includes tens of thousands of models trained with all combinations of three optimizers, four parameterizations, several alignment assumptions, more than a dozen learning rates, and fourteen model sizes up to 27B parameters. We find that the best learning rate scaling prescription would often have been excluded by the assumptions in prior work. Our results show that all parameterizations, not just maximal update parameterization (muP), can achieve hyperparameter transfer; moreover, our novel per-layer learning rate prescription for standard parameterization outperforms muP. Finally, we demonstrate that an overlooked aspect of parameterization, the epsilon parameter in Adam, must be scaled correctly to avoid gradient underflow and propose Adam-atan2, a new numerically stable, scale-invariant version of Adam that eliminates the epsilon hyperparameter entirely.