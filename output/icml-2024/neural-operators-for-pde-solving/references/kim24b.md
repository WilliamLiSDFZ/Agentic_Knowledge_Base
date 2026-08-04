---
title: "Gaussian Plane-Wave Neural Operator for Electron Density Estimation"
source: "https://proceedings.mlr.press/v235/kim24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24b/kim24b.pdf"
categories: ['neural-operators-for-pde-solving', 'generative-models-for-molecular-protein-design']
tags: ['neural-operators', 'electron-density', 'quantum-chemistry']
venue: "ICML 2024"
tldr: "Introduces the Gaussian plane-wave neural operator for electron density prediction in chemical systems using infinite-dimensional functional space operations."
---

# Gaussian Plane-Wave Neural Operator for Electron Density Estimation

**Source**: [https://proceedings.mlr.press/v235/kim24b.html](https://proceedings.mlr.press/v235/kim24b.html)

**TLDR**: Introduces the Gaussian plane-wave neural operator for electron density prediction in chemical systems using infinite-dimensional functional space operations.

## Abstract

This work studies machine learning for electron density prediction, which is fundamental for understanding chemical systems and density functional theory (DFT) simulations. To this end, we introduce the Gaussian plane-wave neural operator (GPWNO), which operates in the infinite-dimensional functional space using the plane-wave and Gaussian-type orbital bases, widely recognized in the context of DFT. In particular, both high- and low-frequency components of the density can be effectively represented due to the complementary nature of the two bases. Extensive experiments on QM9, MD, and material project datasets demonstrate GPWNO’s superior performance over ten baselines.