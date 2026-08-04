---
title: "Symmetry Induces Structure and Constraint of Learning"
source: "https://proceedings.mlr.press/v235/ziyin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ziyin24a/ziyin24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'algebraic-structures-in-machine-learning']
tags: ['symmetry', 'loss-landscape', 'neural-networks', 'mirror-reflection', 'learning-dynamics']
venue: "ICML 2024"
tldr: "This paper proves that mirror-reflection symmetries in loss functions induce structural constraints on learning behavior in neural networks."
---

# Symmetry Induces Structure and Constraint of Learning

**Source**: [https://proceedings.mlr.press/v235/ziyin24a.html](https://proceedings.mlr.press/v235/ziyin24a.html)

**TLDR**: This paper proves that mirror-reflection symmetries in loss functions induce structural constraints on learning behavior in neural networks.

## Abstract

Due to common architecture designs, symmetries exist extensively in contemporary neural networks. In this work, we unveil the importance of the loss function symmetries in affecting, if not deciding, the learning behavior of machine learning models. We prove that every mirror-reflection symmetry, with reflection surface $O$, in the loss function leads to the emergence of a constraint on the model parameters $\theta$: $O^T\theta =0$. This constrained solution becomes satisfied when either the weight decay or gradient noise is large. Common instances of mirror symmetries in deep learning include rescaling, rotation, and permutation symmetry. As direct corollaries, we show that rescaling symmetry leads to sparsity, rotation symmetry leads to low rankness, and permutation symmetry leads to homogeneous ensembling. Then, we show that the theoretical framework can explain intriguing phenomena, such as the loss of plasticity and various collapse phenomena in neural networks, and suggest how symmetries can be used to design an elegant algorithm to enforce hard constraints in a differentiable way.