---
title: "From Vision to Audio and Beyond: A Unified Model for Audio-Visual Representation and Generation"
source: "https://proceedings.mlr.press/v235/su24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/su24b/su24b.pdf"
categories: ['audio-and-music-generation-diffusion-models', 'generative-models-and-variational-inference']
tags: ['audio-visual', 'multimodal', 'representation-learning', 'generation', 'video']
venue: "ICML 2024"
tldr: "A unified model is proposed for joint audio-visual representation and generation, leveraging the complementary nature of audio and visual modalities in video."
---

# From Vision to Audio and Beyond: A Unified Model for Audio-Visual Representation and Generation

**Source**: [https://proceedings.mlr.press/v235/su24b.html](https://proceedings.mlr.press/v235/su24b.html)

**TLDR**: A unified model is proposed for joint audio-visual representation and generation, leveraging the complementary nature of audio and visual modalities in video.

## Abstract

Video encompasses both visual and auditory data, creating a perceptually rich experience where these two modalities complement each other. As such, videos are a valuable type of media for the investigation of the interplay between audio and visual elements. Previous studies of audio-visual modalities primarily focused on either audio-visual representation learning or generative modeling of a modality conditioned on the other, creating a disconnect between these two branches. A unified framework that learns representation and generates modalities has not been developed yet. In this work, we introduce a novel framework called Vision to Audio and Beyond (VAB) to bridge the gap between audio-visual representation learning and vision-to-audio generation. The key approach of VAB is that rather than working with raw video frames and audio data, VAB performs representation learning and generative modeling within latent spaces. In particular, VAB uses a pre-trained audio tokenizer and an image encoder to obtain audio tokens and visual features, respectively. It then performs the pre-training task of visual-conditioned masked audio token prediction. This training strategy enables the model to engage in contextual learning and simultaneous video-to-audio generation. After the pre-training phase, VAB employs the iterative-decoding approach to rapidly generate audio tokens conditioned on visual features. Since VAB is a unified model, its backbone can be fine-tuned for various audio-visual downstream tasks. Our experiments showcase the efficiency of VAB in producing high-quality audio from video, and its capability to acquire semantic audio-visual features, leading to competitive results in audio-visual retrieval and classification.