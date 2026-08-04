---
title: "Semantic-Aware Human Object Interaction Image Generation"
source: "https://proceedings.mlr.press/v235/xu24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24e/xu24e.pdf"
categories: ['generative-models-and-variational-inference']
tags: ['text-to-image', 'human-object-interaction', 'generative-models']
venue: "ICML 2024"
tldr: "A semantic-aware framework improves text-to-image generation fidelity for human-object interaction prompts by incorporating spatial and semantic constraints."
---

# Semantic-Aware Human Object Interaction Image Generation

**Source**: [https://proceedings.mlr.press/v235/xu24e.html](https://proceedings.mlr.press/v235/xu24e.html)

**TLDR**: A semantic-aware framework improves text-to-image generation fidelity for human-object interaction prompts by incorporating spatial and semantic constraints.

## Abstract

Recent text-to-image generative models have demonstrated remarkable abilities in generating realistic images. Despite their great success, these models struggle to generate high-fidelity images with prompts oriented toward human-object interaction (HOI). The difficulty in HOI generation arises from two aspects. Firstly, the complexity and diversity of human poses challenge plausible human generation. Furthermore, untrustworthy generation of interaction boundary regions may lead to deficiency in HOI semantics. To tackle the problems, we propose a Semantic-Aware HOI generation framework SA-HOI . It utilizes human pose quality and interaction boundary region information as guidance for denoising process, thereby encouraging refinement in these regions to produce more reasonable HOI images. Based on it, we establish an iterative inversion and image refinement pipeline to continually enhance generation quality. Further, we introduce a comprehensive benchmark for HOI generation, which comprises a dataset involving diverse and fine-grained HOI categories, along with multiple custom-tailored evaluation metrics for HOI generation. Experiments demonstrate that our method significantly improves generation quality under both HOI-specific and conventional image evaluation metrics. The code is available at https://github.com/XZPKU/SA-HOI.git