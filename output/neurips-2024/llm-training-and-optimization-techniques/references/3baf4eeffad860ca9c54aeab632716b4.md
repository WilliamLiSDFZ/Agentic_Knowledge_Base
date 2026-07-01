---
title: "Vector Quantization Prompting for Continual Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/3baf4eeffad860ca9c54aeab632716b4-Abstract-Conference.html"
categories: ['graph-neural-networks-and-representation-learning', 'llm-training-and-optimization-techniques']
tags: ['continual-learning', 'vector-quantization', 'prompt-tuning']
venue: "NeurIPS 2024"
tldr: "Uses vector quantization to improve prompt selection and task knowledge encoding in continual learning, reducing catastrophic forgetting."
---

# Vector Quantization Prompting for Continual Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/3baf4eeffad860ca9c54aeab632716b4-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/3baf4eeffad860ca9c54aeab632716b4-Abstract-Conference.html)

**TLDR**: Uses vector quantization to improve prompt selection and task knowledge encoding in continual learning, reducing catastrophic forgetting.

## Abstract

Continual learning requires to overcome catastrophic forgetting when training a single model on a sequence of tasks.   Recent top-performing approaches are prompt-based methods that utilize a set of learnable parameters (i.e., prompts) to encode task knowledge, from which appropriate ones are selected to guide the fixed pre-trained model in generating features tailored to a certain task. However, existing methods rely on predicting prompt identities for prompt selection, where the identity prediction process cannot be optimized with task loss. This limitation leads to sub-optimal prompt selection and inadequate adaptation of pre-trained features for a specific task. Previous efforts have tried to address this by directly generating prompts from input queries instead of selecting from a set of candidates. However, these prompts are continuous, which lack sufficient abstraction for task knowledge representation, making them less effective for continual learning. To address these challenges, we propose VQ-Prompt, a prompt-based continual learning method that incorporates Vector Quantization (VQ) into end-to-end training of a set of discrete prompts.  In this way, VQ-Prompt can optimize the prompt selection process with task loss and meanwhile achieve effective abstraction of task knowledge for continual learning. Extensive experiments show that VQ-Prompt outperforms state-of-the-art continual learning methods across a variety of benchmarks under the challenging class-incremental setting.