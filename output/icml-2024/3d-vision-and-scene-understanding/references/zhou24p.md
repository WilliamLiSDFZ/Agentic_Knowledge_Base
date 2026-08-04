---
title: "GALA3D: Towards Text-to-3D Complex Scene Generation via Layout-guided Generative Gaussian Splatting"
source: "https://proceedings.mlr.press/v235/zhou24p.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24p/zhou24p.pdf"
categories: ['3d-vision-and-scene-understanding', 'generative-models-and-variational-inference']
tags: ['text-to-3d', 'gaussian-splatting', 'layout-guided-generation']
venue: "ICML 2024"
tldr: "Presents GALA3D, a framework using LLM-generated layouts to guide compositional text-to-3D scene generation via layout-controlled generative Gaussian splatting."
---

# GALA3D: Towards Text-to-3D Complex Scene Generation via Layout-guided Generative Gaussian Splatting

**Source**: [https://proceedings.mlr.press/v235/zhou24p.html](https://proceedings.mlr.press/v235/zhou24p.html)

**TLDR**: Presents GALA3D, a framework using LLM-generated layouts to guide compositional text-to-3D scene generation via layout-controlled generative Gaussian splatting.

## Abstract

We present GALA3D, generative 3D GAussians with LAyout-guided control, for effective compositional text-to-3D generation. We first utilize large language models (LLMs) to generate the initial layout and introduce a layout-guided 3D Gaussian representation for 3D content generation with adaptive geometric constraints. We then propose an instance-scene compositional optimization mechanism with conditioned diffusion to collaboratively generate realistic 3D scenes with consistent geometry, texture, scale, and accurate interactions among multiple objects while simultaneously adjusting the coarse layout priors extracted from the LLMs to align with the generated scene. Experiments show that GALA3D is a user-friendly, end-to-end framework for state-of-the-art scene-level 3D content generation and controllable editing while ensuring the high fidelity of object-level entities within the scene. The source codes and models will be available at gala3d.github.io.