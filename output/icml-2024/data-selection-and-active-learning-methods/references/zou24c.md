---
title: "Compositional Few-Shot Class-Incremental Learning"
source: "https://proceedings.mlr.press/v235/zou24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zou24c/zou24c.pdf"
categories: ['continual-learning-memory-plasticity', 'data-selection-and-active-learning-methods']
tags: ['few-shot', 'class-incremental-learning', 'compositional-learning', 'continual-learning', 'novel-classes']
venue: "ICML 2024"
tldr: "This paper proposes compositional few-shot class-incremental learning, leveraging human-like compositional recognition to improve continual learning from few examples."
---

# Compositional Few-Shot Class-Incremental Learning

**Source**: [https://proceedings.mlr.press/v235/zou24c.html](https://proceedings.mlr.press/v235/zou24c.html)

**TLDR**: This paper proposes compositional few-shot class-incremental learning, leveraging human-like compositional recognition to improve continual learning from few examples.

## Abstract

Few-shot class-incremental learning (FSCIL) is proposed to continually learn from novel classes with only a few samples after the (pre-)training on base classes with sufficient data. However, this remains a challenge. In contrast, humans can easily recognize novel classes with a few samples. Cognitive science demonstrates that an important component of such human capability is compositional learning. This involves identifying visual primitives from learned knowledge and then composing new concepts using these transferred primitives, making incremental learning both effective and interpretable. To imitate human compositional learning, we propose a cognitive-inspired method for the FSCIL task. We define and build a compositional model based on set similarities, and then equip it with a primitive composition module and a primitive reuse module. In the primitive composition module, we propose to utilize the Centered Kernel Alignment (CKA) similarity to approximate the similarity between primitive sets, allowing the training and evaluation based on primitive compositions. In the primitive reuse module, we enhance primitive reusability by classifying inputs based on primitives replaced with the closest primitives from other classes. Experiments on three datasets validate our method, showing it outperforms current state-of-the-art methods with improved interpretability. Our code is available at https://github.com/Zoilsen/Comp-FSCIL.