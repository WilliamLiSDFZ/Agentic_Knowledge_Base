---
title: "Faster Adaptive Decentralized Learning Algorithms"
source: "https://proceedings.mlr.press/v235/huang24ah.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24ah/huang24ah.pdf"
categories: ['optimization-algorithms-convergence-theory', 'privacy-preserving-federated-and-distributed-learning']
tags: ['decentralized-learning', 'adaptive-gradient', 'convergence', 'optimization', 'communication-efficiency']
venue: "ICML 2024"
tldr: "Develops faster adaptive decentralized learning algorithms with improved convergence guarantees for large-scale machine learning."
---

# Faster Adaptive Decentralized Learning Algorithms

**Source**: [https://proceedings.mlr.press/v235/huang24ah.html](https://proceedings.mlr.press/v235/huang24ah.html)

**TLDR**: Develops faster adaptive decentralized learning algorithms with improved convergence guarantees for large-scale machine learning.

## Abstract

Decentralized learning recently has received increasing attention in machine learning due to its advantages in implementation simplicity and system robustness, data privacy. Meanwhile, the adaptive gradient methods show superior performances in many machine learning tasks such as training neural networks. Although some works focus on studying decentralized optimization algorithms with adaptive learning rates, these adaptive decentralized algorithms still suffer from high sample complexity. To fill these gaps, we propose a class of faster adaptive decentralized algorithms (i.e., AdaMDOS and AdaMDOF) for distributed nonconvex stochastic and finite-sum optimization, respectively. Moreover, we provide a solid convergence analysis framework for our methods. In particular, we prove that our AdaMDOS obtains a near-optimal sample complexity of $\tilde{O}(\epsilon^{-3})$ for finding an $\epsilon$-stationary solution of nonconvex stochastic optimization. Meanwhile, our AdaMDOF obtains a near-optimal sample complexity of $O(\sqrt{n}\epsilon^{-2})$ for finding an $\epsilon$-stationary solution of for nonconvex finite-sum optimization, where $n$ denotes the sample size. To the best of our knowledge, our AdaMDOF algorithm is the first adaptive decentralized algorithm for nonconvex finite-sum optimization. Some experimental results demonstrate efficiency of our algorithms.