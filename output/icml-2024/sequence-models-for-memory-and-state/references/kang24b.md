---
title: "Think Before You Act: Decision Transformers with Working Memory"
source: "https://proceedings.mlr.press/v235/kang24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kang24b/kang24b.pdf"
categories: ['sequence-models-for-memory-and-state', 'continual-learning-memory-plasticity']
tags: ['decision-transformer', 'working-memory', 'multi-task', 'forgetting']
venue: "ICML 2024"
tldr: "Augments Decision Transformers with a working memory module to mitigate forgetting and improve multi-task decision-making efficiency."
---

# Think Before You Act: Decision Transformers with Working Memory

**Source**: [https://proceedings.mlr.press/v235/kang24b.html](https://proceedings.mlr.press/v235/kang24b.html)

**TLDR**: Augments Decision Transformers with a working memory module to mitigate forgetting and improve multi-task decision-making efficiency.

## Abstract

Decision Transformer-based decision-making agents have shown the ability to generalize across multiple tasks. However, their performance relies on massive data and computation. We argue that this inefficiency stems from the forgetting phenomenon, in which a model memorizes its behaviors in parameters throughout training. As a result, training on a new task may deteriorate the model’s performance on previous tasks. In contrast to LLMs’ implicit memory mechanism, the human brain utilizes distributed memory storage, which helps manage and organize multiple skills efficiently, mitigating the forgetting phenomenon. Inspired by this, we propose a working memory module to store, blend, and retrieve information for different downstream tasks. Evaluation results show that the proposed method improves training efficiency and generalization in Atari games and Meta-World object manipulation tasks. Moreover, we demonstrate that memory fine-tuning further enhances the adaptability of the proposed architecture.