---
title: "Reducing Fine-Tuning Memory Overhead by Approximate and Memory-Sharing Backpropagation"
source: "https://proceedings.mlr.press/v235/yang24u.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24u/yang24u.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'optimization-algorithms-convergence-theory']
tags: ['fine-tuning', 'memory-efficiency', 'backpropagation']
venue: "ICML 2024"
tldr: "A method to reduce fine-tuning memory overhead in large models through approximate and memory-sharing backpropagation for activations and layer normalization."
---

# Reducing Fine-Tuning Memory Overhead by Approximate and Memory-Sharing Backpropagation

**Source**: [https://proceedings.mlr.press/v235/yang24u.html](https://proceedings.mlr.press/v235/yang24u.html)

**TLDR**: A method to reduce fine-tuning memory overhead in large models through approximate and memory-sharing backpropagation for activations and layer normalization.

## Abstract

Fine-tuning pretrained large models to downstream tasks is an important problem, which however suffers from huge memory overhead due to large-scale parameters. This work strives to reduce memory overhead in fine-tuning from perspectives of activation function and layer normalization. To this end, we propose the Approximate Backpropagation (Approx-BP) theory, which provides the theoretical feasibility of decoupling the forward and backward passes. We apply our Approx-BP theory to backpropagation training and derive memory-efficient alternatives of GELU and SiLU activation functions, which use derivative functions of ReLUs in the backward pass while keeping their forward pass unchanged. In addition, we introduce a Memory-Sharing Backpropagation strategy, which enables the activation memory to be shared by two adjacent layers, thereby removing activation memory usage redundancy. Our method neither induces extra computation nor reduces training efficiency. We conduct extensive experiments with pretrained vision and language models, and the results demonstrate that our proposal can reduce up to $\sim$$30%$ of the peak memory usage. Our code is released at github.