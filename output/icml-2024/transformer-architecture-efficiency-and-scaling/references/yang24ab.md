---
title: "Gated Linear Attention Transformers with Hardware-Efficient Training"
source: "https://proceedings.mlr.press/v235/yang24ab.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24ab/yang24ab.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'sequence-models-for-memory-and-state']
tags: ['linear-attention', 'gated-attention', 'hardware-efficient']
venue: "ICML 2024"
tldr: "Gated linear attention transformers that achieve hardware-efficient training while maintaining RNN-compatible inference and improving over standard linear attention."
---

# Gated Linear Attention Transformers with Hardware-Efficient Training

**Source**: [https://proceedings.mlr.press/v235/yang24ab.html](https://proceedings.mlr.press/v235/yang24ab.html)

**TLDR**: Gated linear attention transformers that achieve hardware-efficient training while maintaining RNN-compatible inference and improving over standard linear attention.

## Abstract

Transformers with linear attention allow for efficient parallel training but can simultaneously be formulated as an RNN with 2D (matrix-valued) hidden states, thus enjoying linear-time inference complexity. However, linear attention generally underperforms ordinary softmax attention. Moreover, current implementations of linear attention lack I/O-awareness and are thus slower than highly optimized implementations of softmax attention. This work describes a hardware-efficient algorithm for linear attention that trades off memory movement against parallelizability. The resulting implementation, dubbed FlashLinearAttention, is faster than FlashAttention-2 as a standalone layer even on short sequence lengths (e.g., 1K). We then generalize this algorithm to a more expressive variant of linear attention with data-dependent gates. When used as a replacement for the standard attention layer in Transformers, the resulting gated linear attention (GLA) Transformer is found to perform competitively against the LLaMA-architecture Transformer as well recent linear-time-inference baselines such as RetNet and Mamba on moderate-scale language modeling experiments. GLA Transformer is especially effective at length generalization, enabling a model trained on 2K to generalize to sequences longer than 20K without significant perplexity degradations. For training speed, the GLA Transformer has higher throughput than a similarly-sized Mamba model.