---
title: "Extreme Compression of Large Language Models via Additive Quantization"
source: "https://proceedings.mlr.press/v235/egiazarian24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/egiazarian24a/egiazarian24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'sampling-compression-and-dimensionality-reduction']
tags: ['model-compression', 'quantization', 'large-language-models', 'additive-quantization', 'extreme-compression']
venue: "ICML 2024"
tldr: "Proposes an additive quantization approach for extreme LLM compression to 2-bit and below, achieving state-of-the-art performance at very low bit counts."
---

# Extreme Compression of Large Language Models via Additive Quantization

**Source**: [https://proceedings.mlr.press/v235/egiazarian24a.html](https://proceedings.mlr.press/v235/egiazarian24a.html)

**TLDR**: Proposes an additive quantization approach for extreme LLM compression to 2-bit and below, achieving state-of-the-art performance at very low bit counts.

## Abstract

The emergence of accurate open large language models (LLMs) has led to a race towards performant quantization techniques which can enable their execution on end-user devices. In this paper, we revisit the problem of “extreme” LLM compression—defined as targeting extremely low bit counts, such as 2 to 3 bits per parameter—from the point of view of classic methods in Multi-Codebook Quantization (MCQ). Our algorithm, called AQLM, generalizes the classic Additive Quantization (AQ) approach for information retrieval to advance the state-of-the-art in LLM compression, via two innovations: 1) learned additive quantization of weight matrices in input-adaptive fashion, and 2) joint optimization of codebook parameters across each transformer blocks. Broadly, AQLM is the first scheme that is Pareto optimal in terms of accuracy-vs-model-size when compressing to less than 3 bits per parameter, and significantly improves upon all known schemes in the extreme compression (2bit) regime. In addition, AQLM is practical: we provide fast GPU and CPU implementations of AQLM for token generation, which enable us to match or outperform optimized FP16 implementations for speed, while executing in a much smaller memory footprint.