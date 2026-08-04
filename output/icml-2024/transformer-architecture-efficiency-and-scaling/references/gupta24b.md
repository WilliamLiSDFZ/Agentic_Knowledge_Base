---
title: "xT: Nested Tokenization for Larger Context in Large Images"
source: "https://proceedings.mlr.press/v235/gupta24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gupta24b/gupta24b.pdf"
categories: ['3d-vision-and-scene-understanding', 'transformer-architecture-efficiency-and-scaling']
tags: ['large-image-processing', 'nested-tokenization', 'context-length', 'vision-transformers', 'hierarchical']
venue: "ICML 2024"
tldr: "A nested tokenization framework enabling vision transformers to handle large images with full global context."
---

# xT: Nested Tokenization for Larger Context in Large Images

**Source**: [https://proceedings.mlr.press/v235/gupta24b.html](https://proceedings.mlr.press/v235/gupta24b.html)

**TLDR**: A nested tokenization framework enabling vision transformers to handle large images with full global context.

## Abstract

Modern computer vision pipelines handle large images in one of two sub-optimal ways: down-sampling or cropping. These two methods incur significant losses in the amount of information and context present in an image. There are many downstream applications in which global context matters as much as high frequency details, such as in real-world satellite imagery; in such cases researchers have to make the uncomfortable choice of which information to discard. We introduce xT, a simple framework for vision transformers which effectively aggregates global context with local details and can model large images end-to-end on contemporary GPUs. We select a set of benchmark datasets across classic vision tasks which accurately reflect a vision model’s ability to understand truly large images and incorporate fine details over large scales and assess our method’s improvement on them. xT is a streaming, two-stage architecture that adapts existing vision backbones and long sequence language models to effectively model large images without quadratic memory growth. We are able to increase accuracy by up to 8.6% on challenging classification tasks and F1 score by 11.6 on context-dependent segmentation on images as large as 29,000 x 29,000 pixels.