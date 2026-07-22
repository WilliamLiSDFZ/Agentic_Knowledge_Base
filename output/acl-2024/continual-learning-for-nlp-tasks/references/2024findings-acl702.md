---
title: "Continual Few-shot Relation Extraction via Adaptive Gradient Correction and Knowledge Decomposition"
source: "https://aclanthology.org/2024.findings-acl.702/"
categories: ['continual-learning-for-nlp-tasks', 'natural-language-processing-information-extraction']
tags: ['continual-learning', 'few-shot', 'relation-extraction', 'catastrophic-forgetting', 'knowledge-decomposition']
venue: "ACL 2024"
tldr: "A continual few-shot relation extraction method using adaptive gradient correction and knowledge decomposition to mitigate catastrophic forgetting."
---

# Continual Few-shot Relation Extraction via Adaptive Gradient Correction and Knowledge Decomposition

**Source**: [https://aclanthology.org/2024.findings-acl.702/](https://aclanthology.org/2024.findings-acl.702/)

**TLDR**: A continual few-shot relation extraction method using adaptive gradient correction and knowledge decomposition to mitigate catastrophic forgetting.

## Abstract

AbstractContinual few-shot relation extraction (CFRE) aims to continually learn new relations with limited samples. However, current methods neglect the instability of embeddings in the process of different task training, which leads to serious catastrophic forgetting. In this paper, we propose the concept of the following degree from the perspective of instability to analyze catastrophic forgetting and design a novel method based on adaptive gradient correction and knowledge decomposition to alleviate catastrophic forgetting. Specifically, the adaptive gradient correction algorithm is designed to limit the instability of embeddings, which adaptively constrains the current gradient to be orthogonal to the embedding space learned from previous tasks. To reduce the instability between samples and prototypes, the knowledge decomposition module decomposes knowledge into general and task-related knowledge from the perspective of model architecture, which is asynchronously optimized during training. Experimental results on two standard benchmarks show that our method outperforms the state-of-the-art CFRE model and effectively improves the following degree of embeddings.