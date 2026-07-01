---
title: "Adaptive Variance Reduction for Stochastic Optimization under Weaker Assumptions"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/272efd3a6091ceefcbc79f1f3a6fdba4-Abstract-Conference.html"
categories: ['stochastic-optimization-convergence-and-variance-reduction', 'deep-learning-optimization-and-generalization-theory']
tags: ['variance-reduction', 'adaptive-optimization', 'STORM']
venue: "NeurIPS 2024"
tldr: "This paper proposes adaptive variance reduction methods for stochastic optimization under weaker assumptions, improving upon existing STORM-based approaches."
---

# Adaptive Variance Reduction for Stochastic Optimization under Weaker Assumptions

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/272efd3a6091ceefcbc79f1f3a6fdba4-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/272efd3a6091ceefcbc79f1f3a6fdba4-Abstract-Conference.html)

**TLDR**: This paper proposes adaptive variance reduction methods for stochastic optimization under weaker assumptions, improving upon existing STORM-based approaches.

## Abstract

This paper explores adaptive variance reduction methods for stochastic optimization based on the STORM technique. Existing adaptive extensions of STORM rely on strong assumptions like bounded gradients and bounded function values, or suffer an additional $\mathcal{O}(\log T)$ term in the convergence rate. To address these limitations, we introduce a novel adaptive STORM method that achieves an optimal convergence rate of $\mathcal{O}(T^{-1/3})$ for non-convex functions with our newly designed learning rate strategy. Compared with existing approaches, our method requires weaker assumptions and attains the optimal convergence rate without the additional $\mathcal{O}(\log T)$ term. We also extend the proposed technique to stochastic compositional optimization, obtaining the same optimal rate of $\mathcal{O}(T^{-1/3})$. Furthermore, we investigate the non-convex finite-sum problem and develop another innovative adaptive variance reduction method that achieves an optimal convergence rate of $\mathcal{O}(n^{1/4} T^{-1/2} )$, where $n$ represents the number of component functions. Numerical experiments across various tasks validate the effectiveness of our method.