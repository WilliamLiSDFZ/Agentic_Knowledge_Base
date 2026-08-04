---
title: "CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers"
source: "https://proceedings.mlr.press/v235/shi24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shi24e/shi24e.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'knowledge-distillation-methods-and-applications']
tags: ['vision-language-transformers', 'token-pruning', 'model-acceleration']
venue: "ICML 2024"
tldr: "CrossGET introduces a cross-guided token ensemble method to accelerate vision-language transformers by efficiently reducing token redundancy across modalities."
---

# CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers

**Source**: [https://proceedings.mlr.press/v235/shi24e.html](https://proceedings.mlr.press/v235/shi24e.html)

**TLDR**: CrossGET introduces a cross-guided token ensemble method to accelerate vision-language transformers by efficiently reducing token redundancy across modalities.

## Abstract

Recent vision-language models have achieved tremendous advances. However, their computational costs are also escalating dramatically, making model acceleration exceedingly critical. To pursue more efficient vision-language Transformers, this paper introduces Cross-Guided Ensemble of Tokens (CrossGET), a general acceleration framework for vision-language Transformers. This framework adaptively combines tokens in real-time during inference, significantly reducing computational costs while maintaining high performance. CrossGET features two primary innovations: 1) Cross-Guided Matching and Ensemble. CrossGET leverages cross-modal guided token matching and ensemble to effectively utilize cross-modal information, achieving wider applicability across both modality-independent models, e.g., CLIP, and modality-dependent ones, e.g., BLIP2. 2) Complete-Graph Soft Matching. CrossGET introduces an algorithm for the token-matching mechanism, ensuring reliable matching results while facilitating parallelizability and high efficiency. Extensive experiments have been conducted on various vision-language tasks, such as image-text retrieval, visual reasoning, image captioning, and visual question answering. The performance on both classic multimodal architectures and emerging multimodal LLMs demonstrates the framework’s effectiveness and versatility. The code is available at https://github.com/sdc17/CrossGET.