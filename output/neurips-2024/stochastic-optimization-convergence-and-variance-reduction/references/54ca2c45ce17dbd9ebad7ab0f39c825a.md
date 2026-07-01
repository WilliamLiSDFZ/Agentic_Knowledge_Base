---
title: "Remove that Square Root: A New Efficient Scale-Invariant Version of AdaGrad"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/54ca2c45ce17dbd9ebad7ab0f39c825a-Abstract-Conference.html"
categories: ['stochastic-optimization-convergence-and-variance-reduction']
tags: ['AdaGrad', 'scale-invariant', 'adaptive-optimization']
venue: "NeurIPS 2024"
tldr: "KATE is a novel scale-invariant adaptation of AdaGrad that removes the square root operation while maintaining convergence guarantees."
---

# Remove that Square Root: A New Efficient Scale-Invariant Version of AdaGrad

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/54ca2c45ce17dbd9ebad7ab0f39c825a-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/54ca2c45ce17dbd9ebad7ab0f39c825a-Abstract-Conference.html)

**TLDR**: KATE is a novel scale-invariant adaptation of AdaGrad that removes the square root operation while maintaining convergence guarantees.

## Abstract

Adaptive methods are extremely popular in machine learning as they make learning rate tuning less expensive. This paper introduces a novel optimization algorithm named KATE, which presents a scale-invariant adaptation of the well-known AdaGrad algorithm. We prove the scale-invariance of KATE for the case of Generalized Linear Models. Moreover, for general smooth non-convex problems, we establish a convergence rate of  $O((\log T)/\sqrt{T})$ for KATE, matching the best-known ones for AdaGrad and Adam. We also compare KATE to other state-of-the-art adaptive algorithms Adam and AdaGrad in numerical experiments with different problems, including complex machine learning tasks like image classification and text classification on real data. The results indicate that KATE consistently outperforms AdaGrad and matches/surpasses the performance of Adam in all considered scenarios.