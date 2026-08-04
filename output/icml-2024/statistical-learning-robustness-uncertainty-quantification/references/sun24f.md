---
title: "Online Algorithms with Uncertainty-Quantified Predictions"
source: "https://proceedings.mlr.press/v235/sun24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sun24f/sun24f.pdf"
categories: ['online-learning-and-sequential-decision-making', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['algorithms-with-predictions', 'uncertainty-quantification', 'online-algorithms', 'prediction-quality', 'robustness']
venue: "ICML 2024"
tldr: "Online algorithms are developed that leverage uncertainty-quantified predictions to improve performance beyond worst-case while maintaining robustness guarantees."
---

# Online Algorithms with Uncertainty-Quantified Predictions

**Source**: [https://proceedings.mlr.press/v235/sun24f.html](https://proceedings.mlr.press/v235/sun24f.html)

**TLDR**: Online algorithms are developed that leverage uncertainty-quantified predictions to improve performance beyond worst-case while maintaining robustness guarantees.

## Abstract

The burgeoning field of algorithms with predictions studies the problem of using possibly imperfect machine learning predictions to improve online algorithm performance. While nearly all existing algorithms in this framework make no assumptions on prediction quality, a number of methods providing uncertainty quantification (UQ) on machine learning models have been developed in recent years, which could enable additional information about prediction quality at decision time. In this work, we investigate the problem of optimally utilizing uncertainty-quantified predictions in the design of online algorithms. In particular, we study two classic online problems, ski rental and online search, where the decision-maker is provided predictions augmented with UQ describing the likelihood of the ground truth falling within a particular range of values. We demonstrate that non-trivial modifications to algorithm design are needed to fully leverage the UQ predictions. Moreover, we consider how to utilize more general forms of UQ, proposing an online learning framework that learns to exploit UQ to make decisions in multi-instance settings.