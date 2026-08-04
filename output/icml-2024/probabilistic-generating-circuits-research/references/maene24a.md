---
title: "On the Hardness of Probabilistic Neurosymbolic Learning"
source: "https://proceedings.mlr.press/v235/maene24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/maene24a/maene24a.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'probabilistic-generating-circuits-research']
tags: ['neurosymbolic-learning', 'probabilistic-reasoning', 'gradient-complexity']
venue: "ICML 2024"
tldr: "A theoretical analysis of the computational hardness of differentiating probabilistic neurosymbolic models trained with gradient descent."
---

# On the Hardness of Probabilistic Neurosymbolic Learning

**Source**: [https://proceedings.mlr.press/v235/maene24a.html](https://proceedings.mlr.press/v235/maene24a.html)

**TLDR**: A theoretical analysis of the computational hardness of differentiating probabilistic neurosymbolic models trained with gradient descent.

## Abstract

The limitations of purely neural learning have sparked an interest in probabilistic neurosymbolic models, which combine neural networks with probabilistic logical reasoning. As these neurosymbolic models are trained with gradient descent, we study the complexity of differentiating probabilistic reasoning. We prove that although approximating these gradients is intractable in general, it becomes tractable during training. Furthermore, we introduce WeightME, an unbiased gradient estimator based on model sampling. Under mild assumptions, WeightME approximates the gradient with probabilistic guarantees using a logarithmic number of calls to a SAT solver. Lastly, we evaluate the necessity of these guarantees on the gradient. Our experiments indicate that the existing biased approximations indeed struggle to optimize even when exact solving is still feasible.