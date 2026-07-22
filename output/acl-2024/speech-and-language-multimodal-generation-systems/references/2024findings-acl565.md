---
title: "Revisiting Interpolation Augmentation for Speech-to-Text Generation"
source: "https://aclanthology.org/2024.findings-acl.565/"
categories: ['speech-and-language-multimodal-generation-systems', 'continual-learning-for-nlp-tasks']
tags: ['speech-to-text', 'interpolation-augmentation', 'low-resource']
venue: "ACL 2024"
tldr: "Revisits interpolation-based data augmentation for speech-to-text generation in low-resource scenarios to improve system generalization."
---

# Revisiting Interpolation Augmentation for Speech-to-Text Generation

**Source**: [https://aclanthology.org/2024.findings-acl.565/](https://aclanthology.org/2024.findings-acl.565/)

**TLDR**: Revisits interpolation-based data augmentation for speech-to-text generation in low-resource scenarios to improve system generalization.

## Abstract

AbstractSpeech-to-text (S2T) generation systems frequently face challenges in low-resource scenarios, primarily due to the lack of extensive labeled datasets. One emerging solution is constructing virtual training samples by interpolating inputs and labels, which has notably enhanced system generalization in other domains. Despite its potential, this technique’s application in S2T tasks has remained under-explored. In this paper, we delve into the utility of interpolation augmentation, guided by several pivotal questions. Our findings reveal that employing an appropriate strategy in interpolation augmentation significantly enhances performance across diverse tasks, architectures, and data scales, offering a promising avenue for more robust S2T systems in resource-constrained settings.