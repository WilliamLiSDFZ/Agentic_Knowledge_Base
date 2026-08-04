---
title: "Discrete Latent Perspective Learning for Segmentation and Detection"
source: "https://proceedings.mlr.press/v235/ji24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ji24e/ji24e.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'continual-learning-memory-plasticity']
tags: ['perspective-invariant-learning', 'segmentation', 'detection', 'discrete-latent']
venue: "ICML 2024"
tldr: "A discrete latent perspective learning framework enables networks to achieve consistent semantic interpretation across varying viewpoints for segmentation and detection tasks."
---

# Discrete Latent Perspective Learning for Segmentation and Detection

**Source**: [https://proceedings.mlr.press/v235/ji24e.html](https://proceedings.mlr.press/v235/ji24e.html)

**TLDR**: A discrete latent perspective learning framework enables networks to achieve consistent semantic interpretation across varying viewpoints for segmentation and detection tasks.

## Abstract

In this paper, we address the challenge of Perspective-Invariant Learning in machine learning and computer vision, which involves enabling a network to understand images from varying perspectives to achieve consistent semantic interpretation. While standard approaches rely on the labor-intensive collection of multi-view images or limited data augmentation techniques, we propose a novel framework, Discrete Latent Perspective Learning (DLPL), for latent multi-perspective fusion learning using conventional single-view images. DLPL comprises three main modules: Perspective Discrete Decomposition (PDD), Perspective Homography Transformation (PHT), and Perspective Invariant Attention (PIA), which work together to discretize visual features, transform perspectives, and fuse multi-perspective semantic information, respectively. DLPL is a universal perspective learning framework applicable to a variety of scenarios and vision tasks. Extensive experiments demonstrate that DLPL significantly enhances the network’s capacity to depict images across diverse scenarios (daily photos, UAV, auto-driving) and tasks (detection, segmentation).