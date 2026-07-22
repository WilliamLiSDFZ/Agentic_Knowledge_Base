---
title: "Enhanced Visual Instruction Tuning with Synthesized Image-Dialogue Data"
source: "https://aclanthology.org/2024.findings-acl.864/"
categories: ['multimodal-language-vision-learning-systems', 'llm-training-alignment-and-evaluation']
tags: ['multimodal-LLMs', 'visual-instruction-tuning', 'image-dialogue-data']
venue: "ACL 2024"
tldr: "Synthesized image-dialogue data enhances visual instruction tuning for multimodal large language models."
---

# Enhanced Visual Instruction Tuning with Synthesized Image-Dialogue Data

**Source**: [https://aclanthology.org/2024.findings-acl.864/](https://aclanthology.org/2024.findings-acl.864/)

**TLDR**: Synthesized image-dialogue data enhances visual instruction tuning for multimodal large language models.

## Abstract

AbstractThe remarkable multimodal capabilities demonstrated by OpenAI’s GPT-4 have sparked significant interest in the development of multimodal Large Language Models (LLMs). A primary research objective of such models is to align visual and textual modalities effectively while comprehending human instructions.Current methodologies often rely on annotations derived from benchmark datasets to construct image-dialogue datasets for training purposes, akin to instruction tuning in LLMs. However, these datasets often exhibit domain bias, potentially constraining the generative capabilities of the models. In an effort to mitigate these limitations, we propose a novel data collection methodology that synchronously synthesizes images and dialogues for visual instruction tuning. This approach harnesses the power of generative models, marrying the abilities of ChatGPT and text-to-image generative models to yield a diverse and controllable dataset with varied image content. This not only provides greater flexibility compared to existing methodologies but also significantly enhances several model capabilities. Our research includes comprehensive experiments conducted on various datasets using the open-source LLAVA model as a testbed for our proposed pipeline. Our results underscore marked enhancements across more than ten commonly assessed capabilities.