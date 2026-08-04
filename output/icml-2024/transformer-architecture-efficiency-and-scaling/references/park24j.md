---
title: "Can Mamba Learn How To Learn? A Comparative Study on In-Context Learning Tasks"
source: "https://proceedings.mlr.press/v235/park24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/park24j/park24j.pdf"
categories: ['sequence-models-for-memory-and-state', 'transformer-architecture-efficiency-and-scaling']
tags: ['state-space-models', 'Mamba', 'in-context-learning', 'transformers']
venue: "ICML 2024"
tldr: "Conducts a comparative study showing how well Mamba and other SSMs perform on in-context learning tasks relative to Transformer networks."
---

# Can Mamba Learn How To Learn? A Comparative Study on In-Context Learning Tasks

**Source**: [https://proceedings.mlr.press/v235/park24j.html](https://proceedings.mlr.press/v235/park24j.html)

**TLDR**: Conducts a comparative study showing how well Mamba and other SSMs perform on in-context learning tasks relative to Transformer networks.

## Abstract

State-space models (SSMs), such as Mamba (Gu & Dao, 2023), have been proposed as alternatives to Transformer networks in language modeling, incorporating gating, convolutions, and input-dependent token selection to mitigate the quadratic cost of multi-head attention. Although SSMs exhibit competitive performance, their in-context learning (ICL) capabilities, a remarkable emergent property of modern language models that enables task execution without parameter optimization, remain less explored compared to Transformers. In this study, we evaluate the ICL performance of SSMs, focusing on Mamba, against Transformer models across various tasks. Our results show that SSMs perform comparably to Transformers in standard regression ICL tasks, while outperforming them in tasks like sparse parity learning. However, SSMs fall short in tasks involving non-standard retrieval functionality. To address these limitations, we introduce a hybrid model, MambaFormer, that combines Mamba with attention blocks, surpassing individual models in tasks where they struggle independently. Our findings suggest that hybrid architectures offer promising avenues for enhancing ICL in language models.