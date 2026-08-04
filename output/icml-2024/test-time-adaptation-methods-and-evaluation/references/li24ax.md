---
title: "Learning Adaptive and View-Invariant Vision Transformer for Real-Time UAV Tracking"
source: "https://proceedings.mlr.press/v235/li24ax.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24ax/li24ax.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'test-time-adaptation-methods-and-evaluation']
tags: ['vision-transformer', 'UAV-tracking', 'real-time', 'adaptive', 'view-invariant']
venue: "ICML 2024"
tldr: "An adaptive and view-invariant Vision Transformer achieves real-time UAV tracking with constrained computational resources."
---

# Learning Adaptive and View-Invariant Vision Transformer for Real-Time UAV Tracking

**Source**: [https://proceedings.mlr.press/v235/li24ax.html](https://proceedings.mlr.press/v235/li24ax.html)

**TLDR**: An adaptive and view-invariant Vision Transformer achieves real-time UAV tracking with constrained computational resources.

## Abstract

Harnessing transformer-based models, visual tracking has made substantial strides. However, the sluggish performance of current trackers limits their practicality on devices with constrained computational capabilities, especially for real-time unmanned aerial vehicle (UAV) tracking. Addressing this challenge, we introduce AVTrack, an adaptive computation framework tailored to selectively activate transformer blocks for real-time UAV tracking in this work. Our novel Activation Module (AM) dynamically optimizes ViT architecture, selectively engaging relevant components and enhancing inference efficiency without compromising much tracking performance. Moreover, we bolster the effectiveness of ViTs, particularly in addressing challenges arising from extreme changes in viewing angles commonly encountered in UAV tracking, by learning view-invariant representations through mutual information maximization. Extensive experiments on five tracking benchmarks affirm the effectiveness and versatility of our approach, positioning it as a state-of-the-art solution in visual tracking. Code is released at: https://github.com/wuyou3474/AVTrack.