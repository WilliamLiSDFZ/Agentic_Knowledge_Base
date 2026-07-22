---
title: "Integrating Pre-Trained Speech and Language Models for End-to-End Speech Recognition"
source: "https://aclanthology.org/2024.findings-acl.787/"
pdf_url: ""
categories: ['speech-and-language-multimodal-generation-systems', 'transformer-architecture-analysis-and-design']
tags: ['ASR', 'speech-recognition', 'pre-trained-models', 'end-to-end', 'integration']
venue: "ACL 2024"
tldr: "Integrates pre-trained speech and language models for end-to-end automatic speech recognition with reduced training data needs."
---

# Integrating Pre-Trained Speech and Language Models for End-to-End Speech Recognition

**Source**: [https://aclanthology.org/2024.findings-acl.787/](https://aclanthology.org/2024.findings-acl.787/)

**TLDR**: Integrates pre-trained speech and language models for end-to-end automatic speech recognition with reduced training data needs.

## Abstract

AbstractAdvances in machine learning have made it possible to perform various text and speech processing tasks, such as automatic speech recognition (ASR), in an end-to-end (E2E) manner. E2E approaches utilizing pre-trained models are gaining attention for conserving training data and resources. However, most of their applications in ASR involve only one of either a pre-trained speech or a language model. This paper proposes integrating a pre-trained speech representation model and a large language model (LLM) for E2E ASR. The proposed model enables the optimization of the entire ASR process, including acoustic feature extraction and acoustic and language modeling, by combining pre-trained models with a bridge network and also enables the application of remarkable developments in LLM utilization, such as parameter-efficient domain adaptation and inference optimization. Experimental results demonstrate that the proposed model achieves a performance comparable to that of modern E2E ASR models by utilizing powerful pre-training models with the proposed integrated approach.