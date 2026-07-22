---
title: "Token-wise Influential Training Data Retrieval for Large Language Models"
source: "https://aclanthology.org/2024.acl-long.48/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'language-model-representations-and-embedding-spaces']
tags: ['training-data-influence', 'data-attribution', 'LLM-interpretability', 'token-wise', 'scalability']
venue: "ACL 2024"
tldr: "RapidIn is a scalable framework for efficiently estimating which training data influenced specific LLM token-level generations."
---

# Token-wise Influential Training Data Retrieval for Large Language Models

**Source**: [https://aclanthology.org/2024.acl-long.48/](https://aclanthology.org/2024.acl-long.48/)

**TLDR**: RapidIn is a scalable framework for efficiently estimating which training data influenced specific LLM token-level generations.

## Abstract

AbstractGiven a Large Language Model (LLM) generation, how can we identify which training data led to this generation? In this paper, we proposed RapidIn, a scalable framework adapting to LLMs for estimating the influence of each training data. The proposed framework consists of two stages: caching and retrieval. First, we compress the gradient vectors by over 200,000x, allowing them to be cached on disk or in GPU/CPU memory. Then, given a generation, RapidIn efficiently traverses the cached gradients to estimate the influence within minutes, achieving over a 6,326x speedup. Moreover, RapidIn supports multi-GPU parallelization to substantially accelerate caching and retrieval. Our empirical result confirms the efficiency and effectiveness of RapidIn.