---
title: "Replicable Learning of Large-Margin Halfspaces"
source: "https://proceedings.mlr.press/v235/kalavasis24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kalavasis24a/kalavasis24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'sampling-compression-and-dimensionality-reduction']
tags: ['replicability', 'large-margin-halfspaces', 'PAC-learning', 'dimension-independence']
venue: "ICML 2024"
tldr: "Presents an efficient dimension-independent replicable algorithm for learning large-margin halfspaces with improved complexity bounds."
---

# Replicable Learning of Large-Margin Halfspaces

**Source**: [https://proceedings.mlr.press/v235/kalavasis24a.html](https://proceedings.mlr.press/v235/kalavasis24a.html)

**TLDR**: Presents an efficient dimension-independent replicable algorithm for learning large-margin halfspaces with improved complexity bounds.

## Abstract

We provide an efficient replicable algorithm for the problem of learning large-margin halfspaces. Our results improve upon the algorithms provided by Impagliazzo, Lei, Pitassi, and Sorrell (STOC, 2022). We design the first dimension-independent replicable algorithm for this task which runs in polynomial time, is proper, and has strictly improved sample complexity compared to the one achieved by Impagliazzo et al. (STOC, 2022) with respect to all the relevant parameters. Moreover, our algorithm has sample complexity that is optimal with respect to the accuracy parameter $\epsilon$. Departing from the requirement of polynomial time algorithms, using the DP-to-Replicability reduction of Bun et al. (STOC 2023), we show how to obtain a replicable algorithm for large-margin halfspaces with improved sample complexity with respect to the margin parameter $\tau$, but running time doubly exponential in $1/\tau^2$ and worse sample complexity dependence on $\epsilon$ than our previous algorithm. We then design an improved algorithm with better sample complexity than both of our previous algorithms and running time exponential in $1/\tau^{2}.$