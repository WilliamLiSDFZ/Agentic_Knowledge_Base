---
title: "VinT-6D: A Large-Scale Object-in-hand Dataset from Vision, Touch and Proprioception"
source: "https://proceedings.mlr.press/v235/wan24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wan24d/wan24d.pdf"
categories: ['simulation-scaling-limits-for-robot-manipulation', '3d-vision-and-scene-understanding']
tags: ['object-pose-estimation', 'multimodal-dataset', 'robotic-manipulation', 'tactile-sensing', 'proprioception']
venue: "ICML 2024"
tldr: "VinT-6D introduces a large-scale multi-modal dataset combining vision, touch, and proprioception for object-in-hand 6D pose estimation in robotic manipulation."
---

# VinT-6D: A Large-Scale Object-in-hand Dataset from Vision, Touch and Proprioception

**Source**: [https://proceedings.mlr.press/v235/wan24d.html](https://proceedings.mlr.press/v235/wan24d.html)

**TLDR**: VinT-6D introduces a large-scale multi-modal dataset combining vision, touch, and proprioception for object-in-hand 6D pose estimation in robotic manipulation.

## Abstract

This paper addresses the scarcity of large-scale datasets for accurate object-in-hand pose estimation, which is crucial for robotic in-hand manipulation within the "Perception-Planning-Control" paradigm. Specifically, we introduce VinT-6D, the first extensive multi-modal dataset integrating vision, touch, and proprioception, to enhance robotic manipulation. VinT-6D comprises 2 million VinT-Sim and 0.1 million VinT-Real entries, collected via simulations in Mujoco and Blender and a custom-designed real-world platform. This dataset is tailored for robotic hands, offering models with whole-hand tactile perception and high-quality, well-aligned data. To the best of our knowledge, the VinT-Real is the largest considering the collection difficulties in the real-world environment so it can bridge the gap of simulation to real compared to the previous works. Built upon VinT-6D, we present a benchmark method that shows significant improvements in performance by fusing multi-modal information. The project is available at https://VinT-6D.github.io/.