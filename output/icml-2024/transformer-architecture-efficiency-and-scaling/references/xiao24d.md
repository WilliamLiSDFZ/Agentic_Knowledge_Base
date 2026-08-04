---
title: "Improving Transformers with Dynamically Composable Multi-Head Attention"
source: "https://proceedings.mlr.press/v235/xiao24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xiao24d/xiao24d.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'neural-network-learning-dynamics-theory']
tags: ['multi-head-attention', 'transformer', 'dynamic-composition']
venue: "ICML 2024"
tldr: "DCMHA improves transformers by dynamically composing attention heads to address low-rank bottlenecks and head redundancy."
---

# Improving Transformers with Dynamically Composable Multi-Head Attention

**Source**: [https://proceedings.mlr.press/v235/xiao24d.html](https://proceedings.mlr.press/v235/xiao24d.html)

**TLDR**: DCMHA improves transformers by dynamically composing attention heads to address low-rank bottlenecks and head redundancy.

## Abstract

Multi-Head Attention (MHA) is a key component of Transformer. In MHA, attention heads work independently, causing problems such as low-rank bottleneck of attention score matrices and head redundancy. We propose Dynamically Composable Multi-Head Attention (DCMHA), a parameter and computation efficient attention architecture that tackles the shortcomings of MHA and increases the expressive power of the model by dynamically composing attention heads. At the core of DCMHA is a Compose function that transforms the attention score and weight matrices in an input-dependent way. DCMHA can be used as a drop-in replacement of MHA in any transformer architecture to obtain the corresponding DCFormer. DCFormer significantly outperforms Transformer on different architectures and model scales in language modeling, matching the performance of models with 1.7x-2.0x compute. For example, DCPythia-6.9B outperforms open source Pythia-12B on both pretraining perplexity and downstream task evaluation.