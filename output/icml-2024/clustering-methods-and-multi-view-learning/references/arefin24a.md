---
title: "Unsupervised Concept Discovery Mitigates Spurious Correlations"
source: "https://proceedings.mlr.press/v235/arefin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/arefin24a/arefin24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'clustering-methods-and-multi-view-learning']
tags: ['spurious-correlations', 'concept-discovery', 'unsupervised-learning', 'bias-mitigation']
venue: "ICML 2024"
tldr: "Proposes unsupervised concept discovery to mitigate spurious correlations without requiring prior knowledge or group annotations."
---

# Unsupervised Concept Discovery Mitigates Spurious Correlations

**Source**: [https://proceedings.mlr.press/v235/arefin24a.html](https://proceedings.mlr.press/v235/arefin24a.html)

**TLDR**: Proposes unsupervised concept discovery to mitigate spurious correlations without requiring prior knowledge or group annotations.

## Abstract

Models prone to spurious correlations in training data often produce brittle predictions and introduce unintended biases. Addressing this challenge typically involves methods relying on prior knowledge and group annotation to remove spurious correlations, which may not be readily available in many applications. In this paper, we establish a novel connection between unsupervised object-centric learning and mitigation of spurious correlations. Instead of directly inferring subgroups with varying correlations with labels, our approach focuses on discovering concepts: discrete ideas that are shared across input samples. Leveraging existing object-centric representation learning, we introduce CoBalT: a concept balancing technique that effectively mitigates spurious correlations without requiring human labeling of subgroups. Evaluation across the benchmark datasets for sub-population shifts demonstrate superior or competitive performance compared state-of-the-art baselines, without the need for group annotation. Code is available at https://github.com/rarefin/CoBalT