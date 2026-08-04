---
title: "Implicit Compressibility of Overparametrized Neural Networks Trained with Heavy-Tailed SGD"
source: "https://proceedings.mlr.press/v235/wan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wan24a/wan24a.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'neural-network-learning-dynamics-theory']
tags: ['neural-network-compression', 'heavy-tailed-SGD', 'implicit-compressibility', 'generalization', 'overparameterization']
venue: "ICML 2024"
tldr: "Shows that heavy-tailed SGD noise induces implicit compressibility in overparameterized neural networks, linking hyperparameter choice to generalization via compression."
---

# Implicit Compressibility of Overparametrized Neural Networks Trained with Heavy-Tailed SGD

**Source**: [https://proceedings.mlr.press/v235/wan24a.html](https://proceedings.mlr.press/v235/wan24a.html)

**TLDR**: Shows that heavy-tailed SGD noise induces implicit compressibility in overparameterized neural networks, linking hyperparameter choice to generalization via compression.

## Abstract

Neural network compression has been an increasingly important subject, not only due to its practical relevance, but also due to its theoretical implications, as there is an explicit connection between compressibility and generalization error. Recent studies have shown that the choice of the hyperparameters of stochastic gradient descent (SGD) can have an effect on the compressibility of the learned parameter vector. These results, however, rely on unverifiable assumptions and the resulting theory does not provide a practical guideline due to its implicitness. In this study, we propose a simple modification for SGD, such that the outputs of the algorithm will be provably compressible without making any nontrivial assumptions. We consider a one-hidden-layer neural network trained with SGD, and show that if we inject additive heavy-tailed noise to the iterates at each iteration, for any compression rate, there exists a level of overparametrization such that the output of the algorithm will be compressible with high probability. To achieve this result, we make two main technical contributions: (i) we prove a "propagation of chaos" result for a class of heavy-tailed stochastic differential equations, and (ii) we derive error estimates for their Euler discretization. Our experiments suggest that the proposed approach not only achieves increased compressibility with various models and datasets, but also leads to robust test performance under pruning, even in more realistic architectures that lie beyond our theoretical setting.