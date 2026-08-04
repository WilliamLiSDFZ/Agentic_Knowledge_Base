---
title: "When Representations Align: Universality in Representation Learning Dynamics"
source: "https://proceedings.mlr.press/v235/van-rossem24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/van-rossem24a/van-rossem24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'llm-geometry-and-interpretability-research']
tags: ['representation-learning', 'universality', 'learning-dynamics']
venue: "ICML 2024"
tldr: "Investigates conditions under which different neural network architectures converge to universal representations during training."
---

# When Representations Align: Universality in Representation Learning Dynamics

**Source**: [https://proceedings.mlr.press/v235/van-rossem24a.html](https://proceedings.mlr.press/v235/van-rossem24a.html)

**TLDR**: Investigates conditions under which different neural network architectures converge to universal representations during training.

## Abstract

Deep neural networks come in many sizes and architectures. The choice of architecture, in conjunction with the dataset and learning algorithm, is commonly understood to affect the learned neural representations. Yet, recent results have shown that different architectures learn representations with striking qualitative similarities. Here we derive an effective theory of representation learning under the assumption that the encoding map from input to hidden representation and the decoding map from representation to output are arbitrary smooth functions. This theory schematizes representation learning dynamics in the regime of complex, large architectures, where hidden representations are not strongly constrained by the parametrization. We show through experiments that the effective theory describes aspects of representation learning dynamics across a range of deep networks with different activation functions and architectures, and exhibits phenomena similar to the “rich” and “lazy” regime. While many network behaviors depend quantitatively on architecture, our findings point to certain behaviors that are widely conserved once models are sufficiently flexible.