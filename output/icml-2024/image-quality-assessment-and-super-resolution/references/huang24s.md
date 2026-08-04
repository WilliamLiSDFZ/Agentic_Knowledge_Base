---
title: "MFTN: A Multi-scale Feature Transfer Network Based on IMatchFormer for Hyperspectral Image Super-Resolution"
source: "https://proceedings.mlr.press/v235/huang24s.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24s/huang24s.pdf"
categories: ['image-quality-assessment-and-super-resolution', '3d-vision-and-scene-understanding']
tags: ['hyperspectral-image-super-resolution', 'multi-scale-features', 'transformer']
venue: "ICML 2024"
tldr: "Proposes a multi-scale feature transfer network using IMatchFormer for hyperspectral image super-resolution by fusing LR-HSI and HR-MSI."
---

# MFTN: A Multi-scale Feature Transfer Network Based on IMatchFormer for Hyperspectral Image Super-Resolution

**Source**: [https://proceedings.mlr.press/v235/huang24s.html](https://proceedings.mlr.press/v235/huang24s.html)

**TLDR**: Proposes a multi-scale feature transfer network using IMatchFormer for hyperspectral image super-resolution by fusing LR-HSI and HR-MSI.

## Abstract

Hyperspectral image super-resolution (HISR) aims to fuse a low-resolution hyperspectral image (LR-HSI) with a high-resolution multispectral image (HR-MSI) to obtain a high-resolution hyperspectral image (HR-HSI). Due to some existing HISR methods ignoring the significant feature difference between LR-HSI and HR-MSI, the reconstructed HR-HSI typically exhibits spectral distortion and blurring of spatial texture. To solve this issue, we propose a multi-scale feature transfer network (MFTN) for HISR. Firstly, three multi-scale feature extractors are constructed to extract features of different scales from the input images. Then, a multi-scale feature transfer module (MFTM) consisting of three improved feature matching Transformers (IMatchFormers) is designed to learn the detail features of different scales from HR-MSI by establishing the cross-model feature correlation between LR-HSI and degraded HR-MSI. Finally, a multiscale dynamic aggregation module (MDAM) containing three spectral aware aggregation modules (SAAMs) is constructed to reconstruct the final HR-HSI by gradually aggregating features of different scales. Extensive experimental results on three commonly used datasets demonstrate that the proposed model achieves better performance compared to state- of-the-art (SOTA) methods.