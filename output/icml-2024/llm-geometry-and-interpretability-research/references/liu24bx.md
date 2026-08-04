---
title: "In-context Vectors: Making In Context Learning More Effective and Controllable Through Latent Space Steering"
source: "https://proceedings.mlr.press/v235/liu24bx.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bx/liu24bx.pdf"
categories: ['llm-geometry-and-interpretability-research', 'large-language-model-alignment-and-capabilities']
tags: ['in-context-learning', 'latent-space', 'steering-vectors', 'large-language-models', 'controllability']
venue: "ICML 2024"
tldr: "In-context vectors are derived from demonstration examples to steer LLM latent representations, making in-context learning more effective and controllable than standard prompting."
---

# In-context Vectors: Making In Context Learning More Effective and Controllable Through Latent Space Steering

**Source**: [https://proceedings.mlr.press/v235/liu24bx.html](https://proceedings.mlr.press/v235/liu24bx.html)

**TLDR**: In-context vectors are derived from demonstration examples to steer LLM latent representations, making in-context learning more effective and controllable than standard prompting.

## Abstract

Large language models (LLMs) demonstrate emergent in-context learning capabilities, where they adapt to new tasks based on example demonstrations. However, in-context learning has seen limited effectiveness in many settings, is difficult to quantitatively control and takes up context window space. To overcome these limitations, we propose an alternative approach that recasts in-context learning as in-context vectors (ICV). Using ICV has two steps. We first use a forward pass on demonstration examples to create the in-context vector from the latent embedding of the LLM. This vector captures essential information about the intended task. On a new query, instead of adding demonstrations to the prompt, we shift the latent states of the LLM using the ICV. The ICV approach has several benefits: 1) it enables the LLM to more effectively follow the demonstration examples; 2) it’s easy to control by adjusting the magnitude of the ICV; 3) it reduces the length of the prompt by removing the in-context demonstrations; 4) ICV is computationally much more efficient than fine-tuning. We demonstrate that ICV achieves better performance compared to standard in-context learning and fine-tuning on diverse tasks including safety, style transfer, role-playing and formatting. Moreover, we show that we can flexibly teach LLM to simultaneously follow different types of instructions by simple vector arithmetics on the corresponding ICVs.