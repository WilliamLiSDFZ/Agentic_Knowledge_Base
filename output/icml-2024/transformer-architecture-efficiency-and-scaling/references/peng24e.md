---
title: "UPOCR: Towards Unified Pixel-Level OCR Interface"
source: "https://proceedings.mlr.press/v235/peng24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/peng24e/peng24e.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'large-language-model-alignment-and-capabilities']
tags: ['OCR', 'unified-interface', 'pixel-level', 'multi-task', 'vision-language']
venue: "ICML 2024"
tldr: "Proposes UPOCR, a unified pixel-level interface that consolidates diverse OCR tasks into a single architecture and training strategy."
---

# UPOCR: Towards Unified Pixel-Level OCR Interface

**Source**: [https://proceedings.mlr.press/v235/peng24e.html](https://proceedings.mlr.press/v235/peng24e.html)

**TLDR**: Proposes UPOCR, a unified pixel-level interface that consolidates diverse OCR tasks into a single architecture and training strategy.

## Abstract

Existing optical character recognition (OCR) methods rely on task-specific designs with divergent paradigms, architectures, and training strategies, which significantly increases the complexity of research and maintenance and hinders the fast deployment in applications. To this end, we propose UPOCR, a simple-yet-effective generalist model for Unified Pixel-level OCR interface. Specifically, the UPOCR unifies the paradigm of diverse OCR tasks as image-to-image transformation and the architecture as a vision Transformer (ViT)-based encoder-decoder with learnable task prompts. The prompts push the general feature representations extracted by the encoder towards task-specific spaces, endowing the decoder with task awareness. Moreover, the model training is uniformly aimed at minimizing the discrepancy between the predicted and ground-truth images regardless of the inhomogeneity among tasks. Experiments are conducted on three pixel-level OCR tasks including text removal, text segmentation, and tampered text detection. Without bells and whistles, the experimental results showcase that the proposed method can simultaneously achieve state-of-the-art performance on three tasks with a unified single model, which provides valuable strategies and insights for future research on generalist OCR models. Code is available at https://github.com/shannanyinxiang/UPOCR.