---
title: "HALC: Object Hallucination Reduction via Adaptive Focal-Contrast Decoding"
source: "https://proceedings.mlr.press/v235/chen24bi.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24bi/chen24bi.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'sampling-compression-and-dimensionality-reduction']
tags: ['hallucination-reduction', 'vision-language-models', 'focal-contrast-decoding']
venue: "ICML 2024"
tldr: "HALC reduces object hallucinations in large vision-language models via adaptive focal-contrast decoding."
---

# HALC: Object Hallucination Reduction via Adaptive Focal-Contrast Decoding

**Source**: [https://proceedings.mlr.press/v235/chen24bi.html](https://proceedings.mlr.press/v235/chen24bi.html)

**TLDR**: HALC reduces object hallucinations in large vision-language models via adaptive focal-contrast decoding.

## Abstract

While large vision-language models (LVLMs) have demonstrated impressive capabilities in interpreting multi-modal contexts, they invariably suffer from object hallucinations (OH). We introduce HALC, a novel decoding algorithm designed to mitigate OH in LVLMs. HALC leverages distinct fine-grained optimal visual information in vision-language tasks and operates on both local and global contexts simultaneously. Specifically, HALC integrates a robust auto-focal grounding mechanism (locally) to correct hallucinated tokens on the fly, and a specialized beam search algorithm (globally) to significantly reduce OH while preserving text generation quality. Additionally, HALC can be integrated into any LVLMs as a plug-and-play module without extra training. Extensive experimental studies demonstrate HALC’s effectiveness in reducing OH, outperforming state-of-the-arts across four benchmarks. Code is released at https://github.com/BillChan226/HALC.