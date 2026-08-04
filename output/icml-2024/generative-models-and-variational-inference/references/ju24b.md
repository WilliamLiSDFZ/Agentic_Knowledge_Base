---
title: "NaturalSpeech 3: Zero-Shot Speech Synthesis with Factorized Codec and Diffusion Models"
source: "https://proceedings.mlr.press/v235/ju24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ju24b/ju24b.pdf"
categories: ['audio-and-music-generation-diffusion-models', 'generative-models-and-variational-inference']
tags: ['text-to-speech', 'diffusion-models', 'zero-shot', 'speech-synthesis', 'factorized-codec']
venue: "ICML 2024"
tldr: "NaturalSpeech 3 uses factorized codec and diffusion models for high-quality zero-shot text-to-speech synthesis."
---

# NaturalSpeech 3: Zero-Shot Speech Synthesis with Factorized Codec and Diffusion Models

**Source**: [https://proceedings.mlr.press/v235/ju24b.html](https://proceedings.mlr.press/v235/ju24b.html)

**TLDR**: NaturalSpeech 3 uses factorized codec and diffusion models for high-quality zero-shot text-to-speech synthesis.

## Abstract

While recent large-scale text-to-speech (TTS) models have achieved significant progress, they still fall shorts in speech quality, similarity, and prosody. Considering that speech intricately encompasses various attributes (e.g., content, prosody, timbre, and acoustic details) that pose significant challenges for generation, a natural idea is to factorize speech into individual subspaces representing different attributes and generate them individually. Motivated by it, we propose a TTS system with novel factorized diffusion models to generate natural speech in a zero-shot way. Specifically, 1) we design a neural codec with factorized vector quantization (FVQ) to disentangle speech waveform into subspaces of content, prosody, timbre, and acoustic details; 2) we propose a factorized diffusion model, which generates attributes in each subspace following its corresponding prompt. With this factorization design, our method can effectively and efficiently model the intricate speech with disentangled subspaces in a divide-and-conquer way. Experimental results show that our method outperforms the state-of-the-art TTS systems on quality, similarity, prosody, and intelligibility.