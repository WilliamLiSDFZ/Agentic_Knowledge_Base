---
title: "VideoPoet: A Large Language Model for Zero-Shot Video Generation"
source: "https://proceedings.mlr.press/v235/kondratyuk24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kondratyuk24a/kondratyuk24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'generative-models-and-variational-inference']
tags: ['video-generation', 'large-language-models', 'multimodal', 'zero-shot', 'transformer']
venue: "ICML 2024"
tldr: "VideoPoet is a decoder-only transformer LLM capable of zero-shot high-quality video generation from diverse multimodal conditioning signals."
---

# VideoPoet: A Large Language Model for Zero-Shot Video Generation

**Source**: [https://proceedings.mlr.press/v235/kondratyuk24a.html](https://proceedings.mlr.press/v235/kondratyuk24a.html)

**TLDR**: VideoPoet is a decoder-only transformer LLM capable of zero-shot high-quality video generation from diverse multimodal conditioning signals.

## Abstract

We present VideoPoet, a language model capable of synthesizing high-quality video from a large variety of conditioning signals. VideoPoet employs a decoder-only transformer architecture that processes multimodal inputs – including images, videos, text, and audio. The training protocol follows that of Large Language Models (LLMs), consisting of two stages: pretraining and task-specific adaptation. During pretraining, VideoPoet incorporates a mixture of multimodal generative objectives within an autoregressive Transformer framework. The pretrained LLM serves as a foundation that can be adapted for a range of video generation tasks. We present empirical results demonstrating the model’s state-of-the-art capabilities in zero-shot video generation, specifically highlighting the ability to generate high-fidelity motions. Project page: http://sites.research.google/videopoet/