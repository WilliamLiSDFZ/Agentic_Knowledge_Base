---
title: "Ensemble Pruning for Out-of-distribution Generalization"
source: "https://proceedings.mlr.press/v235/qiao24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/qiao24a/qiao24a.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['ensemble-pruning', 'out-of-distribution', 'diversity', 'distribution-shift', 'generalization']
venue: "ICML 2024"
tldr: "A method for pruning neural network ensembles to improve predictive diversity and out-of-distribution generalization."
---

# Ensemble Pruning for Out-of-distribution Generalization

**Source**: [https://proceedings.mlr.press/v235/qiao24a.html](https://proceedings.mlr.press/v235/qiao24a.html)

**TLDR**: A method for pruning neural network ensembles to improve predictive diversity and out-of-distribution generalization.

## Abstract

Ensemble of deep neural networks has achieved great success in hedging against single-model failure under distribution shift. However, existing techniques suffer from producing redundant models, limiting predictive diversity and yielding compromised generalization performance. Existing ensemble pruning methods can only guarantee predictive diversity for in-distribution data, which may not transfer well to out-of-distribution (OoD) data. To address this gap, we propose a principled optimization framework for ensemble pruning under distribution shifts. Since the annotations of test data are not available, we explore relationships between prediction distributions of the models, encapsulated in a topology graph. By incorporating this topology into a combinatorial optimization framework, complementary models with high predictive diversity are selected with theoretical guarantees. Our approach is model-agnostic and can be applied on top of a broad spectrum of off-the-shelf ensembling methods for improved generalization performance. Experiments on common benchmarks demonstrate the superiority of our approach in both multi- and single-source OoD generalization. The source codes are publicly available at: https://github.com/joffery/TEP.