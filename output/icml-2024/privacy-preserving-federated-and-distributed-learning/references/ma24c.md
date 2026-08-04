---
title: "Better Locally Private Sparse Estimation Given Multiple Samples Per User"
source: "https://proceedings.mlr.press/v235/ma24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24c/ma24c.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['local-differential-privacy', 'sparse-estimation', 'linear-regression', 'minimax-rates']
venue: "ICML 2024"
tldr: "New algorithms achieve improved minimax rates for locally private sparse linear regression when multiple samples per user are available."
---

# Better Locally Private Sparse Estimation Given Multiple Samples Per User

**Source**: [https://proceedings.mlr.press/v235/ma24c.html](https://proceedings.mlr.press/v235/ma24c.html)

**TLDR**: New algorithms achieve improved minimax rates for locally private sparse linear regression when multiple samples per user are available.

## Abstract

Previous studies yielded discouraging results for item-level locally differentially private linear regression with $s$-sparsity assumption, where the minimax rate for $nm$ samples is $\mathcal{O}(sd / nm\varepsilon^2)$. This can be challenging for high-dimensional data, where the dimension $d$ is extremely large. In this work, we investigate user-level locally differentially private sparse linear regression. We show that with $n$ users each contributing $m$ samples, the linear dependency of dimension $d$ can be eliminated, yielding an error upper bound of $\mathcal{O}(s/ nm\varepsilon^2)$. We propose a framework that first selects candidate variables and then conducts estimation in the narrowed low-dimensional space, which is extendable to general sparse estimation problems with tight error bounds. Experiments on both synthetic and real datasets demonstrate the superiority of the proposed methods. Both the theoretical and empirical results suggest that, with the same number of samples, locally private sparse estimation is better conducted when multiple samples per user are available.