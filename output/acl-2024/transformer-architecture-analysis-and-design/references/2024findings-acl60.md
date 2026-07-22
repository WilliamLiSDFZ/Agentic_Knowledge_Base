---
title: "Finding and Editing Multi-Modal Neurons in Pre-Trained Transformers"
source: "https://aclanthology.org/2024.findings-acl.60/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'transformer-architecture-analysis-and-design']
tags: ['multimodal-neurons', 'model-editing', 'transformers']
venue: "ACL 2024"
tldr: "Identifies and edits multi-modal neurons in pre-trained transformers to understand how vision-language models integrate cross-modal information."
---

# Finding and Editing Multi-Modal Neurons in Pre-Trained Transformers

**Source**: [https://aclanthology.org/2024.findings-acl.60/](https://aclanthology.org/2024.findings-acl.60/)

**TLDR**: Identifies and edits multi-modal neurons in pre-trained transformers to understand how vision-language models integrate cross-modal information.

## Abstract

AbstractUnderstanding the internal mechanisms by which multi-modal large language models (LLMs) interpret different modalities and integrate cross-modal representations is becoming increasingly critical for continuous improvements in both academia and industry. In this paper, we propose a novel method to identify key neurons for interpretability — how multi-modal LLMs bridge visual and textual concepts for captioning. Our method improves conventional works upon efficiency and applied range by removing needs of costly gradient computation. Based on those identified neurons, we further design a multi-modal knowledge editing method, beneficial to mitigate sensitive words or hallucination. For rationale of our design, we provide theoretical assumption. For empirical evaluation, we have conducted extensive quantitative and qualitative experiments. The results not only validate the effectiveness of our methods, but also offer insightful findings that highlight three key properties of multi-modal neurons: sensitivity, specificity and causal-effect, to shed light for future research.