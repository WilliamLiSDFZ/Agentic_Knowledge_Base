---
title: "FrameQuant: Flexible Low-Bit Quantization for Transformers"
source: "https://proceedings.mlr.press/v235/adepu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/adepu24a/adepu24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling']
tags: ['quantization', 'transformers', 'post-training-quantization', 'low-bit', 'frames']
venue: "ICML 2024"
tldr: "FrameQuant introduces flexible low-bit quantization for transformers using frame theory for improved post-training compression."
---

# FrameQuant: Flexible Low-Bit Quantization for Transformers

**Source**: [https://proceedings.mlr.press/v235/adepu24a.html](https://proceedings.mlr.press/v235/adepu24a.html)

**TLDR**: FrameQuant introduces flexible low-bit quantization for transformers using frame theory for improved post-training compression.

## Abstract

Transformers are the backbone of powerful foundation models for many Vision and Natural Language Processing tasks. But their compute and memory/storage footprint is large, and so, serving such models is expensive often requiring high-end hardware. To mitigate this difficulty, Post-Training Quantization seeks to modify a pre-trained model and quantize it to eight bits or lower, significantly boosting compute/memory/latency efficiency. Such models have been successfully quantized to four bits with some performance loss. In this work, we outline a simple scheme to quantize Transformer-based models to just two bits (plus some overhead) with only a small drop in accuracy. Key to our formulation is a concept borrowed from Harmonic analysis called Fusion Frames. Our main finding is that the quantization must take place not in the original weight space, but instead in the Fusion Frame representations. If quantization is interpreted as the addition of noise, our casting of the problem allows invoking an extensive body of known consistent recovery and noise robustness guarantees. Further, if desired, de-noising filters are known in closed form. We show empirically, via a variety of experiments, that (almost) two-bit quantization for Transformer models promises sizable efficiency gains. The code is available at https://github.com/vsingh-group/FrameQuant