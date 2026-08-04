---
title: "Mastering Text-to-Image Diffusion: Recaptioning, Planning, and Generating with Multimodal LLMs"
source: "https://proceedings.mlr.press/v235/yang24ai.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24ai/yang24ai.pdf"
categories: ['generative-models-and-variational-inference', 'large-language-model-alignment-and-capabilities']
tags: ['text-to-image', 'diffusion-models', 'multimodal-LLM']
venue: "ICML 2024"
tldr: "A training-free framework using multimodal LLMs for recaptioning, planning, and generating complex multi-object text-to-image diffusion outputs."
---

# Mastering Text-to-Image Diffusion: Recaptioning, Planning, and Generating with Multimodal LLMs

**Source**: [https://proceedings.mlr.press/v235/yang24ai.html](https://proceedings.mlr.press/v235/yang24ai.html)

**TLDR**: A training-free framework using multimodal LLMs for recaptioning, planning, and generating complex multi-object text-to-image diffusion outputs.

## Abstract

Diffusion models have exhibit exceptional performance in text-to-image generation and editing. However, existing methods often face challenges when handling complex text prompts that involve multiple objects with multiple attributes and relationships. In this paper, we propose a brand new training-free text-to-image generation/editing framework, namely Recaption, Plan and Generate (RPG), harnessing the powerful chain-of-thought reasoning ability of multimodal LLMs to enhance the compositionality of text-to-image diffusion models. Our approach employs the MLLM as a global planner to decompose the process of generating complex images into multiple simpler generation tasks within subregions. We propose complementary regional diffusion to enable region-wise compositional generation. Furthermore, we integrate text-guided image generation and editing within the proposed RPG in a closed-loop fashion, thereby enhancing generalization ability. Extensive experiments demonstrate our RPG outperforms state-of-the-art text-to-image models, including DALL-E 3 and SDXL, particularly in multi-category object composition and text-image semantic alignment. Notably, our RPG framework exhibits wide compatibility with various MLLM architectures and diffusion backbones. Our code is available at https://github.com/YangLing0818/RPG-DiffusionMaster