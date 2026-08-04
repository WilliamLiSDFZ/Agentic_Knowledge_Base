---
title: "CogDPM: Diffusion Probabilistic Models via Cognitive Predictive Coding"
source: "https://proceedings.mlr.press/v235/chen24o.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24o/chen24o.pdf"
categories: ['generative-models-and-variational-inference', 'neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['diffusion-models', 'predictive-coding', 'spatiotemporal-prediction', 'cognitive-science']
venue: "ICML 2024"
tldr: "CogDPM incorporates predictive coding principles from cognitive science into diffusion probabilistic models for improved spatiotemporal prediction."
---

# CogDPM: Diffusion Probabilistic Models via Cognitive Predictive Coding

**Source**: [https://proceedings.mlr.press/v235/chen24o.html](https://proceedings.mlr.press/v235/chen24o.html)

**TLDR**: CogDPM incorporates predictive coding principles from cognitive science into diffusion probabilistic models for improved spatiotemporal prediction.

## Abstract

Predictive Coding (PC) is a theoretical framework in cognitive science suggesting that the human brain processes cognition through spatiotemporal prediction of visual world. Existing studies have developed spatiotemporal prediction neural networks based on the PC theroy, emulating its two core mechanisms: Correcting predictions from residuals and Hierarchical learning. However, these models do not show the enhancement of prediction skills on real-world forecasting tasks, and ignore the Precision Weighting mechanism of PC theory. Precision weight posits that the brain allocates more attention to signals with lower Precision, contributing to the the cognitive ability of human brains. This work introduces the Cognitive Diffusion Probabilistic Models (CogDPM) which demonstrates the connection between diffusion probabilistic models and PC theory. CogDPM features a precision estimation method based on the hierarchical sampling capabilities of diffusion models, and allocate the guidance with precision weights estimated by the inherent property of diffusion models. We experimentally show that the precision weights is an estimator of model’s predictability on the rigid body and fluid motion dataset. We also apply CogDPM to real-world prediction tasks using the U.K. precipitation and ERA surface wind datasets. Our results demonstrate that CogDPM outperforms both existing domain-specific operational models and general deep prediction models in providing more proficient forecasting.