---
title: "Efficient Non-stationary Online Learning by Wavelets with Applications to Online Distribution Shift Adaptation"
source: "https://proceedings.mlr.press/v235/qian24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/qian24c/qian24c.pdf"
categories: ['online-learning-and-sequential-decision-making', 'time-series-modeling-and-forecasting-methods']
tags: ['dynamic-regret', 'non-stationary', 'online-learning', 'wavelets', 'distribution-shift', 'ensemble']
venue: "ICML 2024"
tldr: "A wavelet-based two-layer online ensemble method for efficient non-stationary online learning with improved dynamic regret bounds."
---

# Efficient Non-stationary Online Learning by Wavelets with Applications to Online Distribution Shift Adaptation

**Source**: [https://proceedings.mlr.press/v235/qian24c.html](https://proceedings.mlr.press/v235/qian24c.html)

**TLDR**: A wavelet-based two-layer online ensemble method for efficient non-stationary online learning with improved dynamic regret bounds.

## Abstract

Dynamic regret minimization offers a principled way for non-stationary online learning, where the algorithm’s performance is evaluated against changing comparators. Prevailing methods often employ a two-layer online ensemble, consisting of a group of base learners with different configurations and a meta learner that combines their outputs. Given the evident computational overhead associated with two-layer algorithms, this paper investigates how to attain optimal dynamic regret without deploying a model ensemble. To this end, we introduce the notion of underlying dynamic regret, a specific form of the general dynamic regret that can encompass many applications of interest. We show that almost optimal dynamic regret can be obtained using a single-layer model alone. This is achieved by an adaptive restart equipped with wavelet detection, wherein a novel streaming wavelet operator is introduced to online update the wavelet coefficients via a carefully designed binary indexed tree. We apply our method to the online label shift adaptation problem, leading to new algorithms with optimal dynamic regret and significantly improved computation/storage efficiency compared to prior arts. Extensive experiments validate our proposal.