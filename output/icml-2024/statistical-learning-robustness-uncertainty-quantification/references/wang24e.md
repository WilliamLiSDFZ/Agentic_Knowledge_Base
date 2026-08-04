---
title: "Towards Theoretical Understanding of Learning Large-scale Dependent Data via Random Features"
source: "https://proceedings.mlr.press/v235/wang24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24e/wang24e.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'sampling-compression-and-dimensionality-reduction']
tags: ['random-features', 'nonparametric-regression', 'dependent-data', 'generalization-theory', 'kernel-methods']
venue: "ICML 2024"
tldr: "This paper provides theoretical guarantees for random feature methods applied to large-scale nonparametric regression with dependent (non-i.i.d.) data."
---

# Towards Theoretical Understanding of Learning Large-scale Dependent Data via Random Features

**Source**: [https://proceedings.mlr.press/v235/wang24e.html](https://proceedings.mlr.press/v235/wang24e.html)

**TLDR**: This paper provides theoretical guarantees for random feature methods applied to large-scale nonparametric regression with dependent (non-i.i.d.) data.

## Abstract

Random feature (RF) mapping is an attractive and powerful technique for solving large-scale nonparametric regression. Yet, the existing theoretical analysis crucially relies on the i.i.d. assumption that individuals in the data are independent and identically distributed. It is still unclear whether learning accuracy would be compromised when the i.i.d. assumption is violated. This paper aims to provide theoretical understanding of the kernel ridge regression (KRR) with RFs for large-scale dependent data. Specifically, we consider two types of data dependence structure, namely, the $\tau$-mixing process with exponential decay coefficient, and that with polynomial decay coefficient. Theoretically, we prove that the kernel ridge estimator with RFs achieves the minimax optimality under the exponential decay scenario, but yields a sub-optimal result under the polynomial decay case. Our analysis further reveals how the decay rate of the $\tau$-mixing coefficient impacts the learning accuracy of the kernel ridge estimator with RFs. Extensive numerical experiments on both synthetic and real examples further validate our theoretical findings and support the effectiveness of the KRR with RFs in dealing with dependent data.