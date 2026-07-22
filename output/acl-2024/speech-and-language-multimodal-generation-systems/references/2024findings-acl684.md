---
title: "CLASP: Cross-modal Alignment Using Pre-trained Unimodal Models"
source: "https://aclanthology.org/2024.findings-acl.684/"
categories: ['multimodal-language-vision-learning-systems', 'speech-and-language-multimodal-generation-systems']
tags: ['speech-text-alignment', 'cross-modal', 'unimodal-pretraining']
venue: "ACL 2024"
tldr: "Introduces CLASP, a cross-modal alignment framework that leverages pre-trained unimodal models without requiring parallel speech-text data."
---

# CLASP: Cross-modal Alignment Using Pre-trained Unimodal Models

**Source**: [https://aclanthology.org/2024.findings-acl.684/](https://aclanthology.org/2024.findings-acl.684/)

**TLDR**: Introduces CLASP, a cross-modal alignment framework that leverages pre-trained unimodal models without requiring parallel speech-text data.

## Abstract

AbstractRecent advancements in joint speech-text pre-training have significantly advanced the processing of natural language. However, a key limitation is their reliance on parallel speech-text data, posing challenges due to data accessibility. Addressing this, our paper introduces an innovative framework for jointly performing speech and text processing without parallel corpora during pre-training but only downstream. Utilizing pre-trained unimodal models, we extract distinct representations for speech and text, aligning them effectively in a newly defined space using a multi-level contrastive learning mechanism. A unique swap reconstruction mechanism enhances the alignment and is followed by fusion via a multi-head mechanism, seamlessly merging modality-invariant and modality-specific representations. Testing for emotion recognition (SLU task) and idiom usage detection (NLU task) demonstrates robust performance, with commendable robustness to noise in text or speech data.