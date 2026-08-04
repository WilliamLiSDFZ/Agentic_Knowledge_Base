---
title: "Conformal Prediction for Deep Classifier via Label Ranking"
source: "https://proceedings.mlr.press/v235/huang24aa.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24aa/huang24aa.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['conformal-prediction', 'label-ranking', 'coverage-guarantee', 'calibration', 'classification']
venue: "ICML 2024"
tldr: "Improves conformal prediction for deep classifiers via label ranking to reduce prediction set sizes while maintaining coverage guarantees."
---

# Conformal Prediction for Deep Classifier via Label Ranking

**Source**: [https://proceedings.mlr.press/v235/huang24aa.html](https://proceedings.mlr.press/v235/huang24aa.html)

**TLDR**: Improves conformal prediction for deep classifiers via label ranking to reduce prediction set sizes while maintaining coverage guarantees.

## Abstract

Conformal prediction is a statistical framework that generates prediction sets containing ground-truth labels with a desired coverage guarantee. The predicted probabilities produced by machine learning models are generally miscalibrated, leading to large prediction sets in conformal prediction. To address this issue, we propose a novel algorithm named $\textit{Sorted Adaptive Prediction Sets}$ (SAPS), which discards all the probability values except for the maximum softmax probability. The key idea behind SAPS is to minimize the dependence of the non-conformity score on the probability values while retaining the uncertainty information. In this manner, SAPS can produce compact prediction sets and communicate instance-wise uncertainty. Extensive experiments validate that SAPS not only lessens the prediction sets but also broadly enhances the conditional coverage rate of prediction sets.