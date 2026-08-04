---
title: "Understanding Retrieval-Augmented Task Adaptation for Vision-Language Models"
source: "https://proceedings.mlr.press/v235/ming24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ming24a/ming24a.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'information-retrieval-and-recommendation-systems']
tags: ['vision-language-models', 'retrieval-augmented-adaptation', 'CLIP']
venue: "ICML 2024"
tldr: "Analyzes retrieval-augmented task adaptation for vision-language models to improve fine-grained category recognition beyond pre-training distribution."
---

# Understanding Retrieval-Augmented Task Adaptation for Vision-Language Models

**Source**: [https://proceedings.mlr.press/v235/ming24a.html](https://proceedings.mlr.press/v235/ming24a.html)

**TLDR**: Analyzes retrieval-augmented task adaptation for vision-language models to improve fine-grained category recognition beyond pre-training distribution.

## Abstract

Pre-trained contrastive vision-language models have demonstrated remarkable performance across a wide range of tasks. However, they often struggle on fine-trained datasets with categories not adequately represented during pre-training, which makes adaptation necessary. Recent works have shown promising results by utilizing samples from web-scale databases for retrieval-augmented adaptation, especially in low-data regimes. Despite the empirical success, understanding how retrieval impacts the adaptation of vision-language models remains an open research question. In this work, we adopt a reflective perspective by presenting a systematic study to understand the roles of key components in retrieval-augmented adaptation. We unveil new insights on uni-modal and cross-modal retrieval and highlight the critical role of logit ensemble for effective adaptation. We further present theoretical underpinnings that directly support our empirical observations.