---
title: "Parallelized Spatiotemporal Slot Binding for Videos"
source: "https://proceedings.mlr.press/v235/singh24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/singh24g/singh24g.pdf"
categories: ['3d-vision-and-scene-understanding', 'transformer-architecture-efficiency-and-scaling']
tags: ['object-centric-learning', 'slot-attention', 'video-understanding']
venue: "ICML 2024"
tldr: "Proposes a parallelized spatiotemporal slot binding model for videos that replaces RNN-based architectures with scalable long-range interaction mechanisms."
---

# Parallelized Spatiotemporal Slot Binding for Videos

**Source**: [https://proceedings.mlr.press/v235/singh24g.html](https://proceedings.mlr.press/v235/singh24g.html)

**TLDR**: Proposes a parallelized spatiotemporal slot binding model for videos that replaces RNN-based architectures with scalable long-range interaction mechanisms.

## Abstract

While modern best practices advocate for scalable architectures that support long-range interactions, object-centric models are yet to fully embrace these architectures. In particular, existing object-centric models for handling sequential inputs, due to their reliance on RNN-based implementation, show poor stability and capacity and are slow to train on long sequences. We introduce Parallelizable Spatiotemporal Binder or PSB, the first temporally-parallelizable slot learning architecture for sequential inputs. Unlike conventional RNN-based approaches, PSB produces object-centric representations, known as slots, for all time-steps in parallel. This is achieved by refining the initial slots across all time-steps through a fixed number of layers equipped with causal attention. By capitalizing on the parallelism induced by our architecture, the proposed model exhibits a significant boost in efficiency. In experiments, we test PSB extensively as an encoder within an auto-encoding framework paired with a wide variety of decoder options. Compared to the state-of-the-art, our architecture demonstrates stable training on longer sequences, achieves parallelization that results in a 60% increase in training speed, and yields performance that is on par with or better on unsupervised 2D and 3D object-centric scene decomposition and understanding.