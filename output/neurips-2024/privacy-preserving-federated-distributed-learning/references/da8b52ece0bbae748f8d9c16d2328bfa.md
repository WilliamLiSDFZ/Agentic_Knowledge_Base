---
title: "Dimension-free Private Mean Estimation for Anisotropic Distributions"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/da8b52ece0bbae748f8d9c16d2328bfa-Abstract-Conference.html"
categories: ['privacy-preserving-federated-distributed-learning', 'statistical-computational-tradeoffs-high-dimensional-learning']
tags: ['differential-privacy', 'mean-estimation', 'high-dimensional']
venue: "NeurIPS 2024"
tldr: "Dimension-free differentially private algorithms for high-dimensional mean estimation that avoid the curse of dimensionality for anisotropic distributions."
---

# Dimension-free Private Mean Estimation for Anisotropic Distributions

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/da8b52ece0bbae748f8d9c16d2328bfa-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/da8b52ece0bbae748f8d9c16d2328bfa-Abstract-Conference.html)

**TLDR**: Dimension-free differentially private algorithms for high-dimensional mean estimation that avoid the curse of dimensionality for anisotropic distributions.

## Abstract

We present differentially private algorithms for high-dimensional mean estimation. Previous private estimators on distributions over $\mathbb{R}^d$ suffer from a curse of dimensionality, as they require $\Omega(d^{1/2})$ samples to achieve non-trivial error, even in cases where $O(1)$ samples suffice without privacy. This rate is  unavoidable when the distribution is isotropic, namely, when the covariance is a multiple of the identity matrix. Yet, real-world data is often highly anisotropic, with signals concentrated on a small number of principal components. We develop estimators that are appropriate for such signals---our estimators are $(\varepsilon,\delta)$-differentially private and have sample complexity that is dimension-independent for anisotropic subgaussian distributions.  Given $n$ samples from a distribution with known covariance-proxy $\Sigma$ and unknown mean $\mu$, we present an estimator $\hat{\mu}$ that achieves error, $\|\hat{\mu}-\mu\|_2\leq \alpha$, as long as $n\gtrsim \text{tr}(\Sigma)/\alpha^2+ \text{tr}(\Sigma^{1/2})/(\alpha\varepsilon)$. We show that this is the optimal sample complexity for this task up to logarithmic factors. Moreover, for the case of unknown covariance, we present an algorithm whose sample complexity has improved dependence on the dimension, from $d^{1/2}$ to $d^{1/4}$.