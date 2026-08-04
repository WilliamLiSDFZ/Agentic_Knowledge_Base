---
title: "How do Transformers Perform In-Context Autoregressive Learning ?"
source: "https://proceedings.mlr.press/v235/sander24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sander24a/sander24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'transformer-architecture-efficiency-and-scaling']
tags: ['transformers', 'in-context-learning', 'autoregressive', 'theoretical-analysis', 'next-token-prediction']
venue: "ICML 2024"
tldr: "Transformers trained on next-token prediction tasks are theoretically and empirically analyzed to understand how they perform in-context autoregressive learning."
---

# How do Transformers Perform In-Context Autoregressive Learning ?

**Source**: [https://proceedings.mlr.press/v235/sander24a.html](https://proceedings.mlr.press/v235/sander24a.html)

**TLDR**: Transformers trained on next-token prediction tasks are theoretically and empirically analyzed to understand how they perform in-context autoregressive learning.

## Abstract

Transformers have achieved state-of-the-art performance in language modeling tasks. However, the reasons behind their tremendous success are still unclear. In this paper, towards a better understanding, we train a Transformer model on a simple next token prediction task, where sequences are generated as a first-order autoregressive process $s_{t+1} = W s_t$. We show how a trained Transformer predicts the next token by first learning $W$ in-context, then applying a prediction mapping. We call the resulting procedure in-context autoregressive learning. More precisely, focusing on commuting orthogonal matrices $W$, we first show that a trained one-layer linear Transformer implements one step of gradient descent for the minimization of an inner objective function, when considering augmented tokens. When the tokens are not augmented, we characterize the global minima of a one-layer diagonal linear multi-head Transformer. Importantly, we exhibit orthogonality between heads and show that positional encoding captures trigonometric relations in the data. On the experimental side, we consider the general case of non-commuting orthogonal matrices and generalize our theoretical findings.