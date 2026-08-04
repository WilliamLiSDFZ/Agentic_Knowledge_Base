---
title: "Trainable Transformer in Transformer"
source: "https://proceedings.mlr.press/v235/panigrahi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/panigrahi24a/panigrahi24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'neural-network-learning-dynamics-theory']
tags: ['in-context-learning', 'transformer', 'meta-learning', 'implicit-fine-tuning']
venue: "ICML 2024"
tldr: "Presents a Trainable Transformer in Transformer construction that reduces memory overhead for simulating internal model fine-tuning during in-context learning."
---

# Trainable Transformer in Transformer

**Source**: [https://proceedings.mlr.press/v235/panigrahi24a.html](https://proceedings.mlr.press/v235/panigrahi24a.html)

**TLDR**: Presents a Trainable Transformer in Transformer construction that reduces memory overhead for simulating internal model fine-tuning during in-context learning.

## Abstract

Recent works attribute the capability of in-context learning (ICL) in large pre-trained language models to implicitly simulating and fine-tuning an internal model (e.g., linear or 2-layer MLP) during inference. However, such constructions require large memory overhead, which makes simulation of more sophisticated internal models intractable. In this work, we propose a new efficient construction, Transformer in Transformer (in short, TINT), that allows a transformer to simulate and fine-tune more complex models during inference (e.g., pre-trained language models). In particular, we introduce innovative approximation techniques that allow a TINT model with less than 2 billion parameters to simulate and fine-tune a 125 million parameter transformer model within a single forward pass. TINT accommodates many common transformer variants and its design ideas also improve the efficiency of past instantiations of simple models inside transformers. We conduct end-to-end experiments to validate the internal fine-tuning procedure of TINT on various language modeling and downstream tasks. For example, even with a limited one-step budget, we observe TINT for a OPT-125M model improves performance by 4 − 16% absolute on average compared to OPT-125M. These findings suggest that large pre-trained language models are capable of performing intricate subroutines. To facilitate further work, a modular and extensible codebase for TINT is included.