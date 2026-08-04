---
title: "Interpreting and Improving Diffusion Models from an Optimization Perspective"
source: "https://proceedings.mlr.press/v235/permenter24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/permenter24a/permenter24a.pdf"
categories: ['generative-models-and-variational-inference', 'optimization-algorithms-convergence-theory']
tags: ['diffusion-models', 'denoising', 'manifold-hypothesis', 'optimization', 'projection']
venue: "ICML 2024"
tldr: "Interprets diffusion model denoising as approximate projection onto a data manifold and uses this perspective to improve sampling and training."
---

# Interpreting and Improving Diffusion Models from an Optimization Perspective

**Source**: [https://proceedings.mlr.press/v235/permenter24a.html](https://proceedings.mlr.press/v235/permenter24a.html)

**TLDR**: Interprets diffusion model denoising as approximate projection onto a data manifold and uses this perspective to improve sampling and training.

## Abstract

Denoising is intuitively related to projection. Indeed, under the manifold hypothesis, adding random noise is approximately equivalent to orthogonal perturbation. Hence, learning to denoise is approximately learning to project. In this paper, we use this observation to interpret denoising diffusion models as approximate gradient descent applied to the Euclidean distance function. We then provide straight-forward convergence analysis of the DDIM sampler under simple assumptions on the projection error of the denoiser. Finally, we propose a new gradient-estimation sampler, generalizing DDIM using insights from our theoretical results. In as few as 5-10 function evaluations, our sampler achieves state-of-the-art FID scores on pretrained CIFAR-10 and CelebA models and can generate high quality samples on latent diffusion models.