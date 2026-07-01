---
title: "Banded Square Root Matrix Factorization for Differentially Private Model Training"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1f7b3b0dd7710af02aac0db5be4cfc8d-Abstract-Conference.html"
categories: ['privacy-preserving-federated-distributed-learning', 'statistical-learning-theory-and-matrix-methods']
tags: ['differential-privacy', 'matrix-factorization', 'banded-square-root']
venue: "NeurIPS 2024"
tldr: "Introduces banded square root matrix factorization to reduce computational overhead in differentially private model training while maintaining near-optimal noise."
---

# Banded Square Root Matrix Factorization for Differentially Private Model Training

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1f7b3b0dd7710af02aac0db5be4cfc8d-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/1f7b3b0dd7710af02aac0db5be4cfc8d-Abstract-Conference.html)

**TLDR**: Introduces banded square root matrix factorization to reduce computational overhead in differentially private model training while maintaining near-optimal noise.

## Abstract

Current state-of-the-art methods for differentially private model training are based on matrix factorization techniques. However, these methods suffer from high computational overhead because they require numerically solving a demanding optimization problem to determine an approximately optimal factorization prior to the actual model training. In this work, we present a new matrix factorization approach, BSR, which overcomes this computational bottleneck. By exploiting properties of the standard matrix square root, BSR allows to efficiently handle also large-scale problems. For the key scenario of stochastic gradient descent with momentum and weight decay, we even derive analytical expressions for BSR that render the computational overhead negligible. We prove bounds on the approximation quality that hold both in the centralized and in the federated learning setting. Our numerical experiments demonstrate that models trained using BSR perform on par with the best existing methods, while completely avoiding their computational overhead.