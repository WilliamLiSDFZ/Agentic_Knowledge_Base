---
title: "Investigating the Impact of Model Instability on Explanations and Uncertainty"
source: "https://aclanthology.org/2024.findings-acl.705/"
categories: ['llm-training-alignment-and-evaluation', 'nlp-benchmark-design-and-interpretability']
tags: ['explainability', 'model-instability', 'uncertainty', 'perturbation', 'xai']
venue: "ACL 2024"
tldr: "Investigates how model instability caused by small input perturbations distorts explanations and affects uncertainty estimates."
---

# Investigating the Impact of Model Instability on Explanations and Uncertainty

**Source**: [https://aclanthology.org/2024.findings-acl.705/](https://aclanthology.org/2024.findings-acl.705/)

**TLDR**: Investigates how model instability caused by small input perturbations distorts explanations and affects uncertainty estimates.

## Abstract

AbstractExplainable AI methods facilitate the understanding of model behaviour, yet, small, imperceptible perturbations to inputs can vastly distort explanations. As these explanations are typically evaluated holistically, before model deployment, it is difficult to assess when a particular explanation is trustworthy. Some studies have tried to create confidence estimators for explanations, but none have investigated an existing link between uncertainty and explanation quality. We artificially simulate epistemic uncertainty in text input by introducing noise at inference time. In this large-scale empirical study, we insert different levels of noise perturbations and measure the effect on the output of pre-trained language models and different uncertainty metrics. Realistic perturbations have minimal effect on performance and explanations, yet masking has a drastic effect. We find that high uncertainty doesn’t necessarily imply low explanation plausibility; the correlation between the two metrics can be moderately positive when noise is exposed during the training process. This suggests that noise-augmented models may be better at identifying salient tokens when uncertain. Furthermore, when predictive and epistemic uncertainty measures are over-confident, the robustness of a saliency map to perturbation can indicate model stability issues. Integrated Gradients shows the overall greatest robustness to perturbation, while still showing model-specific patterns in performance; however, this phenomenon is limited to smaller Transformer-based language models.