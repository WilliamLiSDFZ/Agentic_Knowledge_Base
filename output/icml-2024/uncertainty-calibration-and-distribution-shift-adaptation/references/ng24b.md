---
title: "Measuring Stochastic Data Complexity with Boltzmann Influence Functions"
source: "https://proceedings.mlr.press/v235/ng24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ng24b/ng24b.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['minimum-description-length', 'boltzmann-influence', 'prediction-uncertainty']
venue: "ICML 2024"
tldr: "Boltzmann influence functions are used to efficiently approximate pNML-based stochastic data complexity for uncertainty estimation under distribution shift."
---

# Measuring Stochastic Data Complexity with Boltzmann Influence Functions

**Source**: [https://proceedings.mlr.press/v235/ng24b.html](https://proceedings.mlr.press/v235/ng24b.html)

**TLDR**: Boltzmann influence functions are used to efficiently approximate pNML-based stochastic data complexity for uncertainty estimation under distribution shift.

## Abstract

Estimating the uncertainty of a model’s prediction on a test point is a crucial part of ensuring reliability and calibration under distribution shifts.A minimum description length approach to this problem uses the predictive normalized maximum likelihood (pNML) distribution, which considers every possible label for a data point, and decreases confidence in a prediction if other labels are also consistent with the model and training data. In this work we propose IF-COMP, a scalable and efficient approximation of the pNML distribution that linearizes the model with a temperature-scaled Boltzmann influence function. IF-COMP can be used to produce well-calibrated predictions on test points as well as measure complexity in both labelled and unlabelled settings. We experimentally validate IF-COMP on uncertainty calibration, mislabel detection, and OOD detection tasks, where it consistently matches or beats strong baseline methods.