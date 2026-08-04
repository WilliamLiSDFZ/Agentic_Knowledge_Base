---
title: "Learning Scale-Aware Spatio-temporal Implicit Representation for Event-based Motion Deblurring"
source: "https://proceedings.mlr.press/v235/yu24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yu24g/yu24g.pdf"
categories: ['3d-vision-and-scene-understanding', 'time-series-modeling-and-forecasting-methods']
tags: ['event-camera', 'motion-deblurring', 'implicit-neural-representation']
venue: "ICML 2024"
tldr: "A scale-aware spatio-temporal implicit representation method for event-based motion deblurring at unknown spatial and temporal scales."
---

# Learning Scale-Aware Spatio-temporal Implicit Representation for Event-based Motion Deblurring

**Source**: [https://proceedings.mlr.press/v235/yu24g.html](https://proceedings.mlr.press/v235/yu24g.html)

**TLDR**: A scale-aware spatio-temporal implicit representation method for event-based motion deblurring at unknown spatial and temporal scales.

## Abstract

Existing event-based motion deblurring methods mostly focus on restoring images with the same spatial and temporal scales as events. However, the unknown scales of images and events in the real world pose great challenges and have rarely been explored. To address this gap, we propose a novel Scale-Aware Spatio-temporal Network (SASNet) to flexibly restore blurred images with event streams at arbitrary scales. The core idea is to implicitly aggregate both spatial and temporal correspondence features of images and events to generalize at continuous scales. To restore highly blurred local areas, we develop a Spatial Implicit Representation Module (SIRM) to aggregate spatial correlation at any resolution through event encoding sampling. To tackle global motion blur, a Temporal Implicit Representation Module (TIRM) is presented to learn temporal correlation via temporal shift operations with long-term aggregation. Additionally, we build a High-resolution Hybrid Deblur (H2D) dataset using a new-generation hybrid event-based sensor, which comprises images with naturally spatially aligned and temporally synchronized events at various scales. Experiments demonstrate that our SASNet outperforms state-of-the-art methods on both synthetic GoPro and real H2D datasets, especially in high-speed motion scenarios. Code and dataset are available at https://github.com/aipixel/SASNet.