---
title: "Distributed Bilevel Optimization with Communication Compression"
source: "https://proceedings.mlr.press/v235/he24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/he24d/he24d.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'optimization-algorithms-convergence-theory']
tags: ['bilevel-optimization', 'distributed-learning', 'communication-compression']
venue: "ICML 2024"
tldr: "A communication-compressed distributed bilevel optimization algorithm is proposed to reduce communication overhead in large-scale nested optimization."
---

# Distributed Bilevel Optimization with Communication Compression

**Source**: [https://proceedings.mlr.press/v235/he24d.html](https://proceedings.mlr.press/v235/he24d.html)

**TLDR**: A communication-compressed distributed bilevel optimization algorithm is proposed to reduce communication overhead in large-scale nested optimization.

## Abstract

Stochastic bilevel optimization tackles challenges involving nested optimization structures. Its fast-growing scale nowadays necessitates efficient distributed algorithms. In conventional distributed bilevel methods, each worker must transmit full-dimensional stochastic gradients to the server every iteration, leading to significant communication overhead and thus hindering efficiency and scalability. To resolve this issue, we introduce the first family of distributed bilevel algorithms with communication compression. The primary challenge in algorithmic development is mitigating bias in hypergradient estimation caused by the nested structure. We first propose C-SOBA, a simple yet effective approach with unbiased compression and provable linear speedup convergence. However, it relies on strong assumptions on bounded gradients. To address this limitation, we explore the use of moving average, error feedback, and multi-step compression in bilevel optimization, resulting in a series of advanced algorithms with relaxed assumptions and improved convergence properties. Numerical experiments show that our compressed bilevel algorithms can achieve $10\times$ reduction in communication overhead without severe performance degradation.