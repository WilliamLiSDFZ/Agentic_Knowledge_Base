---
title: "Revisiting Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning: A Benchmark"
source: "https://proceedings.mlr.press/v235/zhang24ad.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ad/zhang24ad.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'optimization-algorithms-convergence-theory']
tags: ['zeroth-order-optimization', 'LLM-fine-tuning', 'memory-efficiency']
venue: "ICML 2024"
tldr: "Benchmarks zeroth-order optimization methods as memory-efficient alternatives to backpropagation for fine-tuning large language models."
---

# Revisiting Zeroth-Order Optimization for Memory-Efficient LLM Fine-Tuning: A Benchmark

**Source**: [https://proceedings.mlr.press/v235/zhang24ad.html](https://proceedings.mlr.press/v235/zhang24ad.html)

**TLDR**: Benchmarks zeroth-order optimization methods as memory-efficient alternatives to backpropagation for fine-tuning large language models.

## Abstract

In the evolving landscape of natural language processing (NLP), fine-tuning pre-trained Large Language Models (LLMs) with first-order (FO) optimizers like SGD and Adam has become standard. Yet, as LLMs grow in size, the substantial memory overhead from back-propagation (BP) for FO gradient computation presents a significant challenge. Addressing this issue is crucial, especially for applications like on-device training where memory efficiency is paramount. This paper proposes a shift towards BP-free, zeroth-order (ZO) optimization as a solution for reducing memory costs during LLM fine-tuning, building on the initial concept introduced by (Malladi et al., 2023). Unlike traditional ZO-SGD methods, ou让work expands the exploration to a wider array of ZO optimization techniques, through a comprehensive, first-of-its-kind benchmarking study across five LLM families, three task complexities, and five fine-tuning schemes. Our study unveils previously overlooked optimization principles, highlighting the importance of task alignment, the role of the forward gradient method, and the balance between algorithm complexity and fine-tuning performance. We further introduce novel enhancements to ZO optimization, including block-wise descent, hybrid training, and gradient sparsity. Our study offers a promising direction for achieving further memory-efficient LLM fine-tuning. Codes to reproduce all our experiments will be made public.