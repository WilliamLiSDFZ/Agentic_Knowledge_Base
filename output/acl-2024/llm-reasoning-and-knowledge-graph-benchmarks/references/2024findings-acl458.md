---
title: "Improving Retrieval Augmented Open-Domain Question-Answering with Vectorized Contexts"
source: "https://aclanthology.org/2024.findings-acl.458/"
categories: ['llm-agents-reasoning-and-planning', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['retrieval-augmented-generation', 'open-domain-qa', 'vectorized-context']
venue: "ACL 2024"
tldr: "Improves retrieval-augmented open-domain QA by using vectorized contexts to overcome context length limitations in large language models."
---

# Improving Retrieval Augmented Open-Domain Question-Answering with Vectorized Contexts

**Source**: [https://aclanthology.org/2024.findings-acl.458/](https://aclanthology.org/2024.findings-acl.458/)

**TLDR**: Improves retrieval-augmented open-domain QA by using vectorized contexts to overcome context length limitations in large language models.

## Abstract

AbstractIn the era of large language models, applying techniques such as Retrieval Augmented Generation can better address Open-Domain Question-Answering problems. Due to constraints including model sizes and computing resources, the length of context is often limited, and it becomes challenging to empower the model to cover overlong contexts while answering questions from open domains. This paper proposes a general and convenient method to cover longer contexts in Open-Domain Question-Answering tasks. %It leverages a small encoder language model that effectively encodes contexts, and the encoding applies cross-attention with origin inputs.It leverages a small encoder and cross-attention mechanism and effectively encodes contexts. With our method, the original language models can cover several times longer contexts while keeping the computing requirements close to the baseline. Our experiments demonstrate that after fine-tuning, there is improved performance across two held-in datasets, four held-out datasets, and also in two In Context Learning settings. Our code will be released at https://github.com/Alibaba-NLP/Vec-RA-ODQA.