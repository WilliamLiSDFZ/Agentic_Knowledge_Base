---
title: "Magnet: We Never Know How Text-to-Image Diffusion Models Work, Until We Learn How Vision-Language Models Function"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/688ffe062732aabd87dfe57bcb0bf3ae-Abstract-Conference.html"
categories: ['diffusion-based-generative-modeling-and-inference', 'visual-language-multimodal-generation-reasoning']
tags: ['text-to-image', 'diffusion-models', 'vision-language-models', 'attribute-binding', 'stable-diffusion']
venue: "NeurIPS 2024"
tldr: "Magnet improves text-to-image diffusion model faithfulness on complex prompts by analyzing and leveraging how vision-language models process attributes."
---

# Magnet: We Never Know How Text-to-Image Diffusion Models Work, Until We Learn How Vision-Language Models Function

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/688ffe062732aabd87dfe57bcb0bf3ae-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/688ffe062732aabd87dfe57bcb0bf3ae-Abstract-Conference.html)

**TLDR**: Magnet improves text-to-image diffusion model faithfulness on complex prompts by analyzing and leveraging how vision-language models process attributes.

## Abstract

Text-to-image diffusion models particularly Stable Diffusion, have revolutionized the field of computer vision. However, the synthesis quality often deteriorates when asked to generate images that faithfully represent complex prompts involving multiple attributes and objects. While previous studies suggest that blended text embeddings lead to improper attribute binding, few have explored this in depth. In this work, we critically examine the limitations of the CLIP text encoder in understanding attributes and investigate how this affects diffusion models. We discern a phenomenon of attribute bias in the text space and highlight a contextual issue in padding embeddings that entangle different concepts. We propose Magnet, a novel training-free approach to tackle the attribute binding problem. We introduce positive and negative binding vectors to enhance disentanglement, further with a neighbor strategy to increase accuracy. Extensive experiments show that Magnet significantly improves synthesis quality and binding accuracy with negligible computational cost, enabling the generation of unconventional and unnatural concepts.