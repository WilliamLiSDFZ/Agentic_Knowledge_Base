---
title: "Enabling Uncertainty Estimation in Iterative Neural Networks"
source: "https://proceedings.mlr.press/v235/durasov24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/durasov24a/durasov24a.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['uncertainty-estimation', 'iterative-networks', 'convergence-rate', 'fixed-point-iteration', 'epistemic-uncertainty']
venue: "ICML 2024"
tldr: "Shows that convergence rates of iterative neural networks' successive outputs correlate strongly with prediction error, enabling uncertainty estimation without extra cost."
---

# Enabling Uncertainty Estimation in Iterative Neural Networks

**Source**: [https://proceedings.mlr.press/v235/durasov24a.html](https://proceedings.mlr.press/v235/durasov24a.html)

**TLDR**: Shows that convergence rates of iterative neural networks' successive outputs correlate strongly with prediction error, enabling uncertainty estimation without extra cost.

## Abstract

Turning pass-through network architectures into iterative ones, which use their own output as input, is a well-known approach for boosting performance. In this paper, we argue that such architectures offer an additional benefit: The convergence rate of their successive outputs is highly correlated with the accuracy of the value to which they converge. Thus, we can use the convergence rate as a useful proxy for uncertainty. This results in an approach to uncertainty estimation that provides state-of-the-art estimates at a much lower computational cost than techniques like Ensembles, and without requiring any modifications to the original iterative model. We demonstrate its practical value by embedding it in two application domains: road detection in aerial images and the estimation of aerodynamic properties of 2D and 3D shapes.