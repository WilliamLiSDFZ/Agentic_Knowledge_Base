---
title: "How Flawed Is ECE? An Analysis via Logit Smoothing"
source: "https://proceedings.mlr.press/v235/chidambaram24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chidambaram24a/chidambaram24a.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['calibration', 'expected-calibration-error', 'logit-smoothing']
venue: "ICML 2024"
tldr: "An analysis of ECE's flaws via logit smoothing reveals systematic biases in this widely used calibration metric."
---

# How Flawed Is ECE? An Analysis via Logit Smoothing

**Source**: [https://proceedings.mlr.press/v235/chidambaram24a.html](https://proceedings.mlr.press/v235/chidambaram24a.html)

**TLDR**: An analysis of ECE's flaws via logit smoothing reveals systematic biases in this widely used calibration metric.

## Abstract

Informally, a model is calibrated if its predictions are correct with a probability that matches the confidence of the prediction. By far the most common method in the literature for measuring calibration is the expected calibration error (ECE). Recent work, however, has pointed out drawbacks of ECE, such as the fact that it is discontinuous in the space of predictors. In this work, we ask: how fundamental are these issues, and what are their impacts on existing results? Towards this end, we completely characterize the discontinuities of ECE with respect to general probability measures on Polish spaces. We then use the nature of these discontinuities to motivate a novel continuous, easily estimated miscalibration metric, which we term Logit-Smoothed ECE (LS-ECE). By comparing the ECE and LS-ECE of pre-trained image classification models, we show in initial experiments that binned ECE closely tracks LS-ECE, indicating that the theoretical pathologies of ECE may be avoidable in practice.