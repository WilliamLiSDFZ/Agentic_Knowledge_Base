---
title: "Amanda: Adaptively Modality-Balanced Domain Adaptation for Multimodal Emotion Recognition"
source: "https://aclanthology.org/2024.findings-acl.859/"
pdf_url: ""
categories: ['emotion-aware-dialogue-and-empathy-systems', 'multimodal-language-vision-learning-systems']
tags: ['multimodal-emotion-recognition', 'domain-adaptation', 'modality-balance']
venue: "ACL 2024"
tldr: "Proposes Amanda, an adaptively modality-balanced domain adaptation method for multimodal emotion recognition."
---

# Amanda: Adaptively Modality-Balanced Domain Adaptation for Multimodal Emotion Recognition

**Source**: [https://aclanthology.org/2024.findings-acl.859/](https://aclanthology.org/2024.findings-acl.859/)

**TLDR**: Proposes Amanda, an adaptively modality-balanced domain adaptation method for multimodal emotion recognition.

## Abstract

AbstractThis paper investigates unsupervised multimodal domain adaptation for multimodal emotion recognition, which is a solution for data scarcity yet remains under studied. Due to the varying distribution discrepancies of different modalities between source and target domains, the primary challenge lies in how to balance the domain alignment across modalities to guarantee they are all well aligned. To achieve this, we first develop our model based on the information bottleneck theory to learn optimal representation for each modality independently. Then, we align the domains via matching the label distributions and the representations. In order to balance the representation alignment, we propose to minimize a surrogate of the alignment losses, which is equivalent to adaptively adjusting the weights of the modalities throughout training, thus achieving balanced domain alignment across modalities. Overall, the proposed approach features Adaptively modality-balanced domain adaptation, dubbed Amanda, for multimodal emotion recognition. Extensive empirical results on commonly used benchmark datasets demonstrate that Amanda significantly outperforms competing approaches. The code is available at https://github.com/sunjunaimer/Amanda.