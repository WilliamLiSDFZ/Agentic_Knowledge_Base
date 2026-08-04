---
title: "CW Complex Hypothesis for Image Data"
source: "https://proceedings.mlr.press/v235/wang24bs.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24bs/wang24bs.pdf"
categories: ['topological-deep-learning-persistent-homology', 'sampling-compression-and-dimensionality-reduction']
tags: ['CW-complex', 'manifold-hypothesis', 'intrinsic-dimension', 'topological-data-analysis']
venue: "ICML 2024"
tldr: "Proposes a CW complex hypothesis as an alternative to the manifold hypothesis, accommodating varying local intrinsic dimensions across image data."
---

# CW Complex Hypothesis for Image Data

**Source**: [https://proceedings.mlr.press/v235/wang24bs.html](https://proceedings.mlr.press/v235/wang24bs.html)

**TLDR**: Proposes a CW complex hypothesis as an alternative to the manifold hypothesis, accommodating varying local intrinsic dimensions across image data.

## Abstract

We examine both the manifold hypothesis (Bengio et al., 2013) and the union of manifold hypothesis (Brown et al., 2023), and argue that, in contrast to these hypotheses, the local intrinsic dimension varies from point to point even in the same connected component. We propose an alternative CW complex hypothesis that image data is distributed in “manifolds with skeletons". We support the hypothesis through visualization of distributions of image data of random geometric objects, as well as by introducing and testing a criterion on natural image datasets. One motivation of our work is to explain why diffusion models have difficulty generating accurate higher dimensional details such as human hands. Under the CW complex hypothesis and with both theoretical and empirical evidences, we provide an interpretation that the mixture of higher and lower dimensional components in data obstructs diffusion models from efficient learning.