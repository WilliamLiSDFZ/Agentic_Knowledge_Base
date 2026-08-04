---
title: "Memory Consolidation Enables Long-Context Video Understanding"
source: "https://proceedings.mlr.press/v235/balazevic24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/balazevic24a/balazevic24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'time-series-modeling-and-forecasting-methods']
tags: ['video-understanding', 'memory-consolidation', 'long-context-transformers']
venue: "ICML 2024"
tldr: "A memory consolidation mechanism repurposes pretrained transformers to handle long temporal contexts in video understanding efficiently."
---

# Memory Consolidation Enables Long-Context Video Understanding

**Source**: [https://proceedings.mlr.press/v235/balazevic24a.html](https://proceedings.mlr.press/v235/balazevic24a.html)

**TLDR**: A memory consolidation mechanism repurposes pretrained transformers to handle long temporal contexts in video understanding efficiently.

## Abstract

Most transformer-based video encoders are limited to short temporal contexts due to their quadratic complexity. While various attempts have been made to extend this context, this has often come at the cost of both conceptual and computational complexity. We propose to instead re-purpose existing pre-trained video transformers by simply fine-tuning them to attend to memories derived non-parametrically from past activations. By leveraging redundancy reduction, our memory-consolidated vision transformer (MC-ViT) effortlessly extends its context far into the past and exhibits excellent scaling behavior when learning from longer videos. In doing so, MC-ViT sets a new state-of-the-art in long-context video understanding on EgoSchema, Perception Test, and Diving48, outperforming methods that benefit from orders of magnitude more parameters.