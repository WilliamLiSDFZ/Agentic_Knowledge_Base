---
title: "Generative Modeling on Manifolds Through Mixture of Riemannian Diffusion Processes"
source: "https://proceedings.mlr.press/v235/jo24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jo24a/jo24a.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-and-optimization-on-manifolds']
tags: ['riemannian-manifolds', 'diffusion-models', 'mixture-of-processes', 'generative-modeling']
venue: "ICML 2024"
tldr: "A mixture of Riemannian diffusion processes enables tractable generative modeling on manifolds without expensive divergence computation."
---

# Generative Modeling on Manifolds Through Mixture of Riemannian Diffusion Processes

**Source**: [https://proceedings.mlr.press/v235/jo24a.html](https://proceedings.mlr.press/v235/jo24a.html)

**TLDR**: A mixture of Riemannian diffusion processes enables tractable generative modeling on manifolds without expensive divergence computation.

## Abstract

Learning the distribution of data on Riemannian manifolds is crucial for modeling data from non-Euclidean space, which is required by many applications in diverse scientific fields. Yet, existing generative models on manifolds suffer from expensive divergence computation or rely on approximations of heat kernel. These limitations restrict their applicability to simple geometries and hinder scalability to high dimensions. In this work, we introduce the Riemannian Diffusion Mixture, a principled framework for building a generative diffusion process on manifolds. Instead of following the denoising approach of previous diffusion models, we construct a diffusion process using a mixture of bridge processes derived on general manifolds without requiring heat kernel estimations. We develop a geometric understanding of the mixture process, deriving the drift as a weighted mean of tangent directions to the data points that guides the process toward the data distribution. We further propose a scalable training objective for learning the mixture process that readily applies to general manifolds. Our method achieves superior performance on diverse manifolds with dramatically reduced number of in-training simulation steps for general manifolds.