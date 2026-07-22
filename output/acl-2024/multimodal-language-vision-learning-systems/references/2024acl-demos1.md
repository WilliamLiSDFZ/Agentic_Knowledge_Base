---
title: "PAI-Diffusion: Constructing and Serving a Family of Open Chinese Diffusion Models for Text-to-image Synthesis on the Cloud"
source: "https://aclanthology.org/2024.acl-demos.1/"
pdf_url: ""
categories: ['multimodal-language-vision-learning-systems', 'text-input-and-generation-for-cjk-languages']
tags: ['text-to-image', 'diffusion-models', 'Chinese-language', 'cloud-serving', 'generation']
venue: "ACL 2024"
tldr: "PAI-Diffusion constructs and serves a family of open Chinese diffusion models for text-to-image synthesis on cloud infrastructure."
---

# PAI-Diffusion: Constructing and Serving a Family of Open Chinese Diffusion Models for Text-to-image Synthesis on the Cloud

**Source**: [https://aclanthology.org/2024.acl-demos.1/](https://aclanthology.org/2024.acl-demos.1/)

**TLDR**: PAI-Diffusion constructs and serves a family of open Chinese diffusion models for text-to-image synthesis on cloud infrastructure.

## Abstract

AbstractText-to-image synthesis for the Chinese language poses unique challenges due to its large vocabulary size, and intricate character relationships. While existing diffusion models have shown promise in generating images from textual descriptions, they often neglect domain-specific contexts and lack robustness in handling the Chinese language. This paper introduces PAI-Diffusion, a comprehensive framework that addresses these limitations. PAI-Diffusion incorporates both general and domain-specific Chinese diffusion models, enabling the generation of contextually relevant images. It explores the potential of using LoRA and ControlNet for fine-grained image style transfer and image editing, empowering users with enhanced control over image generation. Moreover, PAI-Diffusion seamlessly integrates with Alibaba Cloud’s Platform for AI, providing accessible and scalable solutions. All the Chinese diffusion model checkpoints, LoRAs, and ControlNets, including domain-specific ones, are publicly available. A user-friendly Chinese WebUI and the diffusers-api elastic inference toolkit, also open-sourced, further facilitate the easy deployment of PAI-Diffusion models in various local and cloud environments, making it a valuable resource for Chinese text-to-image synthesis.