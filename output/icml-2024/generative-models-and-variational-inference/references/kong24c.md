---
title: "ELF: Encoding Speaker-Specific Latent Speech Feature for Speech Synthesis"
source: "https://proceedings.mlr.press/v235/kong24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kong24c/kong24c.pdf"
categories: ['audio-and-music-generation-diffusion-models', 'generative-models-and-variational-inference']
tags: ['speech-synthesis', 'speaker-modeling', 'latent-features', 'multi-speaker', 'TTS']
venue: "ICML 2024"
tldr: "A novel method encoding speaker-specific latent speech features to synthesize diverse speaker characteristics without target-speaker fine-tuning."
---

# ELF: Encoding Speaker-Specific Latent Speech Feature for Speech Synthesis

**Source**: [https://proceedings.mlr.press/v235/kong24c.html](https://proceedings.mlr.press/v235/kong24c.html)

**TLDR**: A novel method encoding speaker-specific latent speech features to synthesize diverse speaker characteristics without target-speaker fine-tuning.

## Abstract

In this work, we propose a novel method for modeling numerous speakers, which enables expressing the overall characteristics of speakers in detail like a trained multi-speaker model without additional training on the target speaker’s dataset. Although various works with similar purposes have been actively studied, their performance has not yet reached that of trained multi-speaker models due to their fundamental limitations. To overcome previous limitations, we propose effective methods for feature learning and representing target speakers’ speech characteristics by discretizing the features and conditioning them to a speech synthesis model. Our method obtained a significantly higher similarity mean opinion score (SMOS) in subjective similarity evaluation than seen speakers of a high-performance multi-speaker model, even with unseen speakers. The proposed method also outperforms a zero-shot method by significant margins. Furthermore, our method shows remarkable performance in generating new artificial speakers. In addition, we demonstrate that the encoded latent features are sufficiently informative to reconstruct an original speaker’s speech completely. It implies that our method can be used as a general methodology to encode and reconstruct speakers’ characteristics in various tasks.