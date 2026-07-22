---
title: "M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation"
source: "https://aclanthology.org/2024.findings-acl.137/"
pdf_url: ""
categories: ['language-model-representations-and-embedding-spaces', 'multilingual-text-classification-and-sentiment-analysis']
tags: ['text-embedding', 'multilingual', 'retrieval']
venue: "ACL 2024"
tldr: "M3-Embedding introduces a versatile embedding model supporting multilingual, multi-functional, and multi-granularity text retrieval via self-knowledge distillation."
---

# M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation

**Source**: [https://aclanthology.org/2024.findings-acl.137/](https://aclanthology.org/2024.findings-acl.137/)

**TLDR**: M3-Embedding introduces a versatile embedding model supporting multilingual, multi-functional, and multi-granularity text retrieval via self-knowledge distillation.

## Abstract

AbstractIn this paper, we introduce a new embedding model called M3-Embedding, which is distinguished for its versatility in Multi-Linguality, Multi-Functionality, and Multi-Granularity. It provides a uniform support for the semantic retrieval of more than 100 working languages. It can simultaneously accomplish the three common retrieval functionalities: dense retrieval, multi-vector retrieval, and sparse retrieval. Besides, it is also capable of processing inputs of different granularities, spanning from short sentences to long documents of up to 8,192 tokens. The effective training of M3-Embedding presents a series of technical contributions. Notably, we propose a novel self-knowledge distillation approach, where the relevance scores from different retrieval functionalities can be integrated as the teacher signal to enhance the training quality. We also optimize the batching strategy, which enables a large batch size and high training throughput to improve the discriminativeness of embeddings. M3-Embedding exhibits a superior performance in our experiment, leading to new state-of-the-art results on multilingual, cross-lingual, and long-document retrieval benchmarks.