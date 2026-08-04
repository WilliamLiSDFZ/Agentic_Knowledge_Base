---
title: "HumanTOMATO: Text-aligned Whole-body Motion Generation"
source: "https://proceedings.mlr.press/v235/lu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lu24b/lu24b.pdf"
categories: ['audio-and-music-generation-diffusion-models', 'large-language-model-alignment-and-capabilities']
tags: ['motion-generation', 'text-driven', 'whole-body', 'facial-expressions', 'hand-gestures']
venue: "ICML 2024"
tldr: "Proposes a text-aligned framework for generating coherent whole-body motion including facial expressions, hand gestures, and body movement."
---

# HumanTOMATO: Text-aligned Whole-body Motion Generation

**Source**: [https://proceedings.mlr.press/v235/lu24b.html](https://proceedings.mlr.press/v235/lu24b.html)

**TLDR**: Proposes a text-aligned framework for generating coherent whole-body motion including facial expressions, hand gestures, and body movement.

## Abstract

This work targets a novel text-driven whole-body motion generation task, which takes a given textual description as input and aims at generating high-quality, diverse, and coherent facial expressions, hand gestures, and body motions simultaneously. Previous works on text-driven motion generation tasks mainly have two limitations: they ignore the key role of fine-grained hand and face controlling in vivid whole-body motion generation, and lack a good alignment between text and motion. To address such limitations, we propose a Text-aligned whOle-body Motion generATiOn framework, named HumanTOMATO, which is the first attempt to our knowledge towards applicable holistic motion generation in this research area. To tackle this challenging task, our solution includes two key designs: (1) a Holistic Hierarchical VQ-VAE (aka H${}^{2}$VQ) and a Hierarchical-GPT for fine-grained body and hand motion reconstruction and generation with two structured codebooks; and (2) a pre-trained text-motion-alignment model to help generated motion align with the input textual description explicitly. Comprehensive experiments verify that our model has significant advantages in both the quality of generated motions and their alignment with text.