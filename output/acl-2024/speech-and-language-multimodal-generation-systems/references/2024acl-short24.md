---
title: "On the Semantic Latent Space of Diffusion-Based Text-To-Speech Models"
source: "https://aclanthology.org/2024.acl-short.24/"
pdf_url: ""
categories: ['speech-and-language-multimodal-generation-systems', 'language-model-representations-and-embedding-spaces']
tags: ['diffusion-tts', 'semantic-latent-space', 'speech-synthesis']
venue: "ACL 2024"
tldr: "Investigates the semantic latent space of diffusion-based text-to-speech models and methods for controlling synthesis."
---

# On the Semantic Latent Space of Diffusion-Based Text-To-Speech Models

**Source**: [https://aclanthology.org/2024.acl-short.24/](https://aclanthology.org/2024.acl-short.24/)

**TLDR**: Investigates the semantic latent space of diffusion-based text-to-speech models and methods for controlling synthesis.

## Abstract

AbstractThe incorporation of Denoising Diffusion Models (DDMs) in the Text-to-Speech (TTS) domain is rising, providing great value in synthesizing high quality speech. Although they exhibit impressive audio quality, the extent of their semantic capabilities is unknown, and controlling their synthesized speech’s vocal properties remains a challenge. Inspired by recent advances in image synthesis, we explore the latent space of frozen TTS models, which is composed of the latent bottleneck activations of the DDM’s denoiser. We identify that this space contains rich semantic information, and outline several novel methods for finding semantic directions within it, both supervised and unsupervised. We then demonstrate how these enable off-the-shelf audio editing, without any further training, architectural changes or data requirements. We present evidence of the semantic and acoustic qualities of the edited audio, and provide supplemental samples: https://latent-analysis-grad-tts.github.io/speech-samples/.