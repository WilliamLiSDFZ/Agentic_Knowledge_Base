---
title: "IIANet: An Intra- and Inter-Modality Attention Network for Audio-Visual Speech Separation"
source: "https://proceedings.mlr.press/v235/li24cf.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24cf/li24cf.pdf"
categories: ['audio-and-music-generation-diffusion-models']
tags: ['audio-visual', 'speech-separation', 'multimodal-fusion']
venue: "ICML 2024"
tldr: "IIANet introduces intra- and inter-modality attention mechanisms for improved audio-visual speech separation across temporal scales."
---

# IIANet: An Intra- and Inter-Modality Attention Network for Audio-Visual Speech Separation

**Source**: [https://proceedings.mlr.press/v235/li24cf.html](https://proceedings.mlr.press/v235/li24cf.html)

**TLDR**: IIANet introduces intra- and inter-modality attention mechanisms for improved audio-visual speech separation across temporal scales.

## Abstract

Recent research has made significant progress in designing fusion modules for audio-visual speech separation. However, they predominantly focus on multi-modal fusion at a single temporal scale of auditory and visual features without employing selective attention mechanisms, which is in sharp contrast with the brain. To address this, We propose a novel model called intra- and inter-attention network (IIANet), which leverages the attention mechanism for efficient audio-visual feature fusion. IIANet consists of two types of attention blocks: intra-attention (IntraA) and inter-attention (InterA) blocks, where the InterA blocks are distributed at the top, middle and bottom of IIANet. Heavily inspired by the way how human brain selectively focuses on relevant content at various temporal scales, these blocks maintain the ability to learn modality-specific features and enable the extraction of different semantics from audio-visual features. Comprehensive experiments on three standard audio-visual separation benchmarks (LRS2, LRS3, and VoxCeleb2) demonstrate the effectiveness of IIANet, outperforming previous state-of-the-art methods while maintaining comparable inference time. In particular, the fast version of IIANet (IIANet-fast) has only 7% of CTCNet’s MACs and is 40% faster than CTCNet on CPUs while achieving better separation quality, showing the great potential of attention mechanism for efficient and effective multimodal fusion.