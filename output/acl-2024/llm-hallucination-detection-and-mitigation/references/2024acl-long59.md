---
title: "An Information Bottleneck Perspective for Effective Noise Filtering on Retrieval-Augmented Generation"
source: "https://aclanthology.org/2024.acl-long.59/"
categories: ['llm-hallucination-detection-and-mitigation', 'collaborative-llm-deployment-and-inference-optimization']
tags: ['retrieval-augmented-generation', 'noise-filtering', 'information-bottleneck']
venue: "ACL 2024"
tldr: "Applies information bottleneck perspective to filter noisy retrieved content for retrieval-augmented generation."
---

# An Information Bottleneck Perspective for Effective Noise Filtering on Retrieval-Augmented Generation

**Source**: [https://aclanthology.org/2024.acl-long.59/](https://aclanthology.org/2024.acl-long.59/)

**TLDR**: Applies information bottleneck perspective to filter noisy retrieved content for retrieval-augmented generation.

## Abstract

AbstractRetrieval-augmented generation integrates the capabilities of large language models with relevant information retrieved from an extensive corpus, yet encounters challenges when confronted with real-world noisy data. One recent solution is to train a filter module to find relevant content but only achieve suboptimal noise compression. In this paper, we propose to introduce the information bottleneck theory into retrieval-augmented generation. Our approach involves the filtration of noise by simultaneously maximizing the mutual information between compression and ground output, while minimizing the mutual information between compression and retrieved passage. In addition, we derive the formula of information bottleneck to facilitate its application in novel comprehensive evaluations, the selection of supervised fine-tuning data, and the construction of reinforcement learning rewards. Experimental results demonstrate that our approach achieves significant improvements across various question answering datasets, not only in terms of the correctness of answer generation but also in the conciseness with 2.5% compression rate.