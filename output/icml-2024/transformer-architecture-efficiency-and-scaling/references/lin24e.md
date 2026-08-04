---
title: "Can We Remove the Square-Root in Adaptive Gradient Methods? A Second-Order Perspective"
source: "https://proceedings.mlr.press/v235/lin24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24e/lin24e.pdf"
categories: ['optimization-algorithms-convergence-theory', 'transformer-architecture-efficiency-and-scaling']
tags: ['adaptive-gradient', 'Adam', 'second-order-optimization']
venue: "ICML 2024"
tldr: "A second-order perspective showing that the square-root operation in adaptive gradient methods like Adam can be removed for improved optimization."
---

# Can We Remove the Square-Root in Adaptive Gradient Methods? A Second-Order Perspective

**Source**: [https://proceedings.mlr.press/v235/lin24e.html](https://proceedings.mlr.press/v235/lin24e.html)

**TLDR**: A second-order perspective showing that the square-root operation in adaptive gradient methods like Adam can be removed for improved optimization.

## Abstract

Adaptive gradient optimizers like Adam(W) are the default training algorithms for many deep learning architectures, such as transformers. Their diagonal preconditioner is based on the gradient outer product which is incorporated into the parameter update via a square root. While these methods are often motivated as approximate second-order methods, the square root represents a fundamental difference. In this work, we investigate how the behavior of adaptive methods changes when we remove the root, i.e. strengthen their second-order motivation. Surprisingly, we find that such square-root-free adaptive methods close the generalization gap to SGD on convolutional architectures, while maintaining their root-based counterpart’s performance on transformers. The second-order perspective also has practical benefits for the development of non-diagonal adaptive methods through the concept of preconditioner invariance. In contrast to root-based methods like Shampoo, the root-free counterparts do not require numerically unstable matrix root decompositions and inversions, thus work well in half precision. Our findings provide new insights into the development of adaptive methods and raise important questions regarding the currently overlooked role of adaptivity for their success.