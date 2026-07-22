---
title: "RAP: Efficient Text-Video Retrieval with Sparse-and-Correlated Adapter"
source: "https://aclanthology.org/2024.findings-acl.427/"
categories: ['multimodal-language-vision-learning-systems']
tags: ['text-video-retrieval', 'adapter-tuning', 'vision-language-models']
venue: "ACL 2024"
tldr: "Proposes a sparse-and-correlated adapter for efficient text-video retrieval by fine-tuning pretrained vision-language models."
---

# RAP: Efficient Text-Video Retrieval with Sparse-and-Correlated Adapter

**Source**: [https://aclanthology.org/2024.findings-acl.427/](https://aclanthology.org/2024.findings-acl.427/)

**TLDR**: Proposes a sparse-and-correlated adapter for efficient text-video retrieval by fine-tuning pretrained vision-language models.

## Abstract

AbstractText-Video Retrieval (TVR) aims to align relevant video content with natural language queries. To date, most of the state-of-the-art TVR methods learn image-to-video transfer learning based on the large-scale pre-trained vision-language models (e.g., CLIP). However, fully fine-tuning these pre-trained models for TVR incurs prohibitively expensive computation cost. To this end, we propose to conduct efficient text-video Retrieval with a salient-and-correlated AdaPter (RAP), i.e., fine-tuning the pre-trained model with a few parameterized layers. To accommodate the text-video scenario, we equip our RAP with two indispensable characteristics including temporal sparsity and correlation. Specifically, we propose a low-rank modulation module to refine the per-image features from frozen CLIP backbone, which accentuates silent frames within the video features while alleviating temporal redundancy. Besides, we introduce an asynchronous self-attention mechanism which firstly selects top responsive visual patch and augments the correlation modeling between them with learnable temporal and patch offsets. Extensive experiments on four TVR datasets demonstrate that our RAP achieves superior or comparable performance compared to the fully fine-tuned counterpart and other parameter-efficient finetuning methods.