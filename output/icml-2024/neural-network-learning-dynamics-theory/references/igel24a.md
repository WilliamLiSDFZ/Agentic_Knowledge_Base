---
title: "Smooth Min-Max Monotonic Networks"
source: "https://proceedings.mlr.press/v235/igel24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/igel24a/igel24a.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'neural-network-learning-dynamics-theory']
tags: ['monotonic-networks', 'min-max-architecture', 'fairness', 'regularization', 'smooth-optimization']
venue: "ICML 2024"
tldr: "Proposes smooth min-max monotonic networks that avoid underdescent issues while enforcing monotonicity constraints for fair and plausible modeling."
---

# Smooth Min-Max Monotonic Networks

**Source**: [https://proceedings.mlr.press/v235/igel24a.html](https://proceedings.mlr.press/v235/igel24a.html)

**TLDR**: Proposes smooth min-max monotonic networks that avoid underdescent issues while enforcing monotonicity constraints for fair and plausible modeling.

## Abstract

Monotonicity constraints are powerful regularizers in statistical modelling. They can support fairness in computer-aided decision making and increase plausibility in data-driven scientific models. The seminal min-max (MM) neural network architecture ensures monotonicity, but often gets stuck in undesired local optima during training because of partial derivatives being zero when computing extrema. We propose a simple modification of the MM network using strictly-increasing smooth minimum and maximum functions that alleviates this problem. The resulting smooth min-max (SMM) network module inherits the asymptotic approximation properties from the MM architecture. It can be used within larger deep learning systems trained end-to-end. The SMM module is conceptually simple and computationally less demanding than state-of-the-art neural networks for monotonic modelling. Our experiments show that this does not come with a loss in generalization performance compared to alternative neural and non-neural approaches.