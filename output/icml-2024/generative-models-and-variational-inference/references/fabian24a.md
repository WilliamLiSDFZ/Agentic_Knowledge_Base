---
title: "Adapt and Diffuse: Sample-adaptive Reconstruction via Latent Diffusion Models"
source: "https://proceedings.mlr.press/v235/fabian24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fabian24a/fabian24a.pdf"
categories: ['generative-models-and-variational-inference', 'image-quality-assessment-and-super-resolution']
tags: ['inverse-problems', 'latent-diffusion', 'sample-adaptive', 'image-reconstruction', 'posterior-sampling']
venue: "ICML 2024"
tldr: "Proposes a sample-adaptive reconstruction framework using latent diffusion models that adjusts reconstruction strength to per-sample degradation severity."
---

# Adapt and Diffuse: Sample-adaptive Reconstruction via Latent Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/fabian24a.html](https://proceedings.mlr.press/v235/fabian24a.html)

**TLDR**: Proposes a sample-adaptive reconstruction framework using latent diffusion models that adjusts reconstruction strength to per-sample degradation severity.

## Abstract

Inverse problems arise in a multitude of applications, where the goal is to recover a clean signal from noisy and possibly (non)linear observations. The difficulty of a reconstruction problem depends on multiple factors, such as the ground truth signal structure, the severity of the degradation and the complex interactions between the above. This results in natural sample-by-sample variation in the difficulty of a reconstruction problem. Our key observation is that most existing inverse problem solvers lack the ability to adapt their compute power to the difficulty of the reconstruction task, resulting in subpar performance and wasteful resource allocation. We propose a novel method, severity encoding, to estimate the degradation severity of corrupted signals in the latent space of an autoencoder. We show that the estimated severity has strong correlation with the true corruption level and can provide useful hints on the difficulty of reconstruction problems on a sample-by-sample basis. Furthermore, we propose a reconstruction method based on latent diffusion models that leverages the predicted degradation severities to fine-tune the reverse diffusion sampling trajectory and thus achieve sample-adaptive inference times. Our framework, Flash-Diffusion, acts as a wrapper that can be combined with any latent diffusion-based baseline solver, imbuing it with sample-adaptivity and acceleration. We perform experiments on both linear and nonlinear inverse problems and demonstrate that our technique greatly improves the performance of the baseline solver and achieves up to $10\times$ acceleration in mean sampling speed.