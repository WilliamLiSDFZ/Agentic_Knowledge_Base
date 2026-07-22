---
title: "emotion2vec: Self-Supervised Pre-Training for Speech Emotion Representation"
source: "https://aclanthology.org/2024.findings-acl.931/"
categories: ['speech-and-language-multimodal-generation-systems', 'emotion-aware-dialogue-and-empathy-systems']
tags: ['speech-emotion', 'self-supervised', 'pre-training', 'emotion-representation', 'universal-model']
venue: "ACL 2024"
tldr: "emotion2vec is a self-supervised pre-trained universal speech emotion representation model using online distillation."
---

# emotion2vec: Self-Supervised Pre-Training for Speech Emotion Representation

**Source**: [https://aclanthology.org/2024.findings-acl.931/](https://aclanthology.org/2024.findings-acl.931/)

**TLDR**: emotion2vec is a self-supervised pre-trained universal speech emotion representation model using online distillation.

## Abstract

AbstractWe propose emotion2vec, a universal speech emotion representation model. emotion2vec is pre-trained on open-source unlabeled emotion data through self-supervised online distillation, combining utterance-level loss and frame-level loss during pre-training. emotion2vec outperforms state-of-the-art pre-trained universal models and emotion specialist models by only training linear layers for the speech emotion recognition task on the mainstream IEMOCAP dataset. In addition, emotion2vec shows consistent improvements among 10 different languages of speech emotion recognition datasets. emotion2vec also shows excellent results on other emotion tasks, such as song emotion recognition, emotion prediction in conversation, and sentiment analysis. Comparison experiments, ablation experiments, and visualization comprehensively demonstrate the universal capability of the proposed emotion2vec. To the best of our knowledge, emotion2vec is the first universal representation model in various emotion-related tasks, filling a gap in the field.