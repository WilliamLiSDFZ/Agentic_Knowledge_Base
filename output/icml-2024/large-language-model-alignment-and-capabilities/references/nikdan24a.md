---
title: "RoSA: Accurate Parameter-Efficient Fine-Tuning via Robust Adaptation"
source: "https://proceedings.mlr.press/v235/nikdan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nikdan24a/nikdan24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'transformer-architecture-efficiency-and-scaling']
tags: ['parameter-efficient-fine-tuning', 'robust-PCA', 'LoRA']
venue: "ICML 2024"
tldr: "Proposes RoSA, a parameter-efficient fine-tuning method combining low-rank and sparse adaptations inspired by robust PCA for improved LLM accuracy."
---

# RoSA: Accurate Parameter-Efficient Fine-Tuning via Robust Adaptation

**Source**: [https://proceedings.mlr.press/v235/nikdan24a.html](https://proceedings.mlr.press/v235/nikdan24a.html)

**TLDR**: Proposes RoSA, a parameter-efficient fine-tuning method combining low-rank and sparse adaptations inspired by robust PCA for improved LLM accuracy.

## Abstract

We investigate parameter-efficient fine-tuning (PEFT) methods that can provide good accuracy under limited computational and memory budgets in the context of large language models (LLMs). We present a new PEFT method called Robust Adaptation (RoSA) inspired by robust principal component analysis that jointly trains $\textit{low-rank}$ and highly-sparse components on top of a set of fixed pretrained weights to efficiently approximate the performance of a full-fine-tuning (FFT) solution. Across a series of challenging generative tasks such as grade-school math and SQL query generation, which require fine-tuning for good performance, we show that RoSA outperforms LoRA, pure sparse fine-tuning, and alternative hybrid methods at the same parameter budget, and can even recover the performance of FFT on some tasks. We provide system support for RoSA to complement the training algorithm, specifically in the form of sparse GPU kernels which enable memory- and computationally-efficient training, and show that it is also compatible with low-precision base weights, resulting in the first joint representation combining quantization, low-rank and sparse approximations. Our code is available at https://github.com/IST-DASLab/RoSA.