---
title: "Proactive Detection of Voice Cloning with Localized Watermarking"
source: "https://proceedings.mlr.press/v235/san-roman24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/san-roman24a/san-roman24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'audio-and-music-generation-diffusion-models']
tags: ['audio-watermarking', 'voice-cloning', 'speech-synthesis', 'localized-detection', 'generative-audio']
venue: "ICML 2024"
tldr: "AudioSeal is introduced as the first audio watermarking method specifically designed for localized detection of AI-generated speech against voice cloning."
---

# Proactive Detection of Voice Cloning with Localized Watermarking

**Source**: [https://proceedings.mlr.press/v235/san-roman24a.html](https://proceedings.mlr.press/v235/san-roman24a.html)

**TLDR**: AudioSeal is introduced as the first audio watermarking method specifically designed for localized detection of AI-generated speech against voice cloning.

## Abstract

In the rapidly evolving field of speech generative models, there is a pressing need to ensure audio authenticity against the risks of voice cloning. We present AudioSeal, the first audio watermarking technique designed specifically for localized detection of AI-generated speech. AudioSeal employs a generator / detector architecture trained jointly with a localization loss to enable localized watermark detection up to the sample level, and a novel perceptual loss inspired by auditory masking, that enables AudioSeal to achieve better imperceptibility. AudioSeal achieves state-of-the-art performance in terms of robustness to real life audio manipulations and imperceptibility based on automatic and human evaluation metrics. Additionally, AudioSeal is designed with a fast, single-pass detector, that significantly surpasses existing models in speed, achieving detection up to two orders of magnitude faster, making it ideal for large-scale and real-time applications.Code is available at https://github.com/facebookresearch/audioseal