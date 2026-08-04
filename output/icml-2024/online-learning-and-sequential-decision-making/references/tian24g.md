---
title: "Boundary Exploration for Bayesian Optimization With Unknown Physical Constraints"
source: "https://proceedings.mlr.press/v235/tian24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tian24g/tian24g.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'online-learning-and-sequential-decision-making']
tags: ['Bayesian-optimization', 'unknown-constraints', 'boundary-exploration']
venue: "ICML 2024"
tldr: "A Bayesian optimization framework is proposed that explicitly explores feasibility boundaries to handle unknown physical constraints in black-box optimization."
---

# Boundary Exploration for Bayesian Optimization With Unknown Physical Constraints

**Source**: [https://proceedings.mlr.press/v235/tian24g.html](https://proceedings.mlr.press/v235/tian24g.html)

**TLDR**: A Bayesian optimization framework is proposed that explicitly explores feasibility boundaries to handle unknown physical constraints in black-box optimization.

## Abstract

Bayesian optimization has been successfully applied to optimize black-box functions where the number of evaluations is severely limited. However, in many real-world applications, it is hard or impossible to know in advance which designs are feasible due to some physical or system limitations. These issues lead to an even more challenging problem of optimizing an unknown function with unknown constraints. In this paper, we observe that in such scenarios optimal solution typically lies on the boundary between feasible and infeasible regions of the design space, making it considerably more difficult than that with interior optima. Inspired by this observation, we propose BE-CBO, a new Bayesian optimization method that efficiently explores the boundary between feasible and infeasible designs. To identify the boundary, we learn the constraints with an ensemble of neural networks that outperform the standard Gaussian Processes for capturing complex boundaries. Our method demonstrates superior performance against state-of-the-art methods through comprehensive experiments on synthetic and real-world benchmarks. Code available at: https://github.com/yunshengtian/BE-CBO