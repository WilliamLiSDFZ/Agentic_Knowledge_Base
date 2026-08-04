---
title: "Video-LaVIT: Unified Video-Language Pre-training with Decoupled Visual-Motional Tokenization"
source: "https://proceedings.mlr.press/v235/jin24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jin24f/jin24f.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'generative-models-and-variational-inference']
tags: ['video-language-pretraining', 'multimodal-llm', 'visual-motional-tokenization', 'video-generation']
venue: "ICML 2024"
tldr: "Video-LaVIT unifies video and language pretraining by decoupling visual and motion tokenization for scalable multimodal large language models."
---

# Video-LaVIT: Unified Video-Language Pre-training with Decoupled Visual-Motional Tokenization

**Source**: [https://proceedings.mlr.press/v235/jin24f.html](https://proceedings.mlr.press/v235/jin24f.html)

**TLDR**: Video-LaVIT unifies video and language pretraining by decoupling visual and motion tokenization for scalable multimodal large language models.

## Abstract

In light of recent advances in multimodal Large Language Models (LLMs), there is increasing attention to scaling them from image-text data to more informative real-world videos. Compared to static images, video poses unique challenges for effective large-scale pre-training due to the modeling of its spatiotemporal dynamics. In this paper, we address such limitations in video-language pre-training with an efficient video decomposition that represents each video as keyframes and temporal motions. These are then adapted to an LLM using well-designed tokenizers that discretize visual and temporal information as a few tokens, thus enabling unified generative pre-training of videos, images, and text. At inference, the generated tokens from the LLM are carefully recovered to the original continuous pixel space to create various video content. Our proposed framework is both capable of comprehending and generating image and video content, as demonstrated by its competitive performance across 13 multimodal benchmarks in image and video understanding and generation. Our code and models are available at https://video-lavit.github.io.