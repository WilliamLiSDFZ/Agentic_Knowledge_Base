---
title: "Prototypical Transformer As Unified Motion Learners"
source: "https://proceedings.mlr.press/v235/han24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/han24d/han24d.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', '3d-vision-and-scene-understanding']
tags: ['transformer', 'optical-flow', 'motion-estimation']
venue: "ICML 2024"
tldr: "ProtoFormer is a unified prototype-based Transformer framework that addresses diverse motion tasks by integrating prototype learning with motion dynamics."
---

# Prototypical Transformer As Unified Motion Learners

**Source**: [https://proceedings.mlr.press/v235/han24d.html](https://proceedings.mlr.press/v235/han24d.html)

**TLDR**: ProtoFormer is a unified prototype-based Transformer framework that addresses diverse motion tasks by integrating prototype learning with motion dynamics.

## Abstract

In this work, we introduce the Prototypical Transformer (ProtoFormer), a general and unified framework that approaches various motion tasks from a prototype perspective. ProtoFormer seamlessly integrates prototype learning with Transformer by thoughtfully considering motion dynamics, introducing two innovative designs. First, Cross-Attention Prototyping discovers prototypes based on signature motion patterns, providing transparency in understanding motion scenes. Second, Latent Synchronization guides feature representation learning via prototypes, effectively mitigating the problem of motion uncertainty. Empirical results demonstrate that our approach achieves competitive performance on popular motion tasks such as optical flow and scene depth. Furthermore, it exhibits generality across various downstream tasks, including object tracking and video stabilization.