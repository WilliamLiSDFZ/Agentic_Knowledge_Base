---
title: "Stereographic Spherical Sliced Wasserstein Distances"
source: "https://proceedings.mlr.press/v235/tran24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tran24a/tran24a.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'sampling-and-optimization-on-manifolds']
tags: ['spherical-distributions', 'Wasserstein-distance', 'sliced-optimal-transport']
venue: "ICML 2024"
tldr: "Introduces stereographic spherical sliced Wasserstein distances for efficient comparison of spherical probability distributions."
---

# Stereographic Spherical Sliced Wasserstein Distances

**Source**: [https://proceedings.mlr.press/v235/tran24a.html](https://proceedings.mlr.press/v235/tran24a.html)

**TLDR**: Introduces stereographic spherical sliced Wasserstein distances for efficient comparison of spherical probability distributions.

## Abstract

Comparing spherical probability distributions is of great interest in various fields, including geology, medical domains, computer vision, and deep representation learning. The utility of optimal transport-based distances, such as the Wasserstein distance, for comparing probability measures has spurred active research in developing computationally efficient variations of these distances for spherical probability measures. This paper introduces a high-speed and highly parallelizable distance for comparing spherical measures using the stereographic projection and the generalized Radon transform, which we refer to as the Stereographic Spherical Sliced Wasserstein (S3W) distance. We carefully address the distance distortion caused by the stereographic projection and provide an extensive theoretical analysis of our proposed metric and its rotationally invariant variation. Finally, we evaluate the performance of the proposed metrics and compare them with recent baselines in terms of both speed and accuracy through a wide range of numerical studies, including gradient flows and self-supervised learning. Our code is available at https://github.com/mint-vu/s3wd.