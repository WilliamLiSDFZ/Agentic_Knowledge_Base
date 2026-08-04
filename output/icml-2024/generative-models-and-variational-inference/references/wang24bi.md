---
title: "Proteus: Exploring Protein Structure Generation for Enhanced Designability and Efficiency"
source: "https://proceedings.mlr.press/v235/wang24bi.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24bi/wang24bi.pdf"
categories: ['generative-models-for-molecular-protein-design', 'generative-models-and-variational-inference']
tags: ['protein-structure-generation', 'diffusion-models', 'designability', 'generative-models']
venue: "ICML 2024"
tldr: "Presents Proteus, a diffusion-based protein structure generation model achieving enhanced designability and efficiency without relying on large pretrained structure prediction networks."
---

# Proteus: Exploring Protein Structure Generation for Enhanced Designability and Efficiency

**Source**: [https://proceedings.mlr.press/v235/wang24bi.html](https://proceedings.mlr.press/v235/wang24bi.html)

**TLDR**: Presents Proteus, a diffusion-based protein structure generation model achieving enhanced designability and efficiency without relying on large pretrained structure prediction networks.

## Abstract

Diffusion-based generative models have been successfully employed to create proteins with novel structures and functions. However, the construction of such models typically depends on large, pre-trained structure prediction networks, like RFdiffusion. In contrast, alternative models that are trained from scratch, such as FrameDiff, still fall short in performance. In this context, we introduce Proteus, an innovative deep diffusion network that incorporates graph-based triangle methods and a multi-track interaction network, eliminating the dependency on structure prediction pre-training with superior efficiency. We have validated our model’s performance on de novo protein backbone generation through comprehensive in silico evaluations and experimental characterizations, which demonstrate a remarkable success rate. These promising results underscore Proteus’s ability to generate highly designable protein backbones efficiently. This capability, achieved without reliance on pre-training techniques, has the potential to significantly advance the field of protein design.