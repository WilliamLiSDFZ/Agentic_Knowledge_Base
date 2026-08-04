---
title: "Denoising Autoregressive Representation Learning"
source: "https://proceedings.mlr.press/v235/li24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24d/li24d.pdf"
categories: ['generative-models-and-variational-inference', 'transformer-architecture-efficiency-and-scaling']
tags: ['visual-representation', 'autoregressive', 'denoising', 'transformer', 'self-supervised-learning']
venue: "ICML 2024"
tldr: "Proposes DARL, a decoder-only transformer that learns visual representations via denoising autoregressive prediction of image patches."
---

# Denoising Autoregressive Representation Learning

**Source**: [https://proceedings.mlr.press/v235/li24d.html](https://proceedings.mlr.press/v235/li24d.html)

**TLDR**: Proposes DARL, a decoder-only transformer that learns visual representations via denoising autoregressive prediction of image patches.

## Abstract

In this paper, we explore a new generative approach for learning visual representations. Our method, DARL, employs a decoder-only Transformer to predict image patches autoregressively. We find that training with Mean Squared Error (MSE) alone leads to strong representations. To enhance the image generation ability, we replace the MSE loss with the diffusion objective by using a denoising patch decoder. We show that the learned representation can be improved by using tailored noise schedules and longer training in larger models. Notably, the optimal schedule differs significantly from the typical ones used in standard image diffusion models. Overall, despite its simple architecture, DARL delivers performance remarkably close to state-of-the-art masked prediction models under the fine-tuning protocol. This marks an important step towards a unified model capable of both visual perception and generation, effectively combining the strengths of autoregressive and denoising diffusion models.