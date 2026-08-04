---
title: "PIDformer: Transformer Meets Control Theory"
source: "https://proceedings.mlr.press/v235/nguyen24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nguyen24i/nguyen24i.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'bayesian-filtering-and-dynamical-systems-learning']
tags: ['transformer', 'control-theory', 'rank-collapse']
venue: "ICML 2024"
tldr: "Reformulates self-attention as a state-space model and incorporates PID control theory to address rank collapse and input corruption in transformers."
---

# PIDformer: Transformer Meets Control Theory

**Source**: [https://proceedings.mlr.press/v235/nguyen24i.html](https://proceedings.mlr.press/v235/nguyen24i.html)

**TLDR**: Reformulates self-attention as a state-space model and incorporates PID control theory to address rank collapse and input corruption in transformers.

## Abstract

In this work, we address two main shortcomings of transformer architectures: input corruption and rank collapse in their output representation. We unveil self-attention as an autonomous state-space model that inherently promotes smoothness in its solutions, leading to lower-rank outputs and diminished representation capacity. Moreover, the steady-state solution of the model is sensitive to input perturbations. We incorporate a Proportional-Integral-Derivative (PID) closed-loop feedback control system with a reference point into the model to improve robustness and representation capacity. This integration aims to preserve high-frequency details while bolstering model stability, rendering it more noise-resilient. The resulting controlled state-space model is theoretically proven robust and adept at addressing the rank collapse. Motivated by this control framework, we derive a novel class of transformers, PID-controlled Transformer (PIDformer), aimed at improving robustness and mitigating the rank-collapse issue inherent in softmax transformers. We empirically evaluate the model for advantages and robustness against baseline transformers across various practical tasks, including object classification, image segmentation, and language modeling.