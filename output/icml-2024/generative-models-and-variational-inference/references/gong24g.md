---
title: "E$^2$GAN: Efficient Training of Efficient GANs for Image-to-Image Translation"
source: "https://proceedings.mlr.press/v235/gong24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gong24g/gong24g.pdf"
categories: ['generative-models-and-variational-inference', 'knowledge-distillation-methods-and-applications']
tags: ['image-to-image-translation', 'GAN-distillation', 'efficient-training']
venue: "ICML 2024"
tldr: "E²GAN proposes an efficient method for training lightweight GANs for real-time image editing by distilling from large text-to-image diffusion models."
---

# E$^2$GAN: Efficient Training of Efficient GANs for Image-to-Image Translation

**Source**: [https://proceedings.mlr.press/v235/gong24g.html](https://proceedings.mlr.press/v235/gong24g.html)

**TLDR**: E²GAN proposes an efficient method for training lightweight GANs for real-time image editing by distilling from large text-to-image diffusion models.

## Abstract

One highly promising direction for enabling flexible real-time on-device image editing is utilizing data distillation by leveraging large-scale text-to-image diffusion models to generate paired datasets used for training generative adversarial networks (GANs). This approach notably alleviates the stringent requirements typically imposed by high-end commercial GPUs for performing image editing with diffusion models. However, unlike text-to-image diffusion models, each distilled GAN is specialized for a specific image editing task, necessitating costly training efforts to obtain models for various concepts. In this work, we introduce and address a novel research direction: can the process of distilling GANs from diffusion models be made significantly more efficient? To achieve this goal, we propose a series of innovative techniques. First, we construct a base GAN model with generalized features, adaptable to different concepts through fine-tuning, eliminating the need for training from scratch. Second, we identify crucial layers within the base GAN model and employ Low-Rank Adaptation (LoRA) with a simple yet effective rank search process, rather than fine-tuning the entire base model. Third, we investigate the minimal amount of data necessary for fine-tuning, further reducing the overall training time. Extensive experiments show that we can efficiently empower GANs with the ability to perform real-time high-quality image editing on mobile devices with remarkably reduced training and storage costs for each concept.