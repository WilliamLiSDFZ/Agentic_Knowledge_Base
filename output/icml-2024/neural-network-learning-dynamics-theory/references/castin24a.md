---
title: "How Smooth Is Attention?"
source: "https://proceedings.mlr.press/v235/castin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/castin24a/castin24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'neural-network-learning-dynamics-theory']
tags: ['attention-mechanism', 'Lipschitz-continuity', 'transformer-robustness', 'smoothness']
venue: "ICML 2024"
tldr: "Provides a detailed mathematical analysis of the Lipschitz properties of self-attention and masked self-attention mechanisms in transformers."
---

# How Smooth Is Attention?

**Source**: [https://proceedings.mlr.press/v235/castin24a.html](https://proceedings.mlr.press/v235/castin24a.html)

**TLDR**: Provides a detailed mathematical analysis of the Lipschitz properties of self-attention and masked self-attention mechanisms in transformers.

## Abstract

Self-attention and masked self-attention are at the heart of Transformers’ outstanding success. Still, our mathematical understanding of attention, in particular of its Lipschitz properties — which are key when it comes to analyzing robustness and expressive power — is incomplete. We provide a detailed study of the Lipschitz constant of self-attention in several practical scenarios, discussing the impact of the sequence length $n$ and layer normalization on the local Lipschitz constant of both unmasked and masked self-attention. In particular, we show that for inputs of length $n$ in any compact set, the Lipschitz constant of self-attention is bounded by $\sqrt{n}$ up to a constant factor and that this bound is tight for reasonable sequence lengths. When the sequence length $n$ is too large for the previous bound to be tight, which we refer to as the mean-field regime, we provide an upper bound and a matching lower bound which are independent of $n$. Our mean-field framework for masked self-attention is novel and of independent interest. Our experiments on pretrained and randomly initialized BERT and GPT-2 support our theoretical findings.