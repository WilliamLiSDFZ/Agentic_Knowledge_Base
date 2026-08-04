---
title: "D-Flow: Differentiating through Flows for Controlled Generation"
source: "https://proceedings.mlr.press/v235/ben-hamu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ben-hamu24a/ben-hamu24a.pdf"
categories: ['generative-models-and-variational-inference', 'neural-operators-for-pde-solving']
tags: ['diffusion-models', 'flow-matching', 'controlled-generation', 'inverse-problems', 'differentiable-optimization']
venue: "ICML 2024"
tldr: "Introduces D-Flow, a framework for controlled generation in diffusion and flow-matching models by differentiating through the flow without retraining."
---

# D-Flow: Differentiating through Flows for Controlled Generation

**Source**: [https://proceedings.mlr.press/v235/ben-hamu24a.html](https://proceedings.mlr.press/v235/ben-hamu24a.html)

**TLDR**: Introduces D-Flow, a framework for controlled generation in diffusion and flow-matching models by differentiating through the flow without retraining.

## Abstract

Taming the generation outcome of state of the art Diffusion and Flow-Matching (FM) models without having to re-train a task-specific model unlocks a powerful tool for solving inverse problems, conditional generation, and controlled generation in general. In this work we introduce D-Flow, a simple framework for controlling the generation process by differentiating through the flow, optimizing for the source (noise) point. We motivate this framework by our key observation stating that for Diffusion/FM models trained with Gaussian probability paths, differentiating through the generation process projects gradient on the data manifold, implicitly injecting the prior into the optimization process. We validate our framework on linear and non-linear controlled generation problems including: image and audio inverse problems and conditional molecule generation reaching state of the art performance across all.