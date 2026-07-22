---
title: "On the Language Encoder of Contrastive Cross-modal Models"
source: "https://aclanthology.org/2024.findings-acl.293/"
categories: ['multimodal-language-vision-learning-systems', 'language-model-representations-and-embedding-spaces']
tags: ['CLIP', 'language-encoder', 'cross-modal']
venue: "ACL 2024"
tldr: "Investigates and improves the language encoder component in contrastive cross-modal models like CLIP and CLAP."
---

# On the Language Encoder of Contrastive Cross-modal Models

**Source**: [https://aclanthology.org/2024.findings-acl.293/](https://aclanthology.org/2024.findings-acl.293/)

**TLDR**: Investigates and improves the language encoder component in contrastive cross-modal models like CLIP and CLAP.

## Abstract

AbstractContrastive cross-modal models such as CLIP and CLAP aid various vision-language (VL) and audio-language (AL) tasks. However, there has been limited investigation of and improvement in their language encoder – the central component of encoding natural language descriptions of image/audio into vector representations. We extensively evaluate how unsupervised and supervised sentence embedding training affect language encoder quality and cross-modal task performance. In VL pretraining, we found that sentence embedding training enhances language encoder quality and aids in cross-modal tasks, improving contrastive VL models such as CyCLIP. Sentence embedding training benefits AL tasks when the amount of training data is large. We analyze the representation spaces to understand the strengths of sentence embedding training, and find that it improves text-space uniformity, at the cost of decreased cross-modal alignment.