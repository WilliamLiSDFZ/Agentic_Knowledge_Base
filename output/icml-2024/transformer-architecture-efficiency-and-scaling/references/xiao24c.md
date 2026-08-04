---
title: "Improved Operator Learning by Orthogonal Attention"
source: "https://proceedings.mlr.press/v235/xiao24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xiao24c/xiao24c.pdf"
categories: ['neural-operators-for-pde-solving', 'transformer-architecture-efficiency-and-scaling']
tags: ['neural-operators', 'orthogonal-attention', 'PDEs']
venue: "ICML 2024"
tldr: "Introduces orthogonal attention for neural operators to improve PDE surrogate modeling by reformulating the kernel integral operator."
---

# Improved Operator Learning by Orthogonal Attention

**Source**: [https://proceedings.mlr.press/v235/xiao24c.html](https://proceedings.mlr.press/v235/xiao24c.html)

**TLDR**: Introduces orthogonal attention for neural operators to improve PDE surrogate modeling by reformulating the kernel integral operator.

## Abstract

This work presents orthogonal attention for constructing neural operators to serve as surrogates to model the solutions of a family of Partial Differential Equations (PDEs). The motivation is that the kernel integral operator, which is usually at the core of neural operators, can be reformulated with orthonormal eigenfunctions. Inspired by the success of the neural approximation of eigenfunctions (Deng et al., 2022), we opt to directly parameterize the involved eigenfunctions with flexible neural networks (NNs), based on which the input function is then transformed by the rule of kernel integral. Surprisingly, the resulting NN module bears a striking resemblance to regular attention mechanisms, albeit without softmax. Instead, it incorporates an orthogonalization operation that provides regularization during model training and helps mitigate overfitting, particularly in scenarios with limited data availability. In practice, the orthogonalization operation can be implemented with minimal additional overheads. Experiments on six standard neural operator benchmark datasets comprising both regular and irregular geometries show that our method can outperform competing baselines with decent margins.