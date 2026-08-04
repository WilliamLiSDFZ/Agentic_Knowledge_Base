---
title: "LoRA Training in the NTK Regime has No Spurious Local Minima"
source: "https://proceedings.mlr.press/v235/jang24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jang24d/jang24d.pdf"
categories: ['neural-network-learning-dynamics-theory', 'transformer-architecture-efficiency-and-scaling']
tags: ['LoRA', 'fine-tuning', 'NTK-regime', 'optimization-landscape', 'low-rank-adaptation']
venue: "ICML 2024"
tldr: "This work proves that LoRA fine-tuning in the NTK regime has no spurious local minima, providing theoretical guarantees for parameter-efficient LLM fine-tuning."
---

# LoRA Training in the NTK Regime has No Spurious Local Minima

**Source**: [https://proceedings.mlr.press/v235/jang24d.html](https://proceedings.mlr.press/v235/jang24d.html)

**TLDR**: This work proves that LoRA fine-tuning in the NTK regime has no spurious local minima, providing theoretical guarantees for parameter-efficient LLM fine-tuning.

## Abstract

Low-rank adaptation (LoRA) has become the standard approach for parameter-efficient fine-tuning of large language models (LLM), but our theoretical understanding of LoRA has been limited. In this work, we theoretically analyze LoRA fine-tuning in the neural tangent kernel (NTK) regime with $N$ data points, showing: (i) full fine-tuning (without LoRA) admits a low-rank solution of rank $r\lesssim \sqrt{N}$; (ii) using LoRA with rank $r\gtrsim \sqrt{N}$ eliminates spurious local minima, allowing gradient descent to find the low-rank solutions; (iii) the low-rank solution found using LoRA generalizes well.