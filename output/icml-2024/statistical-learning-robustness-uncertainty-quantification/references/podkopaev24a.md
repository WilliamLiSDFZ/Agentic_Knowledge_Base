---
title: "Adaptive Conformal Inference by Betting"
source: "https://proceedings.mlr.press/v235/podkopaev24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/podkopaev24a/podkopaev24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['conformal-prediction', 'adaptive-inference', 'betting']
venue: "ICML 2024"
tldr: "An adaptive conformal inference method using betting strategies to handle non-exchangeable data distributions."
---

# Adaptive Conformal Inference by Betting

**Source**: [https://proceedings.mlr.press/v235/podkopaev24a.html](https://proceedings.mlr.press/v235/podkopaev24a.html)

**TLDR**: An adaptive conformal inference method using betting strategies to handle non-exchangeable data distributions.

## Abstract

Conformal prediction is a valuable tool for quantifying predictive uncertainty of machine learning models. However, its applicability relies on the assumption of data exchangeability, a condition which is often not met in real-world scenarios. In this paper, we consider the problem of adaptive conformal inference without any assumptions about the data generating process. Existing approaches for adaptive conformal inference are based on optimizing the pinball loss using variants of online gradient descent. A notable shortcoming of such approaches is in their explicit dependence on and sensitivity to the choice of the learning rates. In this paper, we propose a different approach for adaptive conformal inference that leverages parameter-free online convex optimization techniques. We prove that our method controls long-term miscoverage frequency at a nominal level and demonstrate its convincing empirical performance without any need of performing cumbersome parameter tuning.