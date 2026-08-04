---
title: "MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Cases"
source: "https://proceedings.mlr.press/v235/liu24ce.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24ce/liu24ce.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'large-language-model-alignment-and-capabilities']
tags: ['on-device-LLM', 'sub-billion-parameters', 'mobile-deployment', 'model-efficiency', 'architecture-design']
venue: "ICML 2024"
tldr: "MobileLLM optimizes sub-billion parameter language models for mobile devices through architecture design choices prioritizing depth and weight sharing over simple scaling."
---

# MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Cases

**Source**: [https://proceedings.mlr.press/v235/liu24ce.html](https://proceedings.mlr.press/v235/liu24ce.html)

**TLDR**: MobileLLM optimizes sub-billion parameter language models for mobile devices through architecture design choices prioritizing depth and weight sharing over simple scaling.

## Abstract

This paper addresses the growing need for efficient large language models (LLMs) on mobile devices, driven by increasing cloud costs and latency concerns. We focus on designing top-quality LLMs with fewer than a billion parameters, a practical choice for mobile deployment. Contrary to prevailing belief emphasizing the pivotal role of data and parameter quantity in determining model quality, our investigation underscores the significance of model architecture for sub-billion scale LLMs. Leveraging deep and thin architectures, coupled with embedding sharing and grouped-query attention mechanisms, we establish a strong baseline network denoted as MobileLLM, which attains a remarkable 2.7%/4.3% accuracy boost over preceding 125M/350M state-of-the-art models. Additionally, we propose an immediate block-wise weight-sharing approach with no increase in model size and only marginal latency overhead. The resultant models, denoted as MobileLLM-LS, demonstrate a further accuracy enhancement of 0.7%/0.8% than MobileLLM 125M/350M. Moreover, MobileLLM model family shows significant improvements compared to previous sub-billion models on chat benchmarks, and demonstrates close correctness to LLaMA-v2 7B in API calling tasks, highlighting the capability of small models for common on-device use cases.