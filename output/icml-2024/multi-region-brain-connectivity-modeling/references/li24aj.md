---
title: "A Differentiable Partially Observable Generalized Linear Model with Forward-Backward Message Passing"
source: "https://proceedings.mlr.press/v235/li24aj.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24aj/li24aj.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'multi-region-brain-connectivity-modeling']
tags: ['partially-observable', 'generalized-linear-model', 'neural-connectivity', 'variational-inference', 'message-passing']
venue: "ICML 2024"
tldr: "A differentiable POGLM with forward-backward message passing improves learning of neural connectivities from spike train data."
---

# A Differentiable Partially Observable Generalized Linear Model with Forward-Backward Message Passing

**Source**: [https://proceedings.mlr.press/v235/li24aj.html](https://proceedings.mlr.press/v235/li24aj.html)

**TLDR**: A differentiable POGLM with forward-backward message passing improves learning of neural connectivities from spike train data.

## Abstract

The partially observable generalized linear model (POGLM) is a powerful tool for understanding neural connectivities under the assumption of existing hidden neurons. With spike trains only recorded from visible neurons, existing works use variational inference to learn POGLM meanwhile presenting the difficulty of learning this latent variable model. There are two main issues: (1) the sampled Poisson hidden spike count hinders the use of the pathwise gradient estimator in VI; and (2) the existing design of the variational model is neither expressive nor time-efficient, which further affects the performance. For (1), we propose a new differentiable POGLM, which enables the pathwise gradient estimator, better than the score function gradient estimator used in existing works. For (2), we propose the forward-backward message-passing sampling scheme for the variational model. Comprehensive experiments show that our differentiable POGLMs with our forward-backward message passing produce a better performance on one synthetic and two real-world datasets. Furthermore, our new method yields more interpretable parameters, underscoring its significance in neuroscience.