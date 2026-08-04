---
title: "A Dynamical Model of Neural Scaling Laws"
source: "https://proceedings.mlr.press/v235/bordelon24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bordelon24a/bordelon24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'transformer-architecture-efficiency-and-scaling']
tags: ['neural-scaling-laws', 'dynamical-model', 'compute-optimal', 'training-dynamics']
venue: "ICML 2024"
tldr: "This paper presents a dynamical model that theoretically explains and predicts neural scaling laws across training time, dataset size, and model size."
---

# A Dynamical Model of Neural Scaling Laws

**Source**: [https://proceedings.mlr.press/v235/bordelon24a.html](https://proceedings.mlr.press/v235/bordelon24a.html)

**TLDR**: This paper presents a dynamical model that theoretically explains and predicts neural scaling laws across training time, dataset size, and model size.

## Abstract

On a variety of tasks, the performance of neural networks predictably improves with training time, dataset size and model size across many orders of magnitude. This phenomenon is known as a neural scaling law. Of fundamental importance is the compute-optimal scaling law, which reports the performance as a function of units of compute when choosing model sizes optimally. We analyze a random feature model trained with gradient descent as a solvable model of network training and generalization. This reproduces many observations about neural scaling laws. First, our model makes a prediction about why the scaling of performance with training time and with model size have different power law exponents. Consequently, the theory predicts an asymmetric compute-optimal scaling rule where the number of training steps are increased faster than model parameters, consistent with recent empirical observations. Second, it has been observed that early in training, networks converge to their infinite-width dynamics at a rate $1/\text{width}$ but at late time exhibit a rate $\text{width}^{-c}$, where $c$ depends on the structure of the architecture and task. We show that our model exhibits this behavior. Lastly, our theory shows how the gap between training and test loss can gradually build up over time due to repeated reuse of data.