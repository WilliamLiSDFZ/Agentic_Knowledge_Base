---
title: "Variance-reduced Zeroth-Order Methods for Fine-Tuning Language Models"
source: "https://proceedings.mlr.press/v235/gautam24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gautam24a/gautam24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'large-language-model-alignment-and-capabilities']
tags: ['zeroth-order-optimization', 'fine-tuning', 'language-models']
venue: "ICML 2024"
tldr: "Proposes variance-reduced zeroth-order optimization methods for memory-efficient fine-tuning of large language models."
---

# Variance-reduced Zeroth-Order Methods for Fine-Tuning Language Models

**Source**: [https://proceedings.mlr.press/v235/gautam24a.html](https://proceedings.mlr.press/v235/gautam24a.html)

**TLDR**: Proposes variance-reduced zeroth-order optimization methods for memory-efficient fine-tuning of large language models.

## Abstract

Fine-tuning language models (LMs) has demonstrated success in a wide array of downstream tasks. However, as LMs are scaled up, the memory requirements for backpropagation become prohibitively high. Zeroth-order (ZO) optimization methods can leverage memory-efficient forward passes to estimate gradients. More recently, MeZO, an adaptation of ZO-SGD, has been shown to consistently outperform zero-shot and in-context learning when combined with suitable task prompts. In this work, we couple ZO methods with variance reduction techniques to enhance stability and convergence for inference-based LM fine-tuning. We introduce Memory-Efficient Zeroth-Order Stochastic Variance-Reduced Gradient (MeZO-SVRG) and demonstrate its efficacy across multiple LM fine-tuning tasks, eliminating the reliance on task-specific prompts. Evaluated across a range of both masked and autoregressive LMs on benchmark GLUE tasks, MeZO-SVRG outperforms MeZO with up to 20% increase in test accuracies in both full- and partial-parameter fine-tuning settings. MeZO-SVRG benefits from reduced computation time as it often surpasses MeZO’s peak test accuracy with a $2\times$ reduction in GPU-hours. MeZO-SVRG significantly reduces the required memory footprint compared to first-order SGD, i.e. by $2\times$ for autoregressive models. Our experiments highlight that MeZO-SVRG’s memory savings progressively improve compared to SGD with larger batch sizes.