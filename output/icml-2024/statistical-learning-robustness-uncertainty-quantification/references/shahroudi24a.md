---
title: "Evaluation of Trajectory Distribution Predictions with Energy Score"
source: "https://proceedings.mlr.press/v235/shahroudi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shahroudi24a/shahroudi24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'time-series-modeling-and-forecasting-methods']
tags: ['trajectory-prediction', 'uncertainty-quantification', 'energy-score']
venue: "ICML 2024"
tldr: "This paper evaluates trajectory distribution predictions using energy scores to better capture uncertainty in autonomous systems planning."
---

# Evaluation of Trajectory Distribution Predictions with Energy Score

**Source**: [https://proceedings.mlr.press/v235/shahroudi24a.html](https://proceedings.mlr.press/v235/shahroudi24a.html)

**TLDR**: This paper evaluates trajectory distribution predictions using energy scores to better capture uncertainty in autonomous systems planning.

## Abstract

Predicting the future trajectory of surrounding objects is inherently uncertain and vital in the safe and reliable planning of autonomous systems such as in self-driving cars. Although trajectory prediction models have become increasingly sophisticated in dealing with the complexities of spatiotemporal data, the evaluation methods used to assess these models have not kept pace. "Minimum of N" is a common family of metrics used to assess the rich outputs of such models. We critically examine the Minimum of N within the proper scoring rules framework to show that it is not strictly proper and demonstrate how that could lead to a misleading assessment of multimodal trajectory predictions. As an alternative, we propose using Energy Score-based evaluation measures, leveraging their proven propriety for a more reliable evaluation of trajectory distribution predictions.