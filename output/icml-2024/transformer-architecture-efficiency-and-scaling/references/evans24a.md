---
title: "Fast Timing-Conditioned Latent Audio Diffusion"
source: "https://proceedings.mlr.press/v235/evans24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/evans24a/evans24a.pdf"
categories: ['audio-and-music-generation-diffusion-models', 'transformer-architecture-efficiency-and-scaling']
tags: ['audio-generation', 'latent-diffusion', 'text-to-audio', 'timing-conditioning', 'long-form-generation']
venue: "ICML 2024"
tldr: "Introduces a fast timing-conditioned latent diffusion model for efficient generation of long-form variable-length stereo audio from text prompts."
---

# Fast Timing-Conditioned Latent Audio Diffusion

**Source**: [https://proceedings.mlr.press/v235/evans24a.html](https://proceedings.mlr.press/v235/evans24a.html)

**TLDR**: Introduces a fast timing-conditioned latent diffusion model for efficient generation of long-form variable-length stereo audio from text prompts.

## Abstract

Generating long-form 44.1kHz stereo audio from text prompts can be computationally demanding. Further, most previous works do not tackle that music and sound effects naturally vary in their duration. Our research focuses on the efficient generation of long-form, variable-length stereo music and sounds at 44.1kHz using text prompts with a generative model. It is based on latent diffusion, with its latent defined by a fully-convolutional variational autoencoder. The generative model is conditioned on text prompts as well as timing embeddings, allowing for fine control over both the content and length of the generated music and sounds. It is capable of rendering stereo signals of up to 95 sec at 44.1kHz in 8 sec on an A100 GPU. Despite its compute efficiency and fast inference, the proposed model is one of the best in two public text-to-music and -audio benchmarks and, differently from state-of-the-art models, can generate music with structure and stereo sounds.