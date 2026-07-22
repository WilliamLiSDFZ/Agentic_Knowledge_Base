---
title: "Unsupervised Information Refinement Training of Large Language Models for Retrieval-Augmented Generation"
source: "https://aclanthology.org/2024.acl-long.9/"
pdf_url: ""
categories: ['llm-hallucination-detection-and-mitigation']
tags: ['retrieval-augmented-generation', 'information-refinement', 'unsupervised-training']
venue: "ACL 2024"
tldr: "Proposes unsupervised information refinement training to help LLMs better utilize retrieved documents in RAG pipelines."
---

# Unsupervised Information Refinement Training of Large Language Models for Retrieval-Augmented Generation

**Source**: [https://aclanthology.org/2024.acl-long.9/](https://aclanthology.org/2024.acl-long.9/)

**TLDR**: Proposes unsupervised information refinement training to help LLMs better utilize retrieved documents in RAG pipelines.

## Abstract

AbstractRetrieval-augmented generation (RAG) enhances large language models (LLMs) by incorporating additional information from retrieval. However, studies have shown that LLMs still face challenges in effectively using the retrieved information, even ignore it or be misled by it. The key reason is that the training of LLMs does not clearly make LLMs learn how to utilize input retrieved texts with varied quality. In this paper, we propose a novel perspective that considers the role of LLMs in RAG as “Information Refiner”, which means that regardless of correctness, completeness, or usefulness of retrieved texts, LLMs can consistently integrate knowledge within the retrieved texts and model parameters to generate the texts that are more concise, accurate, and complete than the retrieved texts. To this end, we propose an information refinement training method named INFO-RAG that optimizes LLMs for RAG in an unsupervised manner. INFO-RAG is low-cost and general across various tasks. Extensive experiments on zero-shot prediction of 11 datasets in diverse tasks including Question Answering, Slot-Filling, Language Modeling, Dialogue, and Code Generation show that INFO-RAG improves the performance of LLaMA2 by an average of 9.39% relative points. INFO-RAG also shows advantages in in-context learning and robustness of RAG.