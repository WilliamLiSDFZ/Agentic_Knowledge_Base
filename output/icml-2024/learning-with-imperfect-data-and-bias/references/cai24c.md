---
title: "Enhancing Cross-Modal Fine-Tuning with Gradually Intermediate Modality Generation"
source: "https://proceedings.mlr.press/v235/cai24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cai24c/cai24c.pdf"
categories: ['knowledge-distillation-methods-and-applications', 'learning-with-imperfect-data-and-bias']
tags: ['cross-modal-fine-tuning', 'modality-gap', 'intermediate-modality', 'pretrained-models']
venue: "ICML 2024"
tldr: "Proposes gradually generating intermediate modalities to bridge the gap between pretrained model modalities and specialized target modalities for fine-tuning."
---

# Enhancing Cross-Modal Fine-Tuning with Gradually Intermediate Modality Generation

**Source**: [https://proceedings.mlr.press/v235/cai24c.html](https://proceedings.mlr.press/v235/cai24c.html)

**TLDR**: Proposes gradually generating intermediate modalities to bridge the gap between pretrained model modalities and specialized target modalities for fine-tuning.

## Abstract

Large-scale pretrained models have proven immensely valuable in handling data-intensive modalities like text and image. However, fine-tuning these models for certain specialized modalities, such as protein sequence and cosmic ray, poses challenges due to the significant modality discrepancy and scarcity of labeled data. In this paper, we propose an end-to-end method, PaRe, to enhance cross-modal fine-tuning, aiming to transfer a large-scale pretrained model to various target modalities. PaRe employs a gating mechanism to select key patches from both source and target data. Through a modality-agnostic Patch Replacement scheme, these patches are preserved and combined to construct data-rich intermediate modalities ranging from easy to hard. By gradually intermediate modality generation, we can not only effectively bridge the modality gap to enhance stability and transferability of cross-modal fine-tuning, but also address the challenge of limited data in the target modality by leveraging enriched intermediate modality data. Compared with hand-designed, general-purpose, task-specific, and state-of-the-art cross-modal fine-tuning approaches, PaRe demonstrates superior performance across three challenging benchmarks, encompassing more than ten modalities.