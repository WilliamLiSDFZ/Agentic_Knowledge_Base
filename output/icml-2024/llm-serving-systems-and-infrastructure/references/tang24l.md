---
title: "QUEST: Query-Aware Sparsity for Efficient Long-Context LLM Inference"
source: "https://proceedings.mlr.press/v235/tang24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tang24l/tang24l.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'llm-serving-systems-and-infrastructure']
tags: ['long-context-inference', 'KV-cache', 'query-aware-sparsity']
venue: "ICML 2024"
tldr: "QUEST introduces query-aware sparsity to efficiently handle long-context LLM inference by selectively retrieving relevant KV cache pages."
---

# QUEST: Query-Aware Sparsity for Efficient Long-Context LLM Inference

**Source**: [https://proceedings.mlr.press/v235/tang24l.html](https://proceedings.mlr.press/v235/tang24l.html)

**TLDR**: QUEST introduces query-aware sparsity to efficiently handle long-context LLM inference by selectively retrieving relevant KV cache pages.

## Abstract

As the demand for long-context large language models (LLMs) increases, models with context windows of up to 128K or 1M tokens are becoming increasingly prevalent. However, long-context LLM inference is challenging since the inference speed decreases significantly as the sequence length grows. This slowdown is primarily caused by loading a large KV cache during self-attention. Previous works have shown that a small portion of critical tokens will dominate the attention outcomes. However, we observe the criticality of a token highly depends on the query. To this end, we propose Quest, a query-aware KV cache selection algorithm. Quest keeps track of the minimal and maximal Key values in KV cache pages and estimates the criticality of a given page using Query vectors. By only loading the Top-K critical KV cache pages for attention, Quest significantly speeds up self-attention without sacrificing accuracy. We show that Quest can achieve up to 2.23x self-attention speedup, which reduces inference latency by 7.03x while performing well on tasks with long dependencies with negligible accuracy loss. Code is available at https://github.com/mit-han-lab/quest.