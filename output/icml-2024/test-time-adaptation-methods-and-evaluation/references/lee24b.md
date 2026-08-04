---
title: "Stationary Latent Weight Inference for Unreliable Observations from Online Test-Time Adaptation"
source: "https://proceedings.mlr.press/v235/lee24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24b/lee24b.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['test-time-adaptation', 'distribution-shift', 'latent-weight-inference', 'online-learning']
venue: "ICML 2024"
tldr: "Proposes a stationary latent weight inference framework for online test-time adaptation to handle unreliable observations and distribution shifts."
---

# Stationary Latent Weight Inference for Unreliable Observations from Online Test-Time Adaptation

**Source**: [https://proceedings.mlr.press/v235/lee24b.html](https://proceedings.mlr.press/v235/lee24b.html)

**TLDR**: Proposes a stationary latent weight inference framework for online test-time adaptation to handle unreliable observations and distribution shifts.

## Abstract

In the rapidly evolving field of online test-time adaptation (OTTA), effectively managing distribution shifts is a pivotal concern. State-of-the-art OTTA methodologies often face limitations such as an inadequate target domain information integration, leading to significant issues like catastrophic forgetting and a lack of adaptability in dynamically changing environments. In this paper, we introduce a stationary latent weight inference (SLWI) framework, a novel approach to overcome these challenges. The proposed SLWI uniquely incorporates Bayesian filtering to continually track and update the target model weights along with the source model weight in online settings, thereby ensuring that the adapted model remains responsive to ongoing changes in the target domain. The proposed framework has the peculiar property to identify and backtrack nonlinear weights that exhibit local non-stationarity, thereby mitigating error propagation, a common pitfall of previous approaches. By integrating and refining information from both source and target domains, SLWI presents a robust solution to the persistent issue of domain adaptation in OTTA, significantly improving existing methodologies. The efficacy of SLWI is demonstrated through various experimental setups, showcasing its superior performance in diverse distribution shift scenarios.