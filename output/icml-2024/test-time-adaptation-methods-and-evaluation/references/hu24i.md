---
title: "Pseudo-Calibration: Improving Predictive Uncertainty Estimation in Unsupervised Domain Adaptation"
source: "https://proceedings.mlr.press/v235/hu24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hu24i/hu24i.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation', 'test-time-adaptation-methods-and-evaluation']
tags: ['domain-adaptation', 'calibration', 'uncertainty', 'pseudo-labels', 'unsupervised']
venue: "ICML 2024"
tldr: "Introduces pseudo-calibration to improve predictive uncertainty estimation in unsupervised domain adaptation without access to labeled target data."
---

# Pseudo-Calibration: Improving Predictive Uncertainty Estimation in Unsupervised Domain Adaptation

**Source**: [https://proceedings.mlr.press/v235/hu24i.html](https://proceedings.mlr.press/v235/hu24i.html)

**TLDR**: Introduces pseudo-calibration to improve predictive uncertainty estimation in unsupervised domain adaptation without access to labeled target data.

## Abstract

Unsupervised domain adaptation (UDA) has seen substantial efforts to improve model accuracy for an unlabeled target domain with the help of a labeled source domain. However, UDA models often exhibit poorly calibrated predictive uncertainty on target data, a problem that remains under-explored and poses risks in safety-critical UDA applications. The calibration problem in UDA is particularly challenging due to the absence of labeled target data and severe distribution shifts between domains. In this paper, we approach UDA calibration as a target-domain-specific unsupervised problem, different from mainstream solutions based on covariate shift. We introduce Pseudo-Calibration (PseudoCal), a novel post-hoc calibration framework. Our innovative use of inference-stage mixup synthesizes a labeled pseudo-target set capturing the structure of the real unlabeled target data. This turns the unsupervised calibration problem into a supervised one, easily solvable with temperature scaling. Extensive empirical evaluations across 5 diverse UDA scenarios involving 10 UDA methods consistently demonstrate the superior performance and versatility of PseudoCal over existing solutions.