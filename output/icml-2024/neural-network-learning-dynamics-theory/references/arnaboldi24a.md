---
title: "Online Learning and Information Exponents: The Importance of Batch size & Time/Complexity Tradeoffs"
source: "https://proceedings.mlr.press/v235/arnaboldi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/arnaboldi24a/arnaboldi24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'online-learning-and-sequential-decision-making']
tags: ['SGD', 'batch-size', 'two-layer-networks', 'information-exponents', 'complexity-tradeoffs']
venue: "ICML 2024"
tldr: "Characterizes optimal batch size minimizing iteration time for one-pass SGD on multi-index target functions in neural network training."
---

# Online Learning and Information Exponents: The Importance of Batch size & Time/Complexity Tradeoffs

**Source**: [https://proceedings.mlr.press/v235/arnaboldi24a.html](https://proceedings.mlr.press/v235/arnaboldi24a.html)

**TLDR**: Characterizes optimal batch size minimizing iteration time for one-pass SGD on multi-index target functions in neural network training.

## Abstract

We study the impact of the batch size $n_b$ on the iteration time $T$ of training two-layer neural networks with one-pass stochastic gradient descent (SGD) on multi-index target functions of isotropic covariates. We characterize the optimal batch size minimizing the iteration time as a function of the hardness of the target, as characterized by the information exponents. We show that performing gradient updates with large batches $n_b \lesssim d^{\frac{\ell}{2}}$ minimizes the training time without changing the total sample complexity, where $\ell$ is the information exponent of the target to be learned and $d$ is the input dimension. However, larger batch sizes than $n_b \gg d^{\frac{\ell}{2}}$ are detrimental for improving the time complexity of SGD. We provably overcome this fundamental limitation via a different training protocol, Correlation loss SGD, which suppresses the auto-correlation terms in the loss function. We show that one can track the training progress by a system of low-dimensional ordinary differential equations (ODEs). Finally, we validate our theoretical results with numerical experiments.