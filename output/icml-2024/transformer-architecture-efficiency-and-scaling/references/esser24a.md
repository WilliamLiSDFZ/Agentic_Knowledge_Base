---
title: "Scaling Rectified Flow Transformers for High-Resolution Image Synthesis"
source: "https://proceedings.mlr.press/v235/esser24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/esser24a/esser24a.pdf"
categories: ['generative-models-and-variational-inference', 'transformer-architecture-efficiency-and-scaling']
tags: ['diffusion-models', 'rectified-flow', 'transformers', 'high-resolution-image-synthesis', 'scaling']
venue: "ICML 2024"
tldr: "Scales rectified flow transformers for high-resolution image synthesis, achieving state-of-the-art generative quality with improved training efficiency."
---

# Scaling Rectified Flow Transformers for High-Resolution Image Synthesis

**Source**: [https://proceedings.mlr.press/v235/esser24a.html](https://proceedings.mlr.press/v235/esser24a.html)

**TLDR**: Scales rectified flow transformers for high-resolution image synthesis, achieving state-of-the-art generative quality with improved training efficiency.

## Abstract

Diffusion models create data from noise by inverting the forward paths of data towards noise and have emerged as a powerful generative modeling technique for high-dimensional, perceptual data such as images and videos. Rectified flow is a recent generative model formulation that connects data and noise in a straight line. Despite its better theoretical properties and conceptual simplicity, it is not yet decisively established as standard practice. In this work, we improve existing noise sampling techniques for training rectified flow models by biasing them towards perceptually relevant scales. Through a large-scale study, we demonstrate the superior performance of this approach compared to established diffusion formulations for high-resolution text-to-image synthesis. Additionally, we present a novel transformer-based architecture for text-to-image generation that uses separate weights for the two modalities and enables a bidirectional flow of information between image and text tokens, improving text comprehension, typography, and human preference ratings. We demonstrate that this architecture follows predictable scaling trends and correlates lower validation loss to improved text-to-image synthesis as measured by various metrics and human evaluations. Our largest models outperform state-of-the-art models. Stability AI is considering making experimental data, code, and model weights publicly available.