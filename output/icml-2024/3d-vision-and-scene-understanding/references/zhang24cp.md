---
title: "Fast Text-to-3D-Aware Face Generation and Manipulation via Direct Cross-modal Mapping and Geometric Regularization"
source: "https://proceedings.mlr.press/v235/zhang24cp.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24cp/zhang24cp.pdf"
categories: ['3d-vision-and-scene-understanding', 'generative-models-and-variational-inference']
tags: ['text-to-3D', 'face-generation', 'cross-modal-mapping']
venue: "ICML 2024"
tldr: "Proposes an end-to-end efficient network for fast text-to-3D-aware face generation and manipulation via direct cross-modal mapping."
---

# Fast Text-to-3D-Aware Face Generation and Manipulation via Direct Cross-modal Mapping and Geometric Regularization

**Source**: [https://proceedings.mlr.press/v235/zhang24cp.html](https://proceedings.mlr.press/v235/zhang24cp.html)

**TLDR**: Proposes an end-to-end efficient network for fast text-to-3D-aware face generation and manipulation via direct cross-modal mapping.

## Abstract

Text-to-3D-aware face (T3D Face) generation and manipulation is an emerging research hot spot in machine learning, which still suffers from low efficiency and poor quality. In this paper, we propose an E*nd-to-End Efficient and Effective network for fast and accurate T3D face generation and manipulation, termed $E^3$-FaceNet. Different from existing complex generation paradigms, $E^3$-FaceNet resorts to a direct mapping from text instructions to 3D-aware visual space. We introduce a novel Style Code Enhancer to enhance cross-modal semantic alignment, alongside an innovative Geometric Regularization* objective to maintain consistency across multi-view generations. Extensive experiments on three benchmark datasets demonstrate that $E^3$-FaceNet can not only achieve picture-like 3D face generation and manipulation, but also improve inference speed by orders of magnitudes. For instance, compared with Latent3D, $E^3$-FaceNet speeds up the five-view generations by almost 470 times, while still exceeding in generation quality. Our code is released at https://github.com/Aria-Zhangjl/E3-FaceNet.