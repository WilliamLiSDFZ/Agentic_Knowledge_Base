---
title: "MinPrompt: Graph-based Minimal Prompt Data Augmentation for Few-shot Question Answering"
source: "https://aclanthology.org/2024.acl-long.16/"
pdf_url: ""
categories: ['educational-question-generation-and-comprehension', 'llm-agents-reasoning-and-planning']
tags: ['few-shot-QA', 'graph-based-augmentation', 'prompt-data-augmentation']
venue: "ACL 2024"
tldr: "Proposes graph-based minimal prompt data augmentation for few-shot question answering with LLMs."
---

# MinPrompt: Graph-based Minimal Prompt Data Augmentation for Few-shot Question Answering

**Source**: [https://aclanthology.org/2024.acl-long.16/](https://aclanthology.org/2024.acl-long.16/)

**TLDR**: Proposes graph-based minimal prompt data augmentation for few-shot question answering with LLMs.

## Abstract

AbstractRecent advances in few-shot question answering (QA) mostly rely on the power of pre-trained large language models (LLMs) and fine-tuning in specific settings. Although the pre-training stage has already equipped LLMs with powerful reasoning capabilities, LLMs still need to be fine-tuned to adapt to specific domains to achieve the best results. In this paper, we propose to select the most informative data for fine-tuning, thereby improving the efficiency of the fine-tuning process with comparative or even better accuracy on the open-domain QA task. We present MinPrompt, a minimal data augmentation framework for open-domain QA based on an approximate graph algorithm and unsupervised question generation. We transform the raw text into a graph structure to build connections between different factual sentences, then apply graph algorithms to identify the minimal set of sentences needed to cover the most information in the raw text. We then generate QA pairs based on the identified sentence subset and train the model on the selected sentences to obtain the final model. Empirical results on several benchmark datasets and theoretical analysis show that MinPrompt is able to achieve comparable or better results than baselines with a high degree of efficiency, bringing consistent improvements in F-1 scores.