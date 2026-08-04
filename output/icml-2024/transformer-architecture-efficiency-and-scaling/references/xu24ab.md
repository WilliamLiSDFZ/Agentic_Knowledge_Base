---
title: "Libra: Building Decoupled Vision System on Large Language Models"
source: "https://proceedings.mlr.press/v235/xu24ab.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24ab/xu24ab.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'transformer-architecture-efficiency-and-scaling']
tags: ['vision-language-model', 'decoupled-vision', 'cross-modal-interaction']
venue: "ICML 2024"
tldr: "Introduces Libra, a multimodal LLM with a decoupled vision system that separates intra-modal modeling from cross-modal interaction."
---

# Libra: Building Decoupled Vision System on Large Language Models

**Source**: [https://proceedings.mlr.press/v235/xu24ab.html](https://proceedings.mlr.press/v235/xu24ab.html)

**TLDR**: Introduces Libra, a multimodal LLM with a decoupled vision system that separates intra-modal modeling from cross-modal interaction.

## Abstract

In this work, we introduce Libra, a prototype model with a decoupled vision system on a large language model (LLM). The decoupled vision system decouples inner-modal modeling and cross-modal interaction, yielding unique visual information modeling and effective cross-modal comprehension. Libra is trained through discrete auto-regressive modeling on both vision and language inputs. Specifically, we incorporate a routed visual expert with a cross-modal bridge module into a pretrained LLM to route the vision and language flows during attention computing to enable different attention patterns in inner-modal modeling and cross-modal interaction scenarios. Experimental results demonstrate that the dedicated design of Libra achieves a strong MLLM baseline that rivals existing works in the image-to-text scenario with merely 50 million training data, providing a new perspective for future multimodal foundation models. Code is available at https://github.com/YifanXu74/Libra.