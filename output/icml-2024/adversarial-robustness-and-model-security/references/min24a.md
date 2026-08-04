---
title: "Can Implicit Bias Imply Adversarial Robustness?"
source: "https://proceedings.mlr.press/v235/min24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/min24a/min24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'neural-network-learning-dynamics-theory']
tags: ['implicit-bias', 'adversarial-robustness', 'gradient-descent']
venue: "ICML 2024"
tldr: "Investigates conditions under which the implicit bias of gradient-based training can both harm and potentially imply adversarial robustness."
---

# Can Implicit Bias Imply Adversarial Robustness?

**Source**: [https://proceedings.mlr.press/v235/min24a.html](https://proceedings.mlr.press/v235/min24a.html)

**TLDR**: Investigates conditions under which the implicit bias of gradient-based training can both harm and potentially imply adversarial robustness.

## Abstract

The implicit bias of gradient-based training algorithms has been considered mostly beneficial as it leads to trained networks that often generalize well. However, Frei et al. (2023) show that such implicit bias can harm adversarial robustness. Specifically, they show that if the data consists of clusters with small inter-cluster correlation, a shallow (two-layer) ReLU network trained by gradient flow generalizes well, but it is not robust to adversarial attacks of small radius. Moreover, this phenomenon occurs despite the existence of a much more robust classifier that can be explicitly constructed from a shallow network. In this paper, we extend recent analyses of neuron alignment to show that a shallow network with a polynomial ReLU activation (pReLU) trained by gradient flow not only generalizes well but is also robust to adversarial attacks. Our results highlight the importance of the interplay between data structure and architecture design in the implicit bias and robustness of trained networks.