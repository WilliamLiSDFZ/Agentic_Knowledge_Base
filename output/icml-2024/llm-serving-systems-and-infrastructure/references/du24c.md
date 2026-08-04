---
title: "GliDe with a CaPE: A Low-Hassle Method to Accelerate Speculative Decoding"
source: "https://proceedings.mlr.press/v235/du24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/du24c/du24c.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'llm-serving-systems-and-infrastructure']
tags: ['speculative-decoding', 'LLM-inference', 'draft-model', 'KV-cache']
venue: "ICML 2024"
tldr: "GliDe and CaPE are two lightweight modifications to speculative decoding that improve decoding speed by better utilizing draft model context and cache."
---

# GliDe with a CaPE: A Low-Hassle Method to Accelerate Speculative Decoding

**Source**: [https://proceedings.mlr.press/v235/du24c.html](https://proceedings.mlr.press/v235/du24c.html)

**TLDR**: GliDe and CaPE are two lightweight modifications to speculative decoding that improve decoding speed by better utilizing draft model context and cache.

## Abstract

Speculative decoding is a relatively new decoding framework that leverages small and efficient draft models to reduce the latency of LLMs. In this study, we introduce GliDe and CaPE, two low-hassle modifications to vanilla speculative decoding to further improve the decoding speed of a frozen LLM. Specifically, GliDe is a modified draft model architecture that reuses the cached keys and values from the target LLM, while CaPE is a proposal expansion method that uses the draft model’s confidence scores to help select additional candidate tokens for verification. Extensive experiments on different benchmarks demonstrate that our proposed GliDe draft model significantly reduces the expected decoding latency. Additional evaluation using walltime reveals that GliDe can accelerate Vicuna models up to 2.17x and further extend the improvement to 2.61x with CaPE. We will release our code, data, and the trained draft models.