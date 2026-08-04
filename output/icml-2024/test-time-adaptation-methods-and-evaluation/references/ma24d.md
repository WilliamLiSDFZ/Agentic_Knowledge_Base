---
title: "Learning Modality Knowledge Alignment for Cross-Modality Transfer"
source: "https://proceedings.mlr.press/v235/ma24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24d/ma24d.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'continual-learning-memory-plasticity']
tags: ['cross-modality-transfer', 'knowledge-alignment', 'pretrained-models', 'fine-tuning']
venue: "ICML 2024"
tldr: "A modality knowledge alignment approach improves cross-modality transfer by understanding and leveraging inter-modal knowledge relationships."
---

# Learning Modality Knowledge Alignment for Cross-Modality Transfer

**Source**: [https://proceedings.mlr.press/v235/ma24d.html](https://proceedings.mlr.press/v235/ma24d.html)

**TLDR**: A modality knowledge alignment approach improves cross-modality transfer by understanding and leveraging inter-modal knowledge relationships.

## Abstract

Cross-modality transfer aims to leverage large pretrained models to complete tasks that may not belong to the modality of pretraining data. Existing works achieve certain success in extending classical finetuning to cross-modal scenarios, yet we still lack understanding about the influence of modality gap on the transfer. In this work, a series of experiments focusing on the source representation quality during transfer are conducted, revealing the connection between larger modality gap and lesser knowledge reuse which means ineffective transfer. We then formalize the gap as the knowledge misalignment between modalities using conditional distribution $P(Y|X)$. Towards this problem, we present Modality kNowledge Alignment (MoNA), a meta-learning approach that learns target data transformation to reduce the modality knowledge discrepancy ahead of the transfer. Experiments show that the approach significantly improves upon cross-modal finetuning methods, and most importantly leads to better reuse of source modality knowledge.