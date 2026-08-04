---
title: "Refined Coreset Selection: Towards Minimal Coreset Size under Model Performance Constraints"
source: "https://proceedings.mlr.press/v235/xia24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xia24b/xia24b.pdf"
categories: ['data-selection-and-active-learning-methods', 'sampling-compression-and-dimensionality-reduction']
tags: ['coreset-selection', 'data-compression', 'minimal-coreset', 'deep-learning', 'data-efficiency']
venue: "ICML 2024"
tldr: "Proposes refined coreset selection methods to minimize coreset size while maintaining model performance, reducing computational costs for deep learning training."
---

# Refined Coreset Selection: Towards Minimal Coreset Size under Model Performance Constraints

**Source**: [https://proceedings.mlr.press/v235/xia24b.html](https://proceedings.mlr.press/v235/xia24b.html)

**TLDR**: Proposes refined coreset selection methods to minimize coreset size while maintaining model performance, reducing computational costs for deep learning training.

## Abstract

Coreset selection is powerful in reducing computational costs and accelerating data processing for deep learning algorithms. It strives to identify a small subset from large-scale data, so that training only on the subset practically performs on par with full data. Practitioners regularly desire to identify the smallest possible coreset in realistic scenes while maintaining comparable model performance, to minimize costs and maximize acceleration. Motivated by this desideratum, for the first time, we pose the problem of refined coreset selection, in which the minimal coreset size under model performance constraints is explored. Moreover, to address this problem, we propose an innovative method, which maintains optimization priority order over the model performance and coreset size, and efficiently optimizes them in the coreset selection procedure. Theoretically, we provide the convergence guarantee of the proposed method. Empirically, extensive experiments confirm its superiority compared with previous strategies, often yielding better model performance with smaller coreset sizes. The implementation is available at https://github.com/xiaoboxia/LBCS.