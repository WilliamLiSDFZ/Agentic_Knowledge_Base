---
title: "Improving fine-grained understanding in image-text pre-training"
source: "https://proceedings.mlr.press/v235/bica24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bica24a/bica24a.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'knowledge-distillation-methods-and-applications']
tags: ['image-text-pretraining', 'contrastive-learning', 'fine-grained', 'multimodal']
venue: "ICML 2024"
tldr: "SPARC is a simple fine-grained contrastive alignment method for image-text pretraining that groups image patches per token to learn better multimodal representations."
---

# Improving fine-grained understanding in image-text pre-training

**Source**: [https://proceedings.mlr.press/v235/bica24a.html](https://proceedings.mlr.press/v235/bica24a.html)

**TLDR**: SPARC is a simple fine-grained contrastive alignment method for image-text pretraining that groups image patches per token to learn better multimodal representations.

## Abstract

We introduce SPARse fine-grained Contrastive alignment (SPARC), a simple method for pretraining more fine-grained multimodal representations from image-text pairs. Given that multiple image patches often correspond to single words, we propose to learn a grouping of image patches for every token in the caption. To achieve this, we use a sparse similarity metric between image patches and language tokens and compute for each token a language-grouped vision embedding as the weighted average of patches. The token and language-grouped vision embeddings are then contrasted through a fine-grained sequence-wise loss that only depends on individual samples and does not require other batch samples as negatives, i.e., more detailed information is encoded in a computationally inexpensive way. SPARC combines this fine-grained loss with a contrastive loss between global image and text embeddings to learn representations that simultaneously encode global and local information. We thoroughly evaluate SPARC and show improved performance over competing approaches both on image-level tasks relying on coarse-grained information, e.g. classification, as well as region-level tasks relying on fine-grained information, e.g., retrieval, object detection, segmentation while also improving model faithfulness and captioning in foundational vision-language models.