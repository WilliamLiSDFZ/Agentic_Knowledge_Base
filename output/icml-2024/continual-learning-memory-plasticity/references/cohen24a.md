---
title: "Slicedit: Zero-Shot Video Editing With Text-to-Image Diffusion Models Using Spatio-Temporal Slices"
source: "https://proceedings.mlr.press/v235/cohen24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cohen24a/cohen24a.pdf"
categories: ['generative-models-and-variational-inference', 'continual-learning-memory-plasticity']
tags: ['video-editing', 'diffusion-models', 'zero-shot']
venue: "ICML 2024"
tldr: "Proposes Slicedit, a zero-shot video editing method leveraging pretrained text-to-image diffusion models via spatio-temporal slices to enforce temporal consistency."
---

# Slicedit: Zero-Shot Video Editing With Text-to-Image Diffusion Models Using Spatio-Temporal Slices

**Source**: [https://proceedings.mlr.press/v235/cohen24a.html](https://proceedings.mlr.press/v235/cohen24a.html)

**TLDR**: Proposes Slicedit, a zero-shot video editing method leveraging pretrained text-to-image diffusion models via spatio-temporal slices to enforce temporal consistency.

## Abstract

Text-to-image (T2I) diffusion models achieve state-of-the-art results in image synthesis and editing. However, leveraging such pre-trained models for video editing is considered a major challenge. Many existing works attempt to enforce temporal consistency in the edited video through explicit correspondence mechanisms, either in pixel space or between deep features. These methods, however, struggle with strong nonrigid motion. In this paper, we introduce a fundamentally different approach, which is based on the observation that spatiotemporal slices of natural videos exhibit similar characteristics to natural images. Thus, the same T2I diffusion model that is normally used only as a prior on video frames, can also serve as a strong prior for enhancing temporal consistency by applying it on spatiotemporal slices. Based on this observation, we present Slicedit, a method for text-based video editing that utilizes a pre-trained T2I diffusion model to process both spatial and spatiotemporal slices. Our method generates videos that retain the structure and motion of the original video while adhering to the target text. Through extensive experiments, we demonstrate Slicedit’s ability to edit a wide range of real-world videos, confirming its clear advantages compared to existing baselines.