---
title: "Efficient Pareto Manifold Learning with Low-Rank Structure"
source: "https://proceedings.mlr.press/v235/chen24x.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24x/chen24x.pdf"
categories: ['optimization-algorithms-convergence-theory', '3d-vision-and-scene-understanding']
tags: ['multi-task-learning', 'Pareto-front', 'low-rank', 'multi-objective-optimization']
venue: "ICML 2024"
tldr: "An efficient method for continuous Pareto manifold learning that exploits low-rank structure to approximate multi-task trade-off solutions compactly."
---

# Efficient Pareto Manifold Learning with Low-Rank Structure

**Source**: [https://proceedings.mlr.press/v235/chen24x.html](https://proceedings.mlr.press/v235/chen24x.html)

**TLDR**: An efficient method for continuous Pareto manifold learning that exploits low-rank structure to approximate multi-task trade-off solutions compactly.

## Abstract

Multi-task learning, which optimizes performance across multiple tasks, is inherently a multi-objective optimization problem. Various algorithms are developed to provide discrete trade-off solutions on the Pareto front. Recently, continuous Pareto front approximations using a linear combination of base networks have emerged as a compelling strategy. However, it suffers from scalability issues when the number of tasks is large. To address this issue, we propose a novel approach that integrates a main network with several low-rank matrices to efficiently learn the Pareto manifold. It significantly reduces the number of parameters and facilitates the extraction of shared features. We also introduce orthogonal regularization to further bolster performance. Extensive experimental results demonstrate that the proposed approach outperforms state-of-the-art baselines, especially on datasets with a large number of tasks.