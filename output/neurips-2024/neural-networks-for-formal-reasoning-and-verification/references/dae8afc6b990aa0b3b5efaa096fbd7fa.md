---
title: "Newton Informed Neural Operator for Solving Nonlinear Partial Differential Equations"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/dae8afc6b990aa0b3b5efaa096fbd7fa-Abstract-Conference.html"
categories: ['physics-informed-neural-operators-and-simulations', 'neural-networks-for-formal-reasoning-and-verification']
tags: ['neural-operators', 'nonlinear-pdes', 'newton-method']
venue: "NeurIPS 2024"
tldr: "Newton Informed Neural Operator integrates Newton's method into neural operators to solve nonlinear PDEs with multiple solutions."
---

# Newton Informed Neural Operator for Solving Nonlinear Partial Differential Equations

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/dae8afc6b990aa0b3b5efaa096fbd7fa-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/dae8afc6b990aa0b3b5efaa096fbd7fa-Abstract-Conference.html)

**TLDR**: Newton Informed Neural Operator integrates Newton's method into neural operators to solve nonlinear PDEs with multiple solutions.

## Abstract

Solving nonlinear partial differential equations (PDEs) with multiple solutions is essential in various fields, including physics, biology, and engineering. However, traditional numerical methods, such as finite element and finite difference methods, often face challenges when dealing with nonlinear solvers, particularly in the presence of multiple solutions. These methods can become computationally expensive, especially when relying on solvers like Newton's method, which may struggle with ill-posedness near bifurcation points.In this paper, we propose a novel approach, the Newton Informed Neural Operator, which learns the Newton solver for nonlinear PDEs. Our method integrates traditional numerical techniques with the Newton nonlinear solver, efficiently learning the nonlinear mapping at each iteration. This approach allows us to compute multiple solutions in a single learning process while requiring fewer supervised data points than existing neural network methods.