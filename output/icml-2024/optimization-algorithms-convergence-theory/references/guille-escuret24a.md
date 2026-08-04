---
title: "No Wrong Turns: The Simple Geometry Of Neural Networks Optimization Paths"
source: "https://proceedings.mlr.press/v235/guille-escuret24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/guille-escuret24a/guille-escuret24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'optimization-algorithms-convergence-theory']
tags: ['optimization-paths', 'loss-landscape', 'neural-network-geometry', 'non-convex-optimization', 'stochastic-gradient-descent']
venue: "ICML 2024"
tldr: "Empirical and theoretical analysis showing that neural network optimization paths exhibit simple monotone geometry despite non-convexity."
---

# No Wrong Turns: The Simple Geometry Of Neural Networks Optimization Paths

**Source**: [https://proceedings.mlr.press/v235/guille-escuret24a.html](https://proceedings.mlr.press/v235/guille-escuret24a.html)

**TLDR**: Empirical and theoretical analysis showing that neural network optimization paths exhibit simple monotone geometry despite non-convexity.

## Abstract

Understanding the optimization dynamics of neural networks is necessary for closing the gap between theory and practice. Stochastic first-order optimization algorithms are known to efficiently locate favorable minima in deep neural networks. This efficiency, however, contrasts with the non-convex and seemingly complex structure of neural loss landscapes. In this study, we delve into the fundamental geometric properties of sampled gradients along optimization paths. We focus on two key quantities, the restricted secant inequality and error bound, as well as their ratio γ, which hold high significance for first-order optimization. Our analysis reveals that these quantities exhibit predictable, consistent behavior throughout training, despite the stochasticity induced by sampling minibatches. Our findings suggest that not only do optimization trajectories never encounter significant obstacles, but they also maintain stable dynamics during the majority of training. These observed properties are sufficiently expressive to theoretically guarantee linear convergence and prescribe learning rate schedules mirroring empirical practices. We conduct our experiments on image classification, semantic segmentation and language modeling across different batch sizes, network architectures, datasets, optimizers, and initialization seeds. We discuss the impact of each factor. Our work provides novel insights into the properties of neural network loss functions, and opens the door to theoretical frameworks more relevant to prevalent practice.