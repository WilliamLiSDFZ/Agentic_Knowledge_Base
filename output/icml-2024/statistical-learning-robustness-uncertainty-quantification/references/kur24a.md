---
title: "Minimum Norm Interpolation Meets The Local Theory of Banach Spaces"
source: "https://proceedings.mlr.press/v235/kur24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kur24a/kur24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'neural-network-learning-dynamics-theory']
tags: ['minimum-norm-interpolation', 'double-descent', 'banach-spaces', 'generalization']
venue: "ICML 2024"
tldr: "Analysis of minimum-norm interpolation beyond Hilbert spaces using local Banach space theory to understand double descent phenomena."
---

# Minimum Norm Interpolation Meets The Local Theory of Banach Spaces

**Source**: [https://proceedings.mlr.press/v235/kur24a.html](https://proceedings.mlr.press/v235/kur24a.html)

**TLDR**: Analysis of minimum-norm interpolation beyond Hilbert spaces using local Banach space theory to understand double descent phenomena.

## Abstract

Minimum-norm interpolators have recently gained attention primarily as an analyzable model to shed light on the double descent phenomenon observed for neural networks. The majority of the work has focused on analyzing interpolators in Hilbert spaces, where typically an effectively low-rank structure of the feature covariance prevents a large bias. More recently, tight vanishing bounds have also been shown for isotropic high-dimensional data for $\ell_p$-spaces with $p\in[1,2)$, leveraging sparse structure of the ground truth. However, these proofs are tailored to specific settings and hard to generalize. This paper takes a first step towards establishing a general framework that connects generalization properties of the interpolators to well-known concepts from high-dimensional geometry, specifically, from the local theory of Banach spaces. In particular, we show that under $2$-uniform convexity, the bias of the minimal norm solution is bounded by the Gaussian complexity of the class. We then prove a “reverse” Efron-Stein lower bound on the expected conditional variance of the minimal norm solution under cotype $2$. Finally, we prove that this bound is sharp for $\ell_p$-linear regression under sub-Gaussian covariates.