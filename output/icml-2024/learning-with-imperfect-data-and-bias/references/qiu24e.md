---
title: "Complexity Matters: Feature Learning in the Presence of Spurious Correlations"
source: "https://proceedings.mlr.press/v235/qiu24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/qiu24e/qiu24e.pdf"
categories: ['neural-network-learning-dynamics-theory', 'learning-with-imperfect-data-and-bias']
tags: ['spurious-correlations', 'feature-learning', 'learning-dynamics', 'complexity', 'neural-networks']
venue: "ICML 2024"
tldr: "An analysis of how relative complexity of spurious vs. core features affects neural network learning dynamics."
---

# Complexity Matters: Feature Learning in the Presence of Spurious Correlations

**Source**: [https://proceedings.mlr.press/v235/qiu24e.html](https://proceedings.mlr.press/v235/qiu24e.html)

**TLDR**: An analysis of how relative complexity of spurious vs. core features affects neural network learning dynamics.

## Abstract

Existing research often posits spurious features as easier to learn than core features in neural network optimization, but the impact of their relative simplicity remains under-explored. Moreover, studies mainly focus on end performance rather than the learning dynamics of feature learning. In this paper, we propose a theoretical framework and an associated synthetic dataset grounded in boolean function analysis. This setup allows for fine-grained control over the relative complexity (compared to core features) and correlation strength (with respect to the label) of spurious features to study the dynamics of feature learning under spurious correlations. Our findings uncover several interesting phenomena: (1) stronger spurious correlations or simpler spurious features slow down the learning rate of the core features, (2) two distinct subnetworks are formed to learn core and spurious features separately, (3) learning phases of spurious and core features are not always separable, (4) spurious features are not forgotten even after core features are fully learned. We demonstrate that our findings justify the success of retraining the last layer to remove spurious correlation and also identifies limitations of popular debiasing algorithms that exploit early learning of spurious features. We support our empirical findings with theoretical analyses for the case of learning XOR features with a one-hidden-layer ReLU network.