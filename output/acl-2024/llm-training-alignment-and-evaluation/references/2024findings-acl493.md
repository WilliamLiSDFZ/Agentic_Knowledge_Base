---
title: "Towards Unified Task Embeddings Across Multiple Models: Bridging the Gap for Prompt-Based Large Language Models and Beyond"
source: "https://aclanthology.org/2024.findings-acl.493/"
categories: ['language-model-representations-and-embedding-spaces', 'llm-training-alignment-and-evaluation']
tags: ['task-embedding', 'meta-learning', 'prompt-based-LLMs']
venue: "ACL 2024"
tldr: "A framework for unified task embeddings that bridges meta-learning with prompt-based large language models across multiple models."
---

# Towards Unified Task Embeddings Across Multiple Models: Bridging the Gap for Prompt-Based Large Language Models and Beyond

**Source**: [https://aclanthology.org/2024.findings-acl.493/](https://aclanthology.org/2024.findings-acl.493/)

**TLDR**: A framework for unified task embeddings that bridges meta-learning with prompt-based large language models across multiple models.

## Abstract

AbstractTask embedding, a meta-learning technique that captures task-specific information, has gained popularity, especially in areas such as multi-task learning, model editing, and interpretability. However, it faces challenges with the emergence of prompt-guided Large Language Models (LLMs) operating in a gradient-free manner. Existing task embedding methods rely on fine-tuned, task-specific language models, which hinders the adaptability of task embeddings across diverse models, especially prompt-based LLMs. To hardness the potential of task embeddings in the era of LLMs, we propose a framework for unified task embeddings (FUTE), harmonizing task embeddings from various models, including smaller language models and LLMs with varied prompts, within a single vector space. Such uniformity enables comparison and analysis of similarities amongst different models, broadening the scope and utility of existing task embedding methods in multi-model scenarios, while maintaining their performance comparable to architecture-specific methods.