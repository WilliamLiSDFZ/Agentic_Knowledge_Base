---
title: "LQER: Low-Rank Quantization Error Reconstruction for LLMs"
source: "https://proceedings.mlr.press/v235/zhang24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24j/zhang24j.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'large-language-model-alignment-and-capabilities']
tags: ['LLM-quantization', 'low-rank-approximation', 'post-training']
venue: "ICML 2024"
tldr: "LQER combines quantization with low-rank error reconstruction using activation-induced scaling to recover LLM performance after post-training quantization."
---

# LQER: Low-Rank Quantization Error Reconstruction for LLMs

**Source**: [https://proceedings.mlr.press/v235/zhang24j.html](https://proceedings.mlr.press/v235/zhang24j.html)

**TLDR**: LQER combines quantization with low-rank error reconstruction using activation-induced scaling to recover LLM performance after post-training quantization.

## Abstract

Post-training quantization of Large Language Models (LLMs) is challenging. In this work, we introduce Low-rank Quantization Error Reduction (LQER), which combines quantization and low-rank approximation to recover the model capability. LQER leverages an activation-induced scale matrix to drive the singular value distribution of quantization error towards a desirable distribution, which enables nearly-lossless W4A8 quantization on various LLMs and downstream tasks without the need for knowledge distillation, grid search, or gradient-based iterative optimization. Unlike existing methods, the computation pattern of LQER eliminates the need for specialized Scatter and Gather processes to collect high-precision weights from irregular memory locations. Our W4A8 LLMs achieve near-lossless performance on six popular downstream tasks, while using $1.36 \times$ fewer hardware resources than the leading state-of-the-art method. We will open-source our framework at https://github.com/ChengZhang-98/lqer