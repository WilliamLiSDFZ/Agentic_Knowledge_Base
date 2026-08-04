---
title: "TENG: Time-Evolving Natural Gradient for Solving PDEs With Deep Neural Nets Toward Machine Precision"
source: "https://proceedings.mlr.press/v235/chen24ad.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24ad/chen24ad.pdf"
categories: ['neural-operators-for-pde-solving', 'optimization-algorithms-convergence-theory']
tags: ['PDEs', 'natural-gradient', 'neural-network-solvers', 'machine-precision']
venue: "ICML 2024"
tldr: "Proposes a time-evolving natural gradient method to train neural network PDE solvers toward machine precision for initial value problems."
---

# TENG: Time-Evolving Natural Gradient for Solving PDEs With Deep Neural Nets Toward Machine Precision

**Source**: [https://proceedings.mlr.press/v235/chen24ad.html](https://proceedings.mlr.press/v235/chen24ad.html)

**TLDR**: Proposes a time-evolving natural gradient method to train neural network PDE solvers toward machine precision for initial value problems.

## Abstract

Partial differential equations (PDEs) are instrumental for modeling dynamical systems in science and engineering. The advent of neural networks has initiated a significant shift in tackling these complexities though challenges in accuracy persist, especially for initial value problems. In this paper, we introduce the Time-Evolving Natural Gradient (TENG), generalizing time-dependent variational principles and optimization-based time integration, leveraging natural gradient optimization to obtain high accuracy in neural-network-based PDE solutions. Our comprehensive development includes algorithms like TENG-Euler and its high-order variants, such as TENG-Heun, tailored for enhanced precision and efficiency. TENG’s effectiveness is further validated through its performance, surpassing current leading methods and achieving machine precision in step-by-step optimizations across a spectrum of PDEs, including the heat equation, Allen-Cahn equation, and Burgers’ equation.