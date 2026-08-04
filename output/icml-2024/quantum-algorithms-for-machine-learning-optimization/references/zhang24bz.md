---
title: "Quantum Algorithms and Lower Bounds for Finite-Sum Optimization"
source: "https://proceedings.mlr.press/v235/zhang24bz.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24bz/zhang24bz.pdf"
categories: ['quantum-algorithms-for-machine-learning-optimization', 'optimization-algorithms-convergence-theory']
tags: ['quantum-computing', 'finite-sum-optimization', 'lower-bounds']
venue: "ICML 2024"
tldr: "Initiates the study of quantum algorithms and lower bounds for finite-sum optimization problems common in machine learning."
---

# Quantum Algorithms and Lower Bounds for Finite-Sum Optimization

**Source**: [https://proceedings.mlr.press/v235/zhang24bz.html](https://proceedings.mlr.press/v235/zhang24bz.html)

**TLDR**: Initiates the study of quantum algorithms and lower bounds for finite-sum optimization problems common in machine learning.

## Abstract

Finite-sum optimization has wide applications in machine learning, covering important problems such as support vector machines, regression, etc. In this paper, we initiate the study of solving finite-sum optimization problems by quantum computing. Specifically, let $f_1,\ldots,f_n:\mathbb{R}^d\to\mathbb{R}$ be $\ell$-smooth convex functions and $\psi:\mathbb{R}^d\to\mathbb{R}$ be a $\mu$-strongly convex proximal function. The goal is to find an $\epsilon$-optimal point for $F(\mathbf{x})=\frac{1}{n}\sum_{i=1}^n f_i(\mathbf{x})+\psi(\mathbf{x})$. We give a quantum algorithm with complexity $\tilde{O}\big(n+\sqrt{d}+\sqrt{\ell/\mu}\big(n^{1/3}d^{1/3}+n^{-2/3}d^{5/6}\big)\big)$, improving the classical tight bound $\tilde{\Theta}\big(n+\sqrt{n\ell/\mu}\big)$. We also prove a quantum lower bound $\tilde{\Omega}(n+n^{3/4}(\ell/\mu)^{1/4})$ when $d$ is large enough. Both our quantum upper and lower bounds can extend to the cases where $\psi$ is not necessarily strongly convex, or each $f_i$ is Lipschitz but not necessarily smooth. In addition, when $F$ is nonconvex, our quantum algorithm can find an $\epsilon$-critial point using $\tilde{O}(n+\ell(d^{1/3}n^{1/3}+\sqrt{d})/\epsilon^2)$ queries.