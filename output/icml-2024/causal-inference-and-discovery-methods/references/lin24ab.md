---
title: "Plug-in Performative Optimization"
source: "https://proceedings.mlr.press/v235/lin24ab.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24ab/lin24ab.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'causal-inference-and-discovery-methods']
tags: ['performative-prediction', 'distribution-shift', 'risk-minimization']
venue: "ICML 2024"
tldr: "A plug-in approach for performative optimization that minimizes performative risk by accounting for prediction-induced distribution shifts."
---

# Plug-in Performative Optimization

**Source**: [https://proceedings.mlr.press/v235/lin24ab.html](https://proceedings.mlr.press/v235/lin24ab.html)

**TLDR**: A plug-in approach for performative optimization that minimizes performative risk by accounting for prediction-induced distribution shifts.

## Abstract

When predictions are performative, the choice of which predictor to deploy influences the distribution of future observations. The overarching goal in learning under performativity is to find a predictor that has low performative risk, that is, good performance on its induced distribution. One family of solutions for optimizing the performative risk, including bandits and other derivative-free methods, is agnostic to any structure in the performative feedback, leading to exceedingly slow convergence rates. A complementary family of solutions makes use of explicit models for the feedback, such as best-response models in strategic classification, enabling faster rates. However, these rates critically rely on the feedback model being correct. In this work we study a general protocol for making use of possibly misspecified models in performative prediction, called plug-in performative optimization. We show this solution can be far superior to model-agnostic strategies, as long as the misspecification is not too extreme. Our results support the hypothesis that models, even if misspecified, can indeed help with learning in performative settings.