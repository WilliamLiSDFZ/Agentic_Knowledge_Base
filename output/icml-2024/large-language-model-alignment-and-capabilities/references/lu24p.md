---
title: "SPP: Sparsity-Preserved Parameter-Efficient Fine-Tuning for Large Language Models"
source: "https://proceedings.mlr.press/v235/lu24p.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lu24p/lu24p.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'knowledge-distillation-methods-and-applications']
tags: ['parameter-efficient-fine-tuning', 'sparsity', 'pruning', 'LLM']
venue: "ICML 2024"
tldr: "SPP preserves sparsity during parameter-efficient fine-tuning of large language models to maintain pruning benefits while enabling effective adaptation."
---

# SPP: Sparsity-Preserved Parameter-Efficient Fine-Tuning for Large Language Models

**Source**: [https://proceedings.mlr.press/v235/lu24p.html](https://proceedings.mlr.press/v235/lu24p.html)

**TLDR**: SPP preserves sparsity during parameter-efficient fine-tuning of large language models to maintain pruning benefits while enabling effective adaptation.

## Abstract

Large Language Models (LLMs) have become pivotal in advancing the field of artificial intelligence, yet their immense sizes pose significant challenges for both fine-tuning and deployment. Current post-training pruning methods, while reducing the sizes of LLMs, often fail to maintain their original performance. To address these challenges, this paper introduces SPP, a Sparsity-Preserved Parameter-efficient fine-tuning method. Different from existing post-training pruning approaches that struggle with performance retention, SPP proposes to employ lightweight learnable column and row matrices to optimize sparse LLM weights, keeping the structure and sparsity of pruned pre-trained models intact. By element-wise multiplication and residual addition, SPP ensures the consistency of model sparsity pattern and ratio during both training and weight-merging processes. We demonstrate the effectiveness of SPP by applying it to the LLaMA and LLaMA-2 model families with recent post-training pruning methods. Our results show that SPP significantly enhances the performance of models with different sparsity patterns (i.e. unstructured and N:M sparsity), especially for those with high sparsity ratios (e.g. 75%), making it a promising solution for the efficient fine-tuning of sparse LLMs. Code will be made available at https://github.com/Lucky-Lance/SPP.