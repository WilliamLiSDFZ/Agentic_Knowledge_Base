---
title: "Online conformal prediction with decaying step sizes"
source: "https://proceedings.mlr.press/v235/angelopoulos24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/angelopoulos24a/angelopoulos24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['conformal-prediction', 'online-learning', 'coverage-guarantee', 'decaying-step-sizes', 'quantile-estimation']
venue: "ICML 2024"
tldr: "Introduces online conformal prediction with decaying step sizes that provides retrospective coverage guarantees while estimating population quantiles."
---

# Online conformal prediction with decaying step sizes

**Source**: [https://proceedings.mlr.press/v235/angelopoulos24a.html](https://proceedings.mlr.press/v235/angelopoulos24a.html)

**TLDR**: Introduces online conformal prediction with decaying step sizes that provides retrospective coverage guarantees while estimating population quantiles.

## Abstract

We introduce a method for online conformal prediction with decaying step sizes. Like previous methods, ours possesses a retrospective guarantee of coverage for arbitrary sequences. However, unlike previous methods, we can simultaneously estimate a population quantile when it exists. Our theory and experiments indicate substantially improved practical properties: in particular, when the distribution is stable, the coverage is close to the desired level for every time point, not just on average over the observed sequence.