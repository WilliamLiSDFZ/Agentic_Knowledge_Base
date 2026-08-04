---
title: "One Meta-tuned Transformer is What You Need for Few-shot Learning"
source: "https://proceedings.mlr.press/v235/yang24ah.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24ah/yang24ah.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'continual-learning-memory-plasticity']
tags: ['few-shot-learning', 'vision-transformers', 'meta-learning']
venue: "ICML 2024"
tldr: "A meta-tuned transformer framework that achieves strong few-shot image classification by integrating meta-learning with pre-trained vision transformers."
---

# One Meta-tuned Transformer is What You Need for Few-shot Learning

**Source**: [https://proceedings.mlr.press/v235/yang24ah.html](https://proceedings.mlr.press/v235/yang24ah.html)

**TLDR**: A meta-tuned transformer framework that achieves strong few-shot image classification by integrating meta-learning with pre-trained vision transformers.

## Abstract

Pre-trained vision transformers have revolutionized few-shot image classification, and it has been recently demonstrated that the previous common practice of meta-learning in synergy with these pre-trained transformers still holds significance. In this work, we design a new framework centered exclusively on self-attention, called MetaFormer, which extends the vision transformers beyond patch token interactions to encompass relationships between samples and tasks simultaneously for further advancing their downstream task performance. Leveraging the intrinsical property of ViTs in handling local patch relationships, we propose Masked Sample Attention (MSA) to efficiently embed the sample relationships into the network, where an adaptive mask is attached for enhancing task-specific feature consistency and providing flexibility in switching between few-shot learning setups. To encapsulate task relationships while filtering out background noise, Patch-grained Task Attention (PTA) is designed to maintain a dynamic knowledge pool consolidating diverse patterns from historical tasks. MetaFormer demonstrates coherence and compatibility with off-the-shelf pre-trained vision transformers and shows significant improvements in both inductive and transductive few-shot learning scenarios, outperforming state-of-the-art methods by up to 8.77% and 6.25% on 12 in-domain and 10 cross-domain datasets, respectively.