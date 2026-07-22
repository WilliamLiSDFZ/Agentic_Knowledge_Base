---
title: "ICC : Quantifying Image Caption Concreteness for Multimodal Dataset Curation"
source: "https://aclanthology.org/2024.findings-acl.657/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'web-data-quality-and-llm-evaluation']
tags: ['image-caption', 'concreteness', 'multimodal-data-curation']
venue: "ACL 2024"
tldr: "Introduces a metric quantifying image caption concreteness to improve filtering of noisy web-scale text-image datasets for multimodal learning."
---

# ICC : Quantifying Image Caption Concreteness for Multimodal Dataset Curation

**Source**: [https://aclanthology.org/2024.findings-acl.657/](https://aclanthology.org/2024.findings-acl.657/)

**TLDR**: Introduces a metric quantifying image caption concreteness to improve filtering of noisy web-scale text-image datasets for multimodal learning.

## Abstract

AbstractWeb-scale training on paired text-image data is becoming increasingly central to multimodal learning, but is challenged by the highly noisy nature of datasets in the wild. Standard data filtering approaches succeed in removing mismatched text-image pairs, but permit semantically related but highly abstract or subjective text. These approaches lack the fine-grained ability to isolate the most concrete samples that provide the strongest signal for learning in a noisy dataset. In this work, we propose a new metric, Image Caption Concreteness (ICC), that evaluates caption text without an image reference to measure its concreteness and relevancy for use in multimodal learning. Our unsupervised approach leverages strong foundation models for measuring visual-semantic information loss in multimodal representations. We demonstrate that this strongly correlates with human evaluation of concreteness in both single-word and caption-level texts. Moreover, we show that curation using ICC complements existing approaches: It succeeds in selecting the highest quality samples from multimodal web-scale datasets to allow for efficient training in resource-constrained settings.