---
title: "Diffusion Models Encode the Intrinsic Dimension of Data Manifolds"
source: "https://proceedings.mlr.press/v235/stanczuk24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/stanczuk24a/stanczuk24a.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-compression-and-dimensionality-reduction']
tags: ['diffusion-models', 'intrinsic-dimension', 'data-manifolds', 'normal-bundles']
venue: "ICML 2024"
tldr: "A mathematical proof shows diffusion models encode data manifolds via normal bundle approximation, enabling intrinsic dimension estimation from trained models."
---

# Diffusion Models Encode the Intrinsic Dimension of Data Manifolds

**Source**: [https://proceedings.mlr.press/v235/stanczuk24a.html](https://proceedings.mlr.press/v235/stanczuk24a.html)

**TLDR**: A mathematical proof shows diffusion models encode data manifolds via normal bundle approximation, enabling intrinsic dimension estimation from trained models.

## Abstract

In this work, we provide a mathematical proof that diffusion models encode data manifolds by approximating their normal bundles. Based on this observation we propose a novel method for extracting the intrinsic dimension of the data manifold from a trained diffusion model. Our insights are based on the fact that a diffusion model approximates the score function i.e. the gradient of the log density of a noise-corrupted version of the target distribution for varying levels of corruption. We prove that as the level of corruption decreases, the score function points towards the manifold, as this direction becomes the direction of maximal likelihood increase. Therefore, at low noise levels, the diffusion model provides us with an approximation of the manifold’s normal bundle, allowing for an estimation of the manifold’s intrinsic dimension. To the best of our knowledge our method is the first estimator of intrinsic dimension based on diffusion models and it outperforms well established estimators in controlled experiments on both Euclidean and image data.