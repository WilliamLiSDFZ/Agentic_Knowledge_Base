---
title: "Prior Mismatch and Adaptation in PnP-ADMM with a Nonconvex Convergence Analysis"
source: "https://proceedings.mlr.press/v235/shoushtari24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shoushtari24a/shoushtari24a.pdf"
categories: ['generative-models-and-variational-inference', 'optimization-algorithms-convergence-theory']
tags: ['plug-and-play-priors', 'ADMM', 'nonconvex-optimization']
venue: "ICML 2024"
tldr: "Analyzes prior mismatch in PnP-ADMM methods and provides a nonconvex convergence analysis for imaging inverse problems."
---

# Prior Mismatch and Adaptation in PnP-ADMM with a Nonconvex Convergence Analysis

**Source**: [https://proceedings.mlr.press/v235/shoushtari24a.html](https://proceedings.mlr.press/v235/shoushtari24a.html)

**TLDR**: Analyzes prior mismatch in PnP-ADMM methods and provides a nonconvex convergence analysis for imaging inverse problems.

## Abstract

Plug-and-Play (PnP) priors is a widely-used family of methods for solving imaging inverse problems by integrating physical measurement models with image priors specified using image denoisers. PnP methods have been shown to achieve state-of-the-art performance when the prior is obtained using powerful deep denoisers. Despite extensive work on PnP, the topic of distribution mismatch between the training and testing data has often been overlooked in the PnP literature. This paper presents a set of new theoretical and numerical results on the topic of prior distribution mismatch and domain adaptation for the alternating direction method of multipliers (ADMM) variant of PnP. Our theoretical result provides an explicit error bound for PnP-ADMM due to the mismatch between the desired denoiser and the one used for inference. Our analysis contributes to the work in the area by considering the mismatch under nonconvex data-fidelity terms and expansive denoisers. Our first set of numerical results quantifies the impact of the prior distribution mismatch on the performance of PnP-ADMM on the problem of image super-resolution. Our second set of numerical results considers a simple and effective domain adaption strategy that closes the performance gap due to the use of mismatched denoisers. Our results suggest the relative robustness of PnP-ADMM to prior distribution mismatch, while also showing that the performance gap can be significantly reduced with only a few training samples from the desired distribution.