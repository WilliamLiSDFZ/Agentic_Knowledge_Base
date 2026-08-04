---
title: "Cascade-CLIP: Cascaded Vision-Language Embeddings Alignment for Zero-Shot Semantic Segmentation"
source: "https://proceedings.mlr.press/v235/li24aq.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24aq/li24aq.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'graph-neural-networks-and-topology']
tags: ['CLIP', 'zero-shot', 'semantic-segmentation', 'cascaded-alignment', 'vision-language']
venue: "ICML 2024"
tldr: "Cascade-CLIP aligns vision-language embeddings across multiple layers for improved zero-shot semantic segmentation."
---

# Cascade-CLIP: Cascaded Vision-Language Embeddings Alignment for Zero-Shot Semantic Segmentation

**Source**: [https://proceedings.mlr.press/v235/li24aq.html](https://proceedings.mlr.press/v235/li24aq.html)

**TLDR**: Cascade-CLIP aligns vision-language embeddings across multiple layers for improved zero-shot semantic segmentation.

## Abstract

Pre-trained vision-language models, e.g., CLIP, have been successfully applied to zero-shot semantic segmentation. Existing CLIP-based approaches primarily utilize visual features from the last layer to align with text embeddings, while they neglect the crucial information in intermediate layers that contain rich object details. However, we find that directly aggregating the multi-level visual features weakens the zero-shot ability for novel classes. The large differences between the visual features from different layers make these features hard to align well with the text embeddings. We resolve this problem by introducing a series of independent decoders to align the multi-level visual features with the text embeddings in a cascaded way, forming a novel but simple framework named Cascade-CLIP. Our Cascade-CLIP is flexible and can be easily applied to existing zero-shot semantic segmentation methods. Experimental results show that our simple Cascade-CLIP achieves superior zero-shot performance on segmentation benchmarks, like COCO-Stuff, Pascal-VOC, and Pascal-Context. Our code is available at https://github.com/HVision-NKU/Cascade-CLIP.