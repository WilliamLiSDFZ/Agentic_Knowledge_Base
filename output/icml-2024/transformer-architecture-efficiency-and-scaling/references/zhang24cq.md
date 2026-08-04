---
title: "Accelerating Iterative Retrieval-augmented Language Model Serving with Speculation"
source: "https://proceedings.mlr.press/v235/zhang24cq.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24cq/zhang24cq.pdf"
categories: ['llm-serving-systems-and-infrastructure', 'transformer-architecture-efficiency-and-scaling']
tags: ['retrieval-augmented-generation', 'speculative-retrieval', 'LLM-serving']
venue: "ICML 2024"
tldr: "Introduces RaLMSpec, a framework accelerating iterative retrieval-augmented language model serving via speculative retrieval and batched verification."
---

# Accelerating Iterative Retrieval-augmented Language Model Serving with Speculation

**Source**: [https://proceedings.mlr.press/v235/zhang24cq.html](https://proceedings.mlr.press/v235/zhang24cq.html)

**TLDR**: Introduces RaLMSpec, a framework accelerating iterative retrieval-augmented language model serving via speculative retrieval and batched verification.

## Abstract

This paper introduces RaLMSpec, a framework that accelerates iterative retrieval-augmented language model (RaLM) with speculative retrieval and batched verification. RaLMSpec further introduces several important systems optimizations, including prefetching, optimal speculation stride scheduler, and asynchronous verification. The combination of these techniques allows RaLMSPec to significantly outperform existing systems. For document-level iterative RaLM serving, evaluation over three LLMs on four QA datasets shows that RaLMSpec improves over existing approaches by $1.75$-$2.39\times$, $1.04$-$1.39\times$, and $1.31$-$1.77\times$ when the retriever is an exact dense retriever, approximate dense retriever, and sparse retriever respectively. For token-level iterative RaLM (KNN-LM) serving, RaLMSpec is up to $7.59\times$ and $2.45\times$ faster than existing methods for exact dense and approximate dense retrievers, respectively.