---
title: "I/O Complexity of Attention, or How Optimal is FlashAttention?"
source: "https://proceedings.mlr.press/v235/saha24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/saha24a/saha24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'fast-sketching-methods-for-large-scale-optimization']
tags: ['FlashAttention', 'I/O-complexity', 'attention-mechanism', 'memory-hierarchy', 'transformers']
venue: "ICML 2024"
tldr: "Theoretical I/O complexity bounds for attention are derived, showing FlashAttention is near-optimal and establishing tight lower bounds for memory-efficient attention."
---

# I/O Complexity of Attention, or How Optimal is FlashAttention?

**Source**: [https://proceedings.mlr.press/v235/saha24a.html](https://proceedings.mlr.press/v235/saha24a.html)

**TLDR**: Theoretical I/O complexity bounds for attention are derived, showing FlashAttention is near-optimal and establishing tight lower bounds for memory-efficient attention.

## Abstract

Attention is at the heart of the popular Transformer architecture, yet suffers from quadratic time and memory complexity. In a recent significant development, FlashAttention shows that the I/O complexity of attention is the true bottleneck in scaling Transformers. Given two levels of memory hierarchy, a fast cache (e.g. GPU on-chip SRAM) where computation happens and a slow memory (e.g. GPU high-bandwidth memory) where the data resides, the I/O complexity measures the number of accesses to the slow memory. FlashAttention is an I/O-aware algorithm for self-attention that requires $\frac{N^2d^2}{M}$ I/O operations where $N$ is the dimension of the attention matrix, $d$ is the head-dimension and $M$ is the size of cache. Naturally, to further reduce the computational costs of Attention, the authors ask the question: is FlashAttention’s I/O complexity optimal for every value of $M$? We resolve the above question in its full generality by showing an I/O complexity lower bound that matches the upper bound provided by FlashAttention for any values of $M \geq d^2$ within any constant factors. Moreover, our lower bounds do not rely on using combinatorial matrix multiplication for computing the attention matrix: even if one uses fast matrix multiplication, the above I/O complexity bounds cannot be improved. Further, we give a better algorithm with lower I/O complexity for $M < d^2$, and show that it is optimal for combinatorial algorithms. We do so by introducing a new communication complexity protocol for matrix compression, and connecting communication complexity to I/O complexity. We believe this connection could be of independent interest and will find more applications in proving I/O complexity lower bounds in future.