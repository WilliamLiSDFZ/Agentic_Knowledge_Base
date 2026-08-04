---
title: "CHAI: Clustered Head Attention for Efficient LLM Inference"
source: "https://proceedings.mlr.press/v235/agarwal24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/agarwal24a/agarwal24a.pdf"
categories: ['llm-serving-systems-and-infrastructure']
tags: ['llm-inference', 'multi-head-attention', 'kv-cache', 'clustering', 'efficiency']
venue: "ICML 2024"
tldr: "CHAI clusters similar attention heads to reduce KV-cache memory and accelerate LLM inference."
---

# CHAI: Clustered Head Attention for Efficient LLM Inference

**Source**: [https://proceedings.mlr.press/v235/agarwal24a.html](https://proceedings.mlr.press/v235/agarwal24a.html)

**TLDR**: CHAI clusters similar attention heads to reduce KV-cache memory and accelerate LLM inference.

## Abstract

Large Language Models (LLMs) with hundreds of billions of parameters have transformed the field of machine learning. However, serving these models at inference time is both compute and memory intensive, where a single request can require multiple GPUs and tens of Gigabytes of memory. Multi-head attention is one of the key components of LLMs, which can for over 50% of LLMs memory and compute requirement. We observe that there is a high amount of redundancy across heads on which tokens they pay attention to. Based on this insight, we propose Clustered HeadAttention ( CHAI ). CHAI combines heads with a high amount of correlation for self-attention at runtime, thus reducing both memory and compute. In our experiments, we show that CHAI is able to reduce the memory requirements for storing K,V cache by up to 21.4% and inference time latency by up to 1.73× without any fine-tuning required. CHAI achieves this with a maximum 3.2% deviation in accuracy across 3 different models (i.e. OPT-66B, LLAMA-7B, LLAMA-33B) and 5 different evaluation datasets.