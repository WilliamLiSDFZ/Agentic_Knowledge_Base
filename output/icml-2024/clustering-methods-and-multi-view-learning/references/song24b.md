---
title: "Multimodal Prototyping for cancer survival prediction"
source: "https://proceedings.mlr.press/v235/song24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/song24b/song24b.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'learning-with-imperfect-data-and-bias']
tags: ['multimodal-learning', 'survival-prediction', 'histology', 'transcriptomics']
venue: "ICML 2024"
tldr: "A multimodal prototyping approach is proposed for cancer survival prediction by compressing gigapixel WSIs and transcriptomic profiles into compact prototypes."
---

# Multimodal Prototyping for cancer survival prediction

**Source**: [https://proceedings.mlr.press/v235/song24b.html](https://proceedings.mlr.press/v235/song24b.html)

**TLDR**: A multimodal prototyping approach is proposed for cancer survival prediction by compressing gigapixel WSIs and transcriptomic profiles into compact prototypes.

## Abstract

Multimodal survival methods combining gigapixel histology whole-slide images (WSIs) and transcriptomic profiles are particularly promising for patient prognostication and stratification. Current approaches involve tokenizing the WSIs into smaller patches ($>10^4$ patches) and transcriptomics into gene groups, which are then integrated using a Transformer for predicting outcomes. However, this process generates many tokens, which leads to high memory requirements for computing attention and complicates post-hoc interpretability analyses. Instead, we hypothesize that we can: (1) effectively summarize the morphological content of a WSI by condensing its constituting tokens using morphological prototypes, achieving more than $300\times$ compression; and (2) accurately characterize cellular functions by encoding the transcriptomic profile with biological pathway prototypes, all in an unsupervised fashion. The resulting multimodal tokens are then processed by a fusion network, either with a Transformer or an optimal transport cross-alignment, which now operates with a small and fixed number of tokens without approximations. Extensive evaluation on six cancer types shows that our framework outperforms state-of-the-art methods with much less computation while unlocking new interpretability analyses. The code is available at https://github.com/mahmoodlab/MMP.