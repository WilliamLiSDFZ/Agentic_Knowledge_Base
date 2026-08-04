---
title: "How Transformers Learn Causal Structure with Gradient Descent"
source: "https://proceedings.mlr.press/v235/nichani24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nichani24a/nichani24a.pdf"
categories: ['neural-network-learning-dynamics-theory', 'causal-inference-and-discovery-methods']
tags: ['transformers', 'causal-structure', 'gradient-descent']
venue: "ICML 2024"
tldr: "Analyzes how transformers learn causal structure through gradient descent via the self-attention mechanism on sequence modeling tasks."
---

# How Transformers Learn Causal Structure with Gradient Descent

**Source**: [https://proceedings.mlr.press/v235/nichani24a.html](https://proceedings.mlr.press/v235/nichani24a.html)

**TLDR**: Analyzes how transformers learn causal structure through gradient descent via the self-attention mechanism on sequence modeling tasks.

## Abstract

The incredible success of transformers on sequence modeling tasks can be largely attributed to the self-attention mechanism, which allows information to be transferred between different parts of a sequence. Self-attention allows transformers to encode causal structure which makes them particularly suitable for sequence modeling. However, the process by which transformers learn such causal structure via gradient-based training algorithms remains poorly understood. To better understand this process, we introduce an in-context learning task that requires learning latent causal structure. We prove that gradient descent on a simplified two-layer transformer learns to solve this task by encoding the latent causal graph in the first attention layer. The key insight of our proof is that the gradient of the attention matrix encodes the mutual information between tokens. As a consequence of the data processing inequality, the largest entries of this gradient correspond to edges in the latent causal graph. As a special case, when the sequences are generated from in-context Markov chains, we prove that transformers learn an induction head (Olsson et al., 2022). We confirm our theoretical findings by showing that transformers trained on our in-context learning task are able to recover a wide variety of causal structures.