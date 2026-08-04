---
title: "Prompt-guided Precise Audio Editing with Diffusion Models"
source: "https://proceedings.mlr.press/v235/xu24p.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24p/xu24p.pdf"
categories: ['audio-and-music-generation-diffusion-models']
tags: ['audio-editing', 'diffusion-models', 'text-guided']
venue: "ICML 2024"
tldr: "A prompt-guided audio editing framework leverages diffusion models for precise and flexible manipulation of target events within audio recordings."
---

# Prompt-guided Precise Audio Editing with Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/xu24p.html](https://proceedings.mlr.press/v235/xu24p.html)

**TLDR**: A prompt-guided audio editing framework leverages diffusion models for precise and flexible manipulation of target events within audio recordings.

## Abstract

Audio editing involves the arbitrary manipulation of audio content through precise control. Although text-guided diffusion models have made significant advancements in text-to-audio generation, they still face challenges in finding a flexible and precise way to modify target events within an audio track. We present a novel approach, referred to as PPAE, which serves as a general module for diffusion models and enables precise audio editing. The editing is based on the input textual prompt only and is entirely training-free. We exploit the cross-attention maps of diffusion models to facilitate accurate local editing and employ a hierarchical local-global pipeline to ensure a smoother editing process. Experimental results highlight the effectiveness of our method in various editing tasks.