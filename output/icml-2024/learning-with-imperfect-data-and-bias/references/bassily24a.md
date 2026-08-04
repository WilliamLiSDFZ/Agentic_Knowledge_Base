---
title: "Differentially Private Domain Adaptation with Theoretical Guarantees"
source: "https://proceedings.mlr.press/v235/bassily24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bassily24a/bassily24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'learning-with-imperfect-data-and-bias']
tags: ['differential-privacy', 'domain-adaptation', 'theoretical-guarantees', 'federated-learning', 'transfer-learning']
venue: "ICML 2024"
tldr: "Develops differentially private domain adaptation algorithms with theoretical guarantees for settings with limited private labeled data."
---

# Differentially Private Domain Adaptation with Theoretical Guarantees

**Source**: [https://proceedings.mlr.press/v235/bassily24a.html](https://proceedings.mlr.press/v235/bassily24a.html)

**TLDR**: Develops differentially private domain adaptation algorithms with theoretical guarantees for settings with limited private labeled data.

## Abstract

In many applications, the labeled data at the learner’s disposal is subject to privacy constraints and is relatively limited. To derive a more accurate predictor for the target domain, it is often beneficial to leverage publicly available labeled data from an alternative domain, somewhat close to the target domain. This is the modern problem of supervised domain adaptation from a public source to a private target domain. We present two $(\epsilon, \delta)$-differentially private adaptation algorithms for supervised adaptation, for which we make use of a general optimization problem, recently shown to benefit from favorable theoretical learning guarantees. Our first algorithm is designed for regression with linear predictors and shown to solve a convex optimization problem. Our second algorithm is a more general solution for loss functions that may be non-convex but Lipschitz and smooth. While our main objective is a theoretical analysis, we also report the results of several experiments. We first show that the non-private versions of our algorithms match state-of-the-art performance in supervised adaptation and that for larger values of the target sample size or $\epsilon$, the performance of our private algorithms remains close to that of their non-private counterparts.