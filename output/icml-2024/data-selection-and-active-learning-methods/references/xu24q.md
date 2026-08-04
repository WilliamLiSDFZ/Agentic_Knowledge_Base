---
title: "Low-Rank Similarity Mining for Multimodal Dataset Distillation"
source: "https://proceedings.mlr.press/v235/xu24q.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24q/xu24q.pdf"
categories: ['data-selection-and-active-learning-methods']
tags: ['dataset-distillation', 'multimodal-learning', 'image-text']
venue: "ICML 2024"
tldr: "Low-rank similarity mining is proposed to distill multimodal image-text datasets by preserving contrastive learning structure across paired modalities."
---

# Low-Rank Similarity Mining for Multimodal Dataset Distillation

**Source**: [https://proceedings.mlr.press/v235/xu24q.html](https://proceedings.mlr.press/v235/xu24q.html)

**TLDR**: Low-rank similarity mining is proposed to distill multimodal image-text datasets by preserving contrastive learning structure across paired modalities.

## Abstract

Though dataset distillation has witnessed rapid development in recent years, the distillation of multimodal data, e.g., image-text pairs, poses unique and under-explored challenges. Unlike unimodal data, image-text contrastive learning (ITC) data lack inherent categorization and should instead place greater emphasis on modality correspondence. In this work, we propose Low-Rank Similarity Mining (LoRS) for multimodal dataset distillation, that concurrently distills a ground truth similarity matrix with image-text pairs, and leverages low-rank factorization for efficiency and scalability. The proposed approach brings significant improvement to the existing algorithms, marking a significant contribution to the field of visual-language dataset distillation. We advocate adopting LoRS as a foundational synthetic data setup for image-text dataset distillation. Our code is available at https://github.com/silicx/LoRS_Distill.