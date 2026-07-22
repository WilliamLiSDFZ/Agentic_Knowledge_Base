---
title: "Controllable Text Generation with Residual Memory Transformer"
source: "https://aclanthology.org/2024.findings-acl.62/"
pdf_url: ""
categories: ['state-memory-replay-sequence-modeling', 'llm-training-alignment-and-evaluation']
tags: ['controllable-text-generation', 'residual-memory', 'causal-language-models']
venue: "ACL 2024"
tldr: "A Residual Memory Transformer is proposed to enable flexible, fine-grained controllable text generation in large-scale causal language models."
---

# Controllable Text Generation with Residual Memory Transformer

**Source**: [https://aclanthology.org/2024.findings-acl.62/](https://aclanthology.org/2024.findings-acl.62/)

**TLDR**: A Residual Memory Transformer is proposed to enable flexible, fine-grained controllable text generation in large-scale causal language models.

## Abstract

AbstractLarge-scale Causal Language Models (CLMs), e.g., GPT3 and ChatGPT, have brought great success in text generation. However, it is still an open challenge to effectively control the generation process of a CLM while balancing the flexibility, control granularity, and generation efficiency. In this paper, we provide a new alternative for controllable text generation (CTG), by designing a non-intrusive, lightweight control plugin, namely Residual Memory Transformer (RMT), to accompany the generation of CLM at arbitrary time steps. With an encoder-decoder setup, RMT can accept any types of control conditions and cooperate with the base CLM through a residual learning paradigm, to achieve a more flexible, general, and efficient CTG. Extensive experiments are carried out on various control tasks, in the form of both automatic and human evaluations. The results demonstrate the superiority of RMT over a wide range of state-of-the-art CTG approaches. The code implementation of our work is available at: https://github.com/Residual_Memory_Transformer.