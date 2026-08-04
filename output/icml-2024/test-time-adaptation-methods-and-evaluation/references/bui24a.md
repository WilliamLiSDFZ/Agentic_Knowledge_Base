---
title: "Density-Softmax: Efficient Test-time Model for Uncertainty Estimation and Robustness under Distribution Shifts"
source: "https://proceedings.mlr.press/v235/bui24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bui24a/bui24a.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['uncertainty-estimation', 'test-time', 'distribution-shift', 'efficiency']
venue: "ICML 2024"
tldr: "Density-Softmax provides efficient test-time uncertainty estimation and robustness to distribution shifts without the high cost of ensembles or BNNs."
---

# Density-Softmax: Efficient Test-time Model for Uncertainty Estimation and Robustness under Distribution Shifts

**Source**: [https://proceedings.mlr.press/v235/bui24a.html](https://proceedings.mlr.press/v235/bui24a.html)

**TLDR**: Density-Softmax provides efficient test-time uncertainty estimation and robustness to distribution shifts without the high cost of ensembles or BNNs.

## Abstract

Sampling-based methods, e.g., Deep Ensembles and Bayesian Neural Nets have become promising approaches to improve the quality of uncertainty estimation and robust generalization. However, they suffer from a large model size and high latency at test time, which limits the scalability needed for low-resource devices and real-time applications. To resolve these computational issues, we propose Density-Softmax, a sampling-free deterministic framework via combining a density function built on a Lipschitz-constrained feature extractor with the softmax layer. Theoretically, we show that our model is the solution of minimax uncertainty risk and is distance-aware on feature space, thus reducing the over-confidence of the standard softmax under distribution shifts. Empirically, our method enjoys competitive results with state-of-the-art techniques in terms of uncertainty and robustness, while having a lower number of model parameters and a lower latency at test time.