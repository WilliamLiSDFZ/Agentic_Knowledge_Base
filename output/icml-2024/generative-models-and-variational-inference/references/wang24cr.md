---
title: "Boximator: Generating Rich and Controllable Motions for Video Synthesis"
source: "https://proceedings.mlr.press/v235/wang24cr.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24cr/wang24cr.pdf"
categories: ['generative-models-and-variational-inference']
tags: ['video-synthesis', 'motion-control', 'bounding-box-constraints']
venue: "ICML 2024"
tldr: "Boximator introduces hard and soft box constraints to enable fine-grained, controllable motion generation in video synthesis."
---

# Boximator: Generating Rich and Controllable Motions for Video Synthesis

**Source**: [https://proceedings.mlr.press/v235/wang24cr.html](https://proceedings.mlr.press/v235/wang24cr.html)

**TLDR**: Boximator introduces hard and soft box constraints to enable fine-grained, controllable motion generation in video synthesis.

## Abstract

Generating rich and controllable motion is a pivotal challenge in video synthesis. We propose Boximator, a new approach for fine-grained motion control. Boximator introduces two constraint types: hard box and soft box. Users select objects in the conditional frame using hard boxes and then use either type of boxes to roughly or rigorously define the object’s position, shape, or motion path in future frames. Boximator functions as a plug-in for existing video diffusion models. Its training process preserves the base model’s knowledge by freezing the original weights and training only the control module. To address training challenges, we introduce a novel self-tracking technique that greatly simplifies the learning of box-object correlations. Empirically, Boximator achieves state-of-the-art video quality (FVD) scores, improving on two base models, and further enhanced after incorporating box constraints. Its robust motion controllability is validated by drastic increases in the bounding box alignment metric. Human evaluation also shows that users favor Boximator generation results over the base model.