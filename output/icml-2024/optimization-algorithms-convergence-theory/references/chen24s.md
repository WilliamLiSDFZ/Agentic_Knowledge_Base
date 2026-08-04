---
title: "Accelerated Policy Gradient for s-rectangular Robust MDPs with Large State Spaces"
source: "https://proceedings.mlr.press/v235/chen24s.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24s/chen24s.pdf"
categories: ['optimization-algorithms-convergence-theory', 'online-learning-and-sequential-decision-making']
tags: ['robust-MDPs', 'policy-gradient', 's-rectangular', 'accelerated-optimization']
venue: "ICML 2024"
tldr: "An accelerated policy gradient method for s-rectangular robust MDPs that improves iteration complexity for large state spaces."
---

# Accelerated Policy Gradient for s-rectangular Robust MDPs with Large State Spaces

**Source**: [https://proceedings.mlr.press/v235/chen24s.html](https://proceedings.mlr.press/v235/chen24s.html)

**TLDR**: An accelerated policy gradient method for s-rectangular robust MDPs that improves iteration complexity for large state spaces.

## Abstract

Robust Markov decision process (robust MDP) is an important machine learning framework to make a reliable policy that is robust to environmental perturbation. Despite empirical success and popularity of policy gradient methods, existing policy gradient methods require at least iteration complexity $\mathcal{O}(\epsilon^{-4})$ to converge to the global optimal solution of s-rectangular robust MDPs with $\epsilon$-accuracy and are limited to deterministic setting with access to exact gradients and small state space that are impractical in many applications. In this work, we propose an accelerated policy gradient algorithm with iteration complexity $\mathcal{O}(\epsilon^{-3}\ln\epsilon^{-1})$ in the deterministic setting using entropy regularization. Furthermore, we extend this algorithm to stochastic setting with access to only stochastic gradients and large state space which achieves the sample complexity $\mathcal{O}(\epsilon^{-7}\ln\epsilon^{-1})$. In the meantime, our algorithms are also the first scalable policy gradient methods to entropy-regularized robust MDPs, which provide an important but underexplored machine learning framework.