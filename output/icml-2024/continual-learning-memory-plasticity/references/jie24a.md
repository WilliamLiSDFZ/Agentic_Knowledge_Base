---
title: "Memory-Space Visual Prompting for Efficient Vision-Language Fine-Tuning"
source: "https://proceedings.mlr.press/v235/jie24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jie24a/jie24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'continual-learning-memory-plasticity']
tags: ['visual-prompting', 'vision-language-models', 'efficient-fine-tuning', 'memory-space']
venue: "ICML 2024"
tldr: "Memory-space visual prompting integrates visual prompts into the memory space of language models for efficient vision-language fine-tuning."
---

# Memory-Space Visual Prompting for Efficient Vision-Language Fine-Tuning

**Source**: [https://proceedings.mlr.press/v235/jie24a.html](https://proceedings.mlr.press/v235/jie24a.html)

**TLDR**: Memory-space visual prompting integrates visual prompts into the memory space of language models for efficient vision-language fine-tuning.

## Abstract

Current solutions for efficiently constructing large vision-language (VL) models follow a two-step paradigm: projecting the output of pre-trained vision encoders to the input space of pre-trained language models as visual prompts; and then transferring the models to downstream VL tasks via end-to-end parameter-efficient fine-tuning (PEFT). However, this paradigm still exhibits inefficiency since it significantly increases the input length of the language models. In this paper, in contrast to integrating visual prompts into inputs, we regard visual prompts as additional knowledge that facilitates language models in addressing tasks associated with visual information. Motivated by the finding that Feed-Forward Network (FFN) of language models acts as "key-value memory", we introduce a novel approach termed memory-space visual prompting (MemVP), wherein visual prompts are concatenated with the weights of FFN for visual knowledge injection. Experimental results across various VL tasks and language models reveal that MemVP significantly reduces the training time and inference latency of the finetuned VL models and surpasses the performance of previous PEFT methods.