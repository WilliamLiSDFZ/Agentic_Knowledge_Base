---
title: "Modeling Caption Diversity in Contrastive Vision-Language Pretraining"
source: "https://proceedings.mlr.press/v235/lavoie24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lavoie24a/lavoie24a.pdf"
categories: ['generative-models-and-variational-inference', 'transformer-architecture-efficiency-and-scaling']
tags: ['contrastive-learning', 'CLIP', 'caption-diversity', 'vision-language']
venue: "ICML 2024"
tldr: "Llip extends CLIP by modeling caption diversity through latent variables, better capturing multiple valid descriptions for a single image."
---

# Modeling Caption Diversity in Contrastive Vision-Language Pretraining

**Source**: [https://proceedings.mlr.press/v235/lavoie24a.html](https://proceedings.mlr.press/v235/lavoie24a.html)

**TLDR**: Llip extends CLIP by modeling caption diversity through latent variables, better capturing multiple valid descriptions for a single image.

## Abstract

There are a thousand ways to caption an image. Contrastive Language Pretraining (CLIP) on the other hand, works by mapping an image and its caption to a single vector – limiting how well CLIP-like models can represent the diverse ways to describe an image. In this work, we introduce Llip, Latent Language Image Pretraining, which models the diversity of captions that could match an image. Llip’s vision encoder outputs a set of visual features that are mixed into a final representation by conditioning on information derived from the text. We show that Llip outperforms non-contextualized baselines like CLIP and SigLIP on a variety of tasks even with large-scale encoders. Llip improves zero-shot classification by an average of 2.9% zero-shot classification benchmarks with a ViT-G/14 encoder. Specifically, Llip attains a zero-shot top-1 accuracy of 83.5% on ImageNet outperforming a similarly sized CLIP by 1.4%. We also demonstrate improvement on zero-shot retrieval on MS-COCO by 6.0%. We provide a comprehensive analysis of the components introduced by the method and demonstrate that Llip leads to richer visual representations.