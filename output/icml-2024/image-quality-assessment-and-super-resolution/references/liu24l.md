---
title: "ESNet: Evolution and Succession Network for High-Resolution Salient Object Detection"
source: "https://proceedings.mlr.press/v235/liu24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24l/liu24l.pdf"
categories: ['image-quality-assessment-and-super-resolution']
tags: ['salient-object-detection', 'high-resolution', 'two-stage']
venue: "ICML 2024"
tldr: "A two-stage evolution-and-succession network is proposed for high-resolution salient object detection balancing detail preservation and computational efficiency."
---

# ESNet: Evolution and Succession Network for High-Resolution Salient Object Detection

**Source**: [https://proceedings.mlr.press/v235/liu24l.html](https://proceedings.mlr.press/v235/liu24l.html)

**TLDR**: A two-stage evolution-and-succession network is proposed for high-resolution salient object detection balancing detail preservation and computational efficiency.

## Abstract

Preserving details and avoiding high computational costs are the two main challenges for the High-Resolution Salient Object Detection (HRSOD) task. In this paper, we propose a two-stage HRSOD model from the perspective of evolution and succession, including an evolution stage with Low-resolution Location Model (LrLM) and a succession stage with High-resolution Refinement Model (HrRM). The evolution stage achieves detail-preserving salient objects localization on the low-resolution image through the evolution mechanisms on supervision and feature; the succession stage utilizes the shallow high-resolution features to complement and enhance the features inherited from the first stage in a lightweight manner and generate the final high-resolution saliency prediction. Besides, a new metric named Boundary-Detail-aware Mean Absolute Error (${MAE}_{{BD}}$) is designed to evaluate the ability to detect details in high-resolution scenes. Extensive experiments on five datasets demonstrate that our network achieves superior performance at real-time speed (49 FPS) compared to state-of-the-art methods.