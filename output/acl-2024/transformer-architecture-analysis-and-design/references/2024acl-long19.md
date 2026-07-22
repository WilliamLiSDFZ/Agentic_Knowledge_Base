---
title: "Expedited Training of Visual Conditioned Language Generation via Redundancy Reduction"
source: "https://aclanthology.org/2024.acl-long.19/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'transformer-architecture-analysis-and-design']
tags: ['vision-language-pretraining', 'redundancy-reduction', 'efficient-training']
venue: "ACL 2024"
tldr: "EVLGen accelerates vision-language model pretraining by reducing redundant visual tokens using frozen LLMs."
---

# Expedited Training of Visual Conditioned Language Generation via Redundancy Reduction

**Source**: [https://aclanthology.org/2024.acl-long.19/](https://aclanthology.org/2024.acl-long.19/)

**TLDR**: EVLGen accelerates vision-language model pretraining by reducing redundant visual tokens using frozen LLMs.

## Abstract

AbstractWe introduce EVLGen, a streamlined framework designed for the pre-training of visually conditioned language generation models with high computational demands, utilizing frozen pre-trained large language models (LLMs). The conventional approach in vision-language pre-training (VLP) typically involves a two-stage optimization process: an initial resource-intensive phase dedicated to general-purpose vision-language representation learning, focused on extracting and consolidating relevant visual features. This is followed by a subsequent phase that emphasizes end-to-end alignment between visual and linguistic modalities. Our novel one-stage, single-loss framework bypasses the computationally demanding first training stage by gradually merging similar visual tokens during training, while avoiding model collapse caused by single-stage training of BLIP-2 type models. The gradual merging process effectively condenses visual information while preserving semantic richness, resulting in rapid convergence without compromising performance. Our experimental findings demonstrate that our approach accelerates the training of vision-language models by a factor of 5 without a noticeable impact on overall performance. Furthermore, we illustrate that our models significantly narrow the performance gap to current vision-language models using only 1/10 of the data. Finally, we showcase how our image-text models can seamlessly adapt to video-conditioned language generation tasks through novel soft attentive temporal token contextualizing modules. Code: https://github.com/yiren-jian/EVLGen