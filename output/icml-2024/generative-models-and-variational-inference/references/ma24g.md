---
title: "X-Oscar: A Progressive Framework for High-quality Text-guided 3D Animatable Avatar Generation"
source: "https://proceedings.mlr.press/v235/ma24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24g/ma24g.pdf"
categories: ['3d-vision-and-scene-understanding', 'generative-models-and-variational-inference']
tags: ['3D-avatar-generation', 'text-guided', 'animation', 'progressive-framework']
venue: "ICML 2024"
tldr: "X-Oscar is a progressive framework for generating high-quality text-guided 3D animatable avatars, addressing oversaturation and quality issues."
---

# X-Oscar: A Progressive Framework for High-quality Text-guided 3D Animatable Avatar Generation

**Source**: [https://proceedings.mlr.press/v235/ma24g.html](https://proceedings.mlr.press/v235/ma24g.html)

**TLDR**: X-Oscar is a progressive framework for generating high-quality text-guided 3D animatable avatars, addressing oversaturation and quality issues.

## Abstract

Recent advancements in automatic 3D avatar generation guided by text have made significant progress. However, existing methods have limitations such as oversaturation and low-quality output. To address these challenges, we propose X-Oscar, a progressive framework for generating high-quality animatable avatars from text prompts. It follows a sequential "Geometry→Texture→Animation" paradigm, simplifying optimization through step-by-step generation. To tackle oversaturation, we introduce Adaptive Variational Parameter (AVP), representing avatars as an adaptive distribution during training. Additionally, we present Avatar-aware Score Distillation Sampling (ASDS), a novel technique that incorporates avatar-aware noise into rendered images for improved generation quality during optimization. Extensive evaluations confirm the superiority of X-Oscar over existing text-to-3D and text-to-avatar approaches. Our anonymous project page: https://anonymous1440.github.io/.