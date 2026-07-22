---
title: "ETAS: Zero-Shot Transformer Architecture Search via Network Trainability and Expressivity"
source: "https://aclanthology.org/2024.findings-acl.405/"
pdf_url: ""
categories: ['transformer-architecture-analysis-and-design', 'llm-training-alignment-and-evaluation']
tags: ['transformer-architecture-search', 'zero-shot', 'trainability']
venue: "ACL 2024"
tldr: "Introduces ETAS, a zero-shot transformer architecture search method evaluating architectures via trainability and expressivity metrics."
---

# ETAS: Zero-Shot Transformer Architecture Search via Network Trainability and Expressivity

**Source**: [https://aclanthology.org/2024.findings-acl.405/](https://aclanthology.org/2024.findings-acl.405/)

**TLDR**: Introduces ETAS, a zero-shot transformer architecture search method evaluating architectures via trainability and expressivity metrics.

## Abstract

AbstractTransformer Architecture Search (TAS) methods aim to automate searching for the optimal Transformer architecture configurations for a given task. However, they are impeded by the prohibitive cost of evaluating Transformer architectures. Recently, several Zero-Shot TAS methods have been proposed to mitigate this problem by utilizing zero-cost proxies to evaluate Transformer architectures without training. Unfortunately, they are limited to specific computer vision or natural language processing tasks. Nonetheless, most of them are developed based on empirical observations and lack theoretical guarantees. To solve this problem, we develop a new zero-cost proxy called NTSR that combines two theoretically-inspired indicators to measure the trainability and expressivity of Transformer networks separately. We then integrate it into an effective regularized evolution framework called ETAS to demonstrate its efficacy on various tasks. The results show that our proposed NTSR proxy can consistently achieve a higher correlation with the true performance of Transformer networks on both computer vision and natural language processing tasks. Further, it can significantly accelerate the search process for finding the best-performing Transformer architecture configurations.