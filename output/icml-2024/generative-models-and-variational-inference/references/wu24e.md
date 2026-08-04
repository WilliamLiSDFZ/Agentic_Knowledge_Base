---
title: "NExT-GPT: Any-to-Any Multimodal LLM"
source: "https://proceedings.mlr.press/v235/wu24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24e/wu24e.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'generative-models-and-variational-inference']
tags: ['multimodal-LLM', 'any-to-any-generation', 'multi-modal-output', 'large-language-models']
venue: "ICML 2024"
tldr: "NExT-GPT is an any-to-any multimodal LLM capable of both understanding and generating content across text, image, audio, and video modalities."
---

# NExT-GPT: Any-to-Any Multimodal LLM

**Source**: [https://proceedings.mlr.press/v235/wu24e.html](https://proceedings.mlr.press/v235/wu24e.html)

**TLDR**: NExT-GPT is an any-to-any multimodal LLM capable of both understanding and generating content across text, image, audio, and video modalities.

## Abstract

While recently Multimodal Large Language Models (MM-LLMs) have made exciting strides, they mostly fall prey to the limitation of only input-side multimodal understanding, without the ability to produce content in multiple modalities. As we humans always perceive the world and communicate with people through various modalities, developing any-to-any MM-LLMs capable of accepting and delivering content in any modality becomes essential to human-level AI. To fill the gap, we present an end-to-end general-purpose any-to-any MM-LLM system, NExT-GPT. We connect an LLM with multimodal adaptors and different diffusion decoders, enabling NExT-GPT to perceive inputs and generate outputs in arbitrary combinations of text, image, video, and audio. By leveraging the existing well-trained high-performing encoders and decoders, NExT-GPT is tuned with only a small amount of parameter (1%) of certain projection layers, which not only benefits low-cost training but also facilitates convenient expansion to more potential modalities. Moreover, we introduce a modality-switching instruction tuning (MosIT) and manually curate a high-quality dataset for MosIT, based on which NExT-GPT is empowered with complex cross-modal semantic understanding and content generation. Overall, our research showcases the promising possibility of building a unified AI agent capable of modeling universal modalities, paving the way for more human-like AI research in the community.