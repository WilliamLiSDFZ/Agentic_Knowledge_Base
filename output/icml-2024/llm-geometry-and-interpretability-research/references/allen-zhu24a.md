---
title: "Physics of Language Models: Part 3.1, Knowledge Storage and Extraction"
source: "https://proceedings.mlr.press/v235/allen-zhu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/allen-zhu24a/allen-zhu24a.pdf"
categories: ['llm-geometry-and-interpretability-research', 'large-language-model-alignment-and-capabilities']
tags: ['LLM-knowledge', 'knowledge-extraction', 'question-answering']
venue: "ICML 2024"
tldr: "This paper investigates whether LLMs genuinely store and retrieve world knowledge or rely on surface-level pattern matching during question answering."
---

# Physics of Language Models: Part 3.1, Knowledge Storage and Extraction

**Source**: [https://proceedings.mlr.press/v235/allen-zhu24a.html](https://proceedings.mlr.press/v235/allen-zhu24a.html)

**TLDR**: This paper investigates whether LLMs genuinely store and retrieve world knowledge or rely on surface-level pattern matching during question answering.

## Abstract

Large language models (LLMs) can store a vast amount of world knowledge, often extractable via question-answering (e.g., "What is Abraham Lincoln’s birthday?”). However, do they answer such questions based on exposure to similar questions during training (i.e., cheating), or by genuinely learning to extract knowledge from sources like Wikipedia? In this paper, we investigate this issue using a controlled biography dataset. We find a strong correlation between the model’s ability to extract knowledge and various diversity measures of the training data. Essentially, for knowledge to be reliably extracted, it must be sufficiently augmented (e.g., through paraphrasing, sentence shuffling) during pretraining. Without such augmentation, knowledge may be memorized but not extractable, leading to 0% accuracy, regardless of subsequent instruction fine-tuning. To understand why this occurs, we employ (nearly) linear probing to demonstrate a strong connection between the observed correlation and how the model internally encodes knowledge — whether it is linearly encoded in the hidden embeddings of entity names or distributed across other token embeddings in the training text. This paper provides several key recommendations for LLM pretraining in the industry: (1) rewrite the pretraining data — using small, auxiliary models — to provide knowledge augmentation, and (2) incorporate more instruction-finetuning data into the pretraining stage before it becomes too late.