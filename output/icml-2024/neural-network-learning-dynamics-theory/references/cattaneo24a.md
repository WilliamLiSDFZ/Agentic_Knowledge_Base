---
title: "On the Implicit Bias of Adam"
source: "https://proceedings.mlr.press/v235/cattaneo24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cattaneo24a/cattaneo24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'neural-network-learning-dynamics-theory']
tags: ['Adam-optimizer', 'implicit-bias', 'backward-error-analysis', 'ODE-approximation']
venue: "ICML 2024"
tldr: "Analyzes the implicit bias of the Adam optimizer using backward error analysis to derive ODE approximations of its training trajectory."
---

# On the Implicit Bias of Adam

**Source**: [https://proceedings.mlr.press/v235/cattaneo24a.html](https://proceedings.mlr.press/v235/cattaneo24a.html)

**TLDR**: Analyzes the implicit bias of the Adam optimizer using backward error analysis to derive ODE approximations of its training trajectory.

## Abstract

In previous literature, backward error analysis was used to find ordinary differential equations (ODEs) approximating the gradient descent trajectory. It was found that finite step sizes implicitly regularize solutions because terms appearing in the ODEs penalize the two-norm of the loss gradients. We prove that the existence of similar implicit regularization in RMSProp and Adam depends on their hyperparameters and the training stage, but with a different "norm" involved: the corresponding ODE terms either penalize the (perturbed) one-norm of the loss gradients or, conversely, impede its reduction (the latter case being typical). We also conduct numerical experiments and discuss how the proven facts can influence generalization.