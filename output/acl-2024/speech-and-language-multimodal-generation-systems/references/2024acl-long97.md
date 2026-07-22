---
title: "Generative Pre-trained Speech Language Model with Efficient Hierarchical Transformer"
source: "https://aclanthology.org/2024.acl-long.97/"
categories: ['speech-and-language-multimodal-generation-systems', 'transformer-architecture-analysis-and-design']
tags: ['speech-language-model', 'hierarchical-transformer', 'audio-codec']
venue: "ACL 2024"
tldr: "Introduces GPST, a hierarchical transformer for generative pre-trained speech modeling that efficiently handles long neural audio codec sequences."
---

# Generative Pre-trained Speech Language Model with Efficient Hierarchical Transformer

**Source**: [https://aclanthology.org/2024.acl-long.97/](https://aclanthology.org/2024.acl-long.97/)

**TLDR**: Introduces GPST, a hierarchical transformer for generative pre-trained speech modeling that efficiently handles long neural audio codec sequences.

## Abstract

AbstractWhile recent advancements in speech language models have achieved significant progress, they face remarkable challenges in modeling the long acoustic sequences of neural audio codecs. In this paper, we introduce Generative Pre-trained Speech Transformer (GPST), a hierarchical transformer designed for efficient speech language modeling. GPST quantizes audio waveforms into two distinct types of discrete speech representations and integrates them within a hierarchical transformer architecture, allowing for a unified one-stage generation process and enhancing Hi-Res audio generation capabilities. By training on large corpora of speeches in an end-to-end unsupervised manner, GPST can generate syntactically consistent speech with diverse speaker identities. Given a brief 3-second prompt, GPST can produce natural and coherent personalized speech, demonstrating in-context learning abilities. Moreover, our approach can be easily extended to spoken cross-lingual speech generation by incorporating multi-lingual semantic tokens and universal acoustic tokens. Experimental results indicate that GPST significantly outperforms the existing speech language models in terms of word error rate, speech quality, and speaker similarity. See https://youngsheen.github.io/GPST/demo for demo samples.