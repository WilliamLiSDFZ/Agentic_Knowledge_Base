---
title: "ViHateT5: Enhancing Hate Speech Detection in Vietnamese With a Unified Text-to-Text Transformer Model"
source: "https://aclanthology.org/2024.findings-acl.355/"
pdf_url: ""
categories: ['hate-speech-and-toxic-content-detection', 'nlp-for-asian-languages']
tags: ['hate-speech-detection', 'vietnamese-nlp', 'text-to-text-transformer']
venue: "ACL 2024"
tldr: "ViHateT5 is a unified T5-based model for Vietnamese hate speech detection that outperforms BERT-based approaches across multiple tasks."
---

# ViHateT5: Enhancing Hate Speech Detection in Vietnamese With a Unified Text-to-Text Transformer Model

**Source**: [https://aclanthology.org/2024.findings-acl.355/](https://aclanthology.org/2024.findings-acl.355/)

**TLDR**: ViHateT5 is a unified T5-based model for Vietnamese hate speech detection that outperforms BERT-based approaches across multiple tasks.

## Abstract

AbstractRecent advancements in hate speech detection (HSD) in Vietnamese have made significant progress, primarily attributed to the emergence of transformer-based pre-trained language models, particularly those built on the BERT architecture. However, the necessity for specialized fine-tuned models has resulted in the complexity and fragmentation of developing a multitasking HSD system. Moreover, most current methodologies focus on fine-tuning general pre-trained models, primarily trained on formal textual datasets like Wikipedia, which may not accurately capture human behavior on online platforms. In this research, we introduce ViHateT5, a T5-based model pre-trained on our proposed large-scale domain-specific dataset named VOZ-HSD. By harnessing the power of a text-to-text architecture, ViHateT5 can tackle multiple tasks using a unified model and achieve state-of-the-art performance across all standard HSD benchmarks in Vietnamese. Our experiments also underscore the significance of label distribution in pre-training data on model efficacy. We provide our experimental materials for research purposes, including the VOZ-HSD dataset, pre-trained checkpoint, the unified HSD-multitask ViHateT5 model, and related source code on GitHub publicly.