---
title: "PruNeRF: Segment-Centric Dataset Pruning via 3D Spatial Consistency"
source: "https://proceedings.mlr.press/v235/jung24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jung24b/jung24b.pdf"
categories: ['3d-vision-and-scene-understanding', 'data-selection-and-active-learning-methods']
tags: ['NeRF', 'dataset-pruning', '3D-consistency', 'distractors']
venue: "ICML 2024"
tldr: "Introduces segment-centric dataset pruning using 3D spatial consistency to make NeRF robust to distractors in training images."
---

# PruNeRF: Segment-Centric Dataset Pruning via 3D Spatial Consistency

**Source**: [https://proceedings.mlr.press/v235/jung24b.html](https://proceedings.mlr.press/v235/jung24b.html)

**TLDR**: Introduces segment-centric dataset pruning using 3D spatial consistency to make NeRF robust to distractors in training images.

## Abstract

Neural Radiance Fields (NeRF) have shown remarkable performance in learning 3D scenes. However, NeRF exhibits vulnerability when confronted with distractors in the training images – unexpected objects are present only within specific views, such as moving entities like pedestrians or birds. Excluding distractors during dataset construction is a straightforward solution, but without prior knowledge of their types and quantities, it becomes prohibitively expensive. In this paper, we propose PruNeRF, a segment-centric dataset pruning framework via 3D spatial consistency, that effectively identifies and prunes the distractors. We first examine existing metrics for measuring pixel-wise distraction and introduce Influence Functions for more accurate measurements. Then, we assess 3D spatial consistency using a depth-based reprojection technique to obtain 3D-aware distraction. Furthermore, we incorporate segmentation for pixel-to-segment refinement, enabling more precise identification. Our experiments on benchmark datasets demonstrate that PruNeRF consistently outperforms state-of-the-art methods in robustness against distractors.