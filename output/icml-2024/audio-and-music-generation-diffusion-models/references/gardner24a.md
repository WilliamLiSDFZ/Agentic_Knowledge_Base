---
title: "LLark: A Multimodal Instruction-Following Language Model for Music"
source: "https://proceedings.mlr.press/v235/gardner24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gardner24a/gardner24a.pdf"
categories: ['audio-and-music-generation-diffusion-models', 'large-language-model-alignment-and-capabilities']
tags: ['music-understanding', 'multimodal-model', 'instruction-tuning']
venue: "ICML 2024"
tldr: "Presents LLark, a multimodal instruction-tuned language model for music understanding built via curated music-caption data."
---

# LLark: A Multimodal Instruction-Following Language Model for Music

**Source**: [https://proceedings.mlr.press/v235/gardner24a.html](https://proceedings.mlr.press/v235/gardner24a.html)

**TLDR**: Presents LLark, a multimodal instruction-tuned language model for music understanding built via curated music-caption data.

## Abstract

Music has a unique and complex structure which is challenging for both expert humans and existing AI systems to understand, and presents unique challenges relative to other forms of audio. We present LLark, an instruction-tuned multimodal model for music understanding. We detail our process for dataset creation, which involves augmenting the annotations of diverse open-source music datasets and converting them to a unified instruction-tuning format. We propose a multimodal architecture for LLark, integrating a pretrained generative model for music with a pretrained language model. In evaluations on three types of tasks (music understanding, captioning, reasoning), we show that LLark matches or outperforms existing baselines in music understanding, and that humans show a high degree of agreement with its responses in captioning and reasoning tasks. LLark is trained entirely from open-source music data and models, and we make our training code available along with the release of this paper. Additional results and audio examples are at https://bit.ly/llark, and our source code is available at https://github.com/spotify-research/llark.