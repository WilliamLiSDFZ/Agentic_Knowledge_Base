---
title: "Parallel Affine Transformation Tuning of Markov Chain Monte Carlo"
source: "https://proceedings.mlr.press/v235/schar24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/schar24a/schar24a.pdf"
categories: ['sampling-and-optimization-on-manifolds', 'sampling-compression-and-dimensionality-reduction']
tags: ['MCMC', 'affine-transformations', 'preconditioning', 'sampling', 'covariance-adaptation']
venue: "ICML 2024"
tldr: "Bijective affine transformations of the sample space are used to improve MCMC sampler performance by adapting to the target distribution's geometry."
---

# Parallel Affine Transformation Tuning of Markov Chain Monte Carlo

**Source**: [https://proceedings.mlr.press/v235/schar24a.html](https://proceedings.mlr.press/v235/schar24a.html)

**TLDR**: Bijective affine transformations of the sample space are used to improve MCMC sampler performance by adapting to the target distribution's geometry.

## Abstract

The performance of Markov chain Monte Carlo samplers strongly depends on the properties of the target distribution such as its covariance structure, the location of its probability mass and its tail behavior. We explore the use of bijective affine transformations of the sample space to improve the properties of the target distribution and thereby the performance of samplers running in the transformed space. In particular, we propose a flexible and user-friendly scheme for adaptively learning the affine transformation during sampling. Moreover, the combination of our scheme with Gibbsian polar slice sampling is shown to produce samples of high quality at comparatively low computational cost in several settings based on real-world data.