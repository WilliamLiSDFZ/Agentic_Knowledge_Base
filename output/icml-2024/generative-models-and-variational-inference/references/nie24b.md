---
title: "Compositional Text-to-Image Generation with Dense Blob Representations"
source: "https://proceedings.mlr.press/v235/nie24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nie24b/nie24b.pdf"
categories: ['generative-models-and-variational-inference', 'large-language-model-alignment-and-capabilities']
tags: ['text-to-image', 'compositional-generation', 'blob-representations']
venue: "ICML 2024"
tldr: "Introduces dense blob representations as visual primitives to enable more controllable and compositional text-to-image generation."
---

# Compositional Text-to-Image Generation with Dense Blob Representations

**Source**: [https://proceedings.mlr.press/v235/nie24b.html](https://proceedings.mlr.press/v235/nie24b.html)

**TLDR**: Introduces dense blob representations as visual primitives to enable more controllable and compositional text-to-image generation.

## Abstract

Existing text-to-image models struggle to follow complex text prompts, raising the need for extra grounding inputs for better controllability. In this work, we propose to decompose a scene into visual primitives - denoted as dense blob representations - that contain fine-grained details of the scene while being modular, human-interpretable, and easy-to-construct. Based on blob representations, we develop a blob-grounded text-to-image diffusion model, termed BlobGEN, for compositional generation. Particularly, we introduce a new masked cross-attention module to disentangle the fusion between blob representations and visual features. To leverage the compositionality of large language models (LLMs), we introduce a new in-context learning approach to generate blob representations from text prompts. Our extensive experiments show that BlobGEN achieves superior zero-shot generation quality and better layout-guided controllability on MS-COCO. When augmented by LLMs, our method exhibits superior numerical and spatial correctness on compositional image generation benchmarks.