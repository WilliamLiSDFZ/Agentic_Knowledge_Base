---
title: "Deep Equilibrium Models are Almost Equivalent to Not-so-deep Explicit Models for High-dimensional Gaussian Mixtures"
source: "https://proceedings.mlr.press/v235/ling24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ling24a/ling24a.pdf"
categories: ['neural-network-learning-dynamics-theory']
tags: ['deep-equilibrium-models', 'implicit-networks', 'gaussian-mixtures']
venue: "ICML 2024"
tldr: "This paper theoretically shows that deep equilibrium models are nearly equivalent to shallow explicit networks for high-dimensional Gaussian mixture tasks."
---

# Deep Equilibrium Models are Almost Equivalent to Not-so-deep Explicit Models for High-dimensional Gaussian Mixtures

**Source**: [https://proceedings.mlr.press/v235/ling24a.html](https://proceedings.mlr.press/v235/ling24a.html)

**TLDR**: This paper theoretically shows that deep equilibrium models are nearly equivalent to shallow explicit networks for high-dimensional Gaussian mixture tasks.

## Abstract

Deep equilibrium models (DEQs), as typical implicit neural networks, have demonstrated remarkable success on various tasks. There is, however, a lack of theoretical understanding of the connections and differences between implicit DEQs and explicit neural network models. In this paper, leveraging recent advances in random matrix theory (RMT), we perform an in-depth analysis on the eigenspectra of the conjugate kernel (CK) and neural tangent kernel (NTK) matrices for implicit DEQs, when the input data are drawn from a high-dimensional Gaussia mixture. We prove that, in this setting, the spectral behavior of these Implicit-CKs and NTKs depend on the DEQ activation function and initial weight variances, but only via a system of four nonlinear equations. As a direct consequence of this theoretical result, we demonstrate that a shallow explicit network can be carefully designed to produce the same CK or NTK as a given DEQ. Despite derived here for Gaussian mixture data, empirical results show the proposed theory and design principles also apply to popular real-world datasets.