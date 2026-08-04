---
title: "High-Order Contrastive Learning with Fine-grained Comparative Levels for Sparse Ordinal Tensor Completion"
source: "https://proceedings.mlr.press/v235/dai24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dai24c/dai24c.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'information-retrieval-and-recommendation-systems']
tags: ['contrastive-learning', 'tensor-completion', 'sparse-data', 'ordinal-data', 'representation-learning']
venue: "ICML 2024"
tldr: "Proposes a high-order contrastive learning framework with fine-grained comparative levels for sparse ordinal tensor completion by modeling complex mode interactions."
---

# High-Order Contrastive Learning with Fine-grained Comparative Levels for Sparse Ordinal Tensor Completion

**Source**: [https://proceedings.mlr.press/v235/dai24c.html](https://proceedings.mlr.press/v235/dai24c.html)

**TLDR**: Proposes a high-order contrastive learning framework with fine-grained comparative levels for sparse ordinal tensor completion by modeling complex mode interactions.

## Abstract

Contrastive learning is a powerful paradigm for representation learning with prominent success in computer vision and NLP, but how to extend its success to high-dimensional tensors remains a challenge. This is because tensor data often exhibit high-order mode-interactions that are hard to profile and with negative samples growing combinatorially faster than second-order contrastive learning; furthermore, many real-world tensors have ordinal entries that necessitate more delicate comparative levels. To solve the challenge, we propose High-Order Contrastive Tensor Completion (HOCTC), an innovative network to extend contrastive learning to sparse ordinal tensor data. HOCTC employs a novel attention-based strategy with query-expansion to capture high-order mode interactions even in case of very limited tokens, which transcends beyond second-order learning scenarios. Besides, it extends two-level comparisons (positive-vs-negative) to fine-grained contrast-levels using ordinal tensor entries as a natural guidance. Efficient sampling scheme is proposed to enforce such delicate comparative structures, generating comprehensive self-supervised signals for high-order representation learning. Extensive experiments show that HOCTC has promising results in sparse tensor completion in traffic/recommender applications.