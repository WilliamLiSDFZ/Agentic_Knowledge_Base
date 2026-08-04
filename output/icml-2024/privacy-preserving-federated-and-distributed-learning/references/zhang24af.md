---
title: "DPZero: Private Fine-Tuning of Language Models without Backpropagation"
source: "https://proceedings.mlr.press/v235/zhang24af.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24af/zhang24af.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'large-language-model-alignment-and-capabilities']
tags: ['differential-privacy', 'LLM-fine-tuning', 'zeroth-order-optimization']
venue: "ICML 2024"
tldr: "A privacy-preserving LLM fine-tuning method using zeroth-order optimization that eliminates backpropagation and satisfies differential privacy."
---

# DPZero: Private Fine-Tuning of Language Models without Backpropagation

**Source**: [https://proceedings.mlr.press/v235/zhang24af.html](https://proceedings.mlr.press/v235/zhang24af.html)

**TLDR**: A privacy-preserving LLM fine-tuning method using zeroth-order optimization that eliminates backpropagation and satisfies differential privacy.

## Abstract

The widespread practice of fine-tuning large language models (LLMs) on domain-specific data faces two major challenges in memory and privacy. First, as the size of LLMs continues to grow, the memory demands of gradient-based training methods via backpropagation become prohibitively high. Second, given the tendency of LLMs to memorize training data, it is important to protect potentially sensitive information in the fine-tuning data from being regurgitated. Zeroth-order methods, which rely solely on forward passes, substantially reduce memory consumption during training. However, directly combining them with standard differentially private gradient descent suffers more as model size grows. To bridge this gap, we introduce DPZero, a novel private zeroth-order algorithm with nearly dimension-independent rates. The memory efficiency of DPZero is demonstrated in privately fine-tuning RoBERTa and OPT on several downstream tasks. Our code is available at https://github.com/Liang137/DPZero.