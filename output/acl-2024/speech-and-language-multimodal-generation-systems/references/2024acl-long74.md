---
title: "EasyGen: Easing Multimodal Generation with BiDiffuser and LLMs"
source: "https://aclanthology.org/2024.acl-long.74/"
categories: ['multimodal-language-vision-learning-systems', 'speech-and-language-multimodal-generation-systems']
tags: ['multimodal-generation', 'diffusion-models', 'llm-integration']
venue: "ACL 2024"
tldr: "Introduces EasyGen, a model combining bidirectional diffusion and LLMs for efficient multimodal understanding and generation."
---

# EasyGen: Easing Multimodal Generation with BiDiffuser and LLMs

**Source**: [https://aclanthology.org/2024.acl-long.74/](https://aclanthology.org/2024.acl-long.74/)

**TLDR**: Introduces EasyGen, a model combining bidirectional diffusion and LLMs for efficient multimodal understanding and generation.

## Abstract

AbstractWe present EasyGen, an efficient model designed to enhance multimodal understanding and generation by harnessing the capabilities of diffusion models and large language models (LLMs). Unlike existing multimodal models that predominately depend on encoders like CLIP or ImageBind and need ample amounts of training data to bridge modalities, EasyGen leverages BiDiffuser, a bidirectional conditional diffusion model, to foster more efficient modality interactions. EasyGen achieves text generation by training a projection layer linking BiDiffuser and an LLM, and facilities image generation by training an adapter to align the LLM’s text space with the BiDiffuser’s image space. Comprehensive quantitative and qualitative experiments show that EasyGen excels in data-efficient training, high-quality image generation, and extendibility, effectively addressing the challenges in multimodal generation.