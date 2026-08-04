---
title: "Transformers Learn Nonlinear Features In Context: Nonconvex Mean-field Dynamics on the Attention Landscape"
source: "https://proceedings.mlr.press/v235/kim24af.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24af/kim24af.pdf"
categories: ['neural-network-learning-dynamics-theory', 'large-language-model-alignment-and-capabilities']
tags: ['transformers', 'in-context-learning', 'mean-field-dynamics']
venue: "ICML 2024"
tldr: "Analyzes how transformers learn nonlinear features in context via nonconvex mean-field dynamics on the attention landscape."
---

# Transformers Learn Nonlinear Features In Context: Nonconvex Mean-field Dynamics on the Attention Landscape

**Source**: [https://proceedings.mlr.press/v235/kim24af.html](https://proceedings.mlr.press/v235/kim24af.html)

**TLDR**: Analyzes how transformers learn nonlinear features in context via nonconvex mean-field dynamics on the attention landscape.

## Abstract

Large language models based on the Transformer architecture have demonstrated impressive capabilities to learn in context. However, existing theoretical studies on how this phenomenon arises are limited to the dynamics of a single layer of attention trained on linear regression tasks. In this paper, we study the optimization of a Transformer consisting of a fully connected layer followed by a linear attention layer. The MLP acts as a common nonlinear representation or feature map, greatly enhancing the power of in-context learning. We prove in the mean-field and two-timescale limit that the infinite-dimensional loss landscape for the distribution of parameters, while highly nonconvex, becomes quite benign. We also analyze the second-order stability of mean-field dynamics and show that Wasserstein gradient flow almost always avoids saddle points. Furthermore, we establish novel methods for obtaining concrete improvement rates both away from and near critical points. This represents the first saddle point analysis of mean-field dynamics in general and the techniques are of independent interest.