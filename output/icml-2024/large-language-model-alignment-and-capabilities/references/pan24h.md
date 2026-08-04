---
title: "Auto-Encoding Morph-Tokens for Multimodal LLM"
source: "https://proceedings.mlr.press/v235/pan24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pan24h/pan24h.pdf"
categories: ['generative-models-and-variational-inference', 'large-language-model-alignment-and-capabilities']
tags: ['multimodal-LLM', 'visual-generation', 'visual-comprehension', 'autoencoding']
venue: "ICML 2024"
tldr: "Proposes Auto-Encoding Morph-Tokens to reconcile the conflicting objectives of visual comprehension and generation in multimodal large language models."
---

# Auto-Encoding Morph-Tokens for Multimodal LLM

**Source**: [https://proceedings.mlr.press/v235/pan24h.html](https://proceedings.mlr.press/v235/pan24h.html)

**TLDR**: Proposes Auto-Encoding Morph-Tokens to reconcile the conflicting objectives of visual comprehension and generation in multimodal large language models.

## Abstract

For multimodal LLMs, the synergy of visual comprehension (textual output) and generation (visual output) presents an ongoing challenge. This is due to a conflicting objective: for comprehension, an MLLM needs to abstract the visuals; for generation, it needs to preserve the visuals as much as possible. Thus, the objective is a dilemma for visual-tokens. To resolve the conflict, we propose encoding images into morph-tokens to serve a dual purpose: for comprehension, they act as visual prompts instructing MLLM to generate texts; for generation, they take on a different, non-conflicting role as complete visual-tokens for image reconstruction, where the missing visual cues are recovered by the MLLM. Extensive experiments show that morph-tokens can achieve a new SOTA for multimodal comprehension and generation simultaneously. Our project is available at https://github.com/DCDmllm/MorphTokens.