---
title: "Geometry-Calibrated DRO: Combating Over-Pessimism with Free Energy Implications"
source: "https://proceedings.mlr.press/v235/liu24br.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24br/liu24br.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['distributionally-robust-optimization', 'over-pessimism', 'free-energy', 'uncertainty-set', 'distributional-shift']
venue: "ICML 2024"
tldr: "Geometry-Calibrated DRO combats over-pessimism in distributionally robust optimization using free energy implications and geometric calibration of uncertainty sets."
---

# Geometry-Calibrated DRO: Combating Over-Pessimism with Free Energy Implications

**Source**: [https://proceedings.mlr.press/v235/liu24br.html](https://proceedings.mlr.press/v235/liu24br.html)

**TLDR**: Geometry-Calibrated DRO combats over-pessimism in distributionally robust optimization using free energy implications and geometric calibration of uncertainty sets.

## Abstract

Machine learning algorithms minimizing average risk are susceptible to distributional shifts. Distributionally Robust Optimization (DRO) addresses this issue by optimizing the worst-case risk within an uncertainty set. However, DRO suffers from over-pessimism, leading to low-confidence predictions, poor parameter estimations as well as poor generalization. In this work, we conduct a theoretical analysis of a probable root cause of over-pessimism: excessive focus on noisy samples. To alleviate the impact of noise, we incorporate data geometry into calibration terms in DRO, resulting in our novel Geometry-Calibrated DRO (GCDRO) for regression. We establish the connection between our risk objective and the Helmholtz free energy in statistical physics, and this free-energy-based risk can extend to standard DRO methods. Leveraging gradient flow in Wasserstein space, we develop an approximate minimax optimization algorithm with a bounded error ratio and elucidate how our approach mitigates noisy sample effects. Comprehensive experiments confirm GCDRO’s superiority over conventional DRO methods.