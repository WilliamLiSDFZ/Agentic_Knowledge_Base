---
title: "Is Epistemic Uncertainty Faithfully Represented by Evidential Deep Learning Methods?"
source: "https://proceedings.mlr.press/v235/juergens24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/juergens24a/juergens24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['epistemic-uncertainty', 'evidential-deep-learning', 'Bayesian-methods', 'uncertainty-quantification']
venue: "ICML 2024"
tldr: "Critically evaluates whether evidential deep learning methods faithfully represent epistemic uncertainty compared to Bayesian approaches."
---

# Is Epistemic Uncertainty Faithfully Represented by Evidential Deep Learning Methods?

**Source**: [https://proceedings.mlr.press/v235/juergens24a.html](https://proceedings.mlr.press/v235/juergens24a.html)

**TLDR**: Critically evaluates whether evidential deep learning methods faithfully represent epistemic uncertainty compared to Bayesian approaches.

## Abstract

Trustworthy ML systems should not only return accurate predictions, but also a reliable representation of their uncertainty. Bayesian methods are commonly used to quantify both aleatoric and epistemic uncertainty, but alternative approaches, such as evidential deep learning methods, have become popular in recent years. The latter group of methods in essence extends empirical risk minimization (ERM) for predicting second-order probability distributions over outcomes, from which measures of epistemic (and aleatoric) uncertainty can be extracted. This paper presents novel theoretical insights of evidential deep learning, highlighting the difficulties in optimizing second-order loss functions and interpreting the resulting epistemic uncertainty measures. With a systematic setup that covers a wide range of approaches for classification, regression and counts, it provides novel insights into issues of identifiability and convergence in second-order loss minimization, and the relative (rather than absolute) nature of epistemic uncertainty measures.