---
title: "Concept-aware Data Construction Improves In-context Learning of Language Models"
source: "https://aclanthology.org/2024.findings-acl.733/"
pdf_url: ""
categories: ['llm-training-alignment-and-evaluation', 'state-memory-replay-sequence-modeling']
tags: ['in-context-learning', 'concept-awareness', 'data-construction']
venue: "ACL 2024"
tldr: "Shows that concept-aware data construction during training improves in-context learning capabilities of language models."
---

# Concept-aware Data Construction Improves In-context Learning of Language Models

**Source**: [https://aclanthology.org/2024.findings-acl.733/](https://aclanthology.org/2024.findings-acl.733/)

**TLDR**: Shows that concept-aware data construction during training improves in-context learning capabilities of language models.

## Abstract

AbstractMany recent language models (LMs) are capable of in-context learning (ICL), manifested in the LMs’ ability to perform a new task solely from natural-language instruction. Previous work curating in-context learners assumes that ICL emerges from a vast over-parametrization or the scale of multi-task training. However, recent theoretical work attributes the ICL ability to concept-dependent training data and creates functional in-context learners even in small-scale, synthetic settings.In this work, we practically explore this newly identified axis of ICL quality. We propose Concept-aware Training (CoAT), a framework for constructing training scenarios that make it beneficial for the LM to learn to utilize the analogical reasoning concepts from demonstrations. We find that by using CoAT, pre-trained transformers can learn to better utilise new latent concepts from demonstrations and that such ability makes ICL more robust to the functional deficiencies of the previous models. Finally, we show that concept-aware in-context learners are much more effective in in-context learning a majority of unseen tasks compared to traditional instruction tuning, and fare comparably also to previous in-context learners trained in large-scale multitask learning requiring magnitudes of more training data.