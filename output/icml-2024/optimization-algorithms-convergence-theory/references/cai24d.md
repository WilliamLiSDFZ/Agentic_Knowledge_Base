---
title: "Batch and match: black-box variational inference with a score-based divergence"
source: "https://proceedings.mlr.press/v235/cai24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cai24d/cai24d.pdf"
categories: ['generative-models-and-variational-inference', 'optimization-algorithms-convergence-theory']
tags: ['variational-inference', 'black-box-VI', 'score-based-divergence', 'ELBO']
venue: "ICML 2024"
tldr: "Introduces a batch-and-match BBVI method using a score-based divergence that converges faster and is less sensitive to hyperparameters than ELBO-based approaches."
---

# Batch and match: black-box variational inference with a score-based divergence

**Source**: [https://proceedings.mlr.press/v235/cai24d.html](https://proceedings.mlr.press/v235/cai24d.html)

**TLDR**: Introduces a batch-and-match BBVI method using a score-based divergence that converges faster and is less sensitive to hyperparameters than ELBO-based approaches.

## Abstract

Most leading implementations of black-box variational inference (BBVI) are based on optimizing a stochastic evidence lower bound (ELBO). But such approaches to BBVI often converge slowly due to the high variance of their gradient estimates and their sensitivity to hyperparameters. In this work, we propose batch and match (BaM), an alternative approach to BBVI based on a score-based divergence. Notably, this score-based divergence can be optimized by a closed-form proximal update for Gaussian variational families with full covariance matrices. We analyze the convergence of BaM when the target distribution is Gaussian, and we prove that in the limit of infinite batch size the variational parameter updates converge exponentially quickly to the target mean and covariance. We also evaluate the performance of BaM on Gaussian and non-Gaussian target distributions that arise from posterior inference in hierarchical and deep generative models. In these experiments, we find that BaM typically converges in fewer (and sometimes significantly fewer) gradient evaluations than leading implementations of BBVI based on ELBO maximization.