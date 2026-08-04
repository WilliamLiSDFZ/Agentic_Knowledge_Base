---
title: "Can Gaussian Sketching Converge Faster on a Preconditioned Landscape?"
source: "https://proceedings.mlr.press/v235/wang24ch.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24ch/wang24ch.pdf"
categories: ['fast-sketching-methods-for-large-scale-optimization']
tags: ['gaussian-sketching', 'preconditioning', 'coordinate-descent']
venue: "ICML 2024"
tldr: "This paper analyzes whether Gaussian sketching-based gradient methods can achieve faster convergence on preconditioned optimization landscapes."
---

# Can Gaussian Sketching Converge Faster on a Preconditioned Landscape?

**Source**: [https://proceedings.mlr.press/v235/wang24ch.html](https://proceedings.mlr.press/v235/wang24ch.html)

**TLDR**: This paper analyzes whether Gaussian sketching-based gradient methods can achieve faster convergence on preconditioned optimization landscapes.

## Abstract

This paper focuses on the large-scale optimization which is very popular in the big data era. The gradient sketching is an important technique in the large-scale optimization. Specifically, the random coordinate descent algorithm is a kind of gradient sketching method with the random sampling matrix as the sketching matrix. In this paper, we propose a novel gradient sketching called GSGD (Gaussian Sketched Gradient Descent). Compared with the classical gradient sketching methods such as the random coordinate descent and SEGA (Hanzely et al., 2018), our GSGD does not require the importance sampling but can achieve a fast convergence rate matching the ones of these methods with importance sampling. Furthermore, if the objective function has a non-smooth regularization term, our GSGD can also exploit the implicit structure information of the regularization term to achieve a fast convergence rate. Finally, our experimental results substantiate the effectiveness and efficiency of our algorithm.