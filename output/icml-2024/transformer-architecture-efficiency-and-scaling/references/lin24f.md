---
title: "Structured Inverse-Free Natural Gradient Descent: Memory-Efficient & Numerically-Stable KFAC"
source: "https://proceedings.mlr.press/v235/lin24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24f/lin24f.pdf"
categories: ['optimization-algorithms-convergence-theory', 'transformer-architecture-efficiency-and-scaling']
tags: ['natural-gradient', 'KFAC', 'memory-efficiency']
venue: "ICML 2024"
tldr: "A structured inverse-free natural gradient method that improves memory efficiency and numerical stability over standard KFAC."
---

# Structured Inverse-Free Natural Gradient Descent: Memory-Efficient & Numerically-Stable KFAC

**Source**: [https://proceedings.mlr.press/v235/lin24f.html](https://proceedings.mlr.press/v235/lin24f.html)

**TLDR**: A structured inverse-free natural gradient method that improves memory efficiency and numerical stability over standard KFAC.

## Abstract

Second-order methods such as KFAC can be useful for neural net training. However, they are often memory-inefficient since their preconditioning Kronecker factors are dense, and numerically unstable in low precision as they require matrix inversion or decomposition. These limitations render such methods unpopular for modern mixed-precision training. We address them by (i) formulating an inverse-free KFAC update and (ii) imposing structures in the Kronecker factors, resulting in structured inverse-free natural gradient descent (SINGD). On modern neural networks, we show that SINGD is memory-efficient and numerically robust, in contrast to KFAC, and often outperforms AdamW even in half precision. Our work closes a gap between first- and second-order methods in modern low-precision training.