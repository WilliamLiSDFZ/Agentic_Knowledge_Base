---
title: "StableMask: Refining Causal Masking in Decoder-only Transformer"
source: "https://proceedings.mlr.press/v235/yin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yin24a/yin24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling']
tags: ['transformer', 'causal-masking', 'relative-position-encoding', 'decoder']
venue: "ICML 2024"
tldr: "StableMask refines causal masking in decoder-only transformers to address limitations in attention normalization and position encoding."
---

# StableMask: Refining Causal Masking in Decoder-only Transformer

**Source**: [https://proceedings.mlr.press/v235/yin24a.html](https://proceedings.mlr.press/v235/yin24a.html)

**TLDR**: StableMask refines causal masking in decoder-only transformers to address limitations in attention normalization and position encoding.

## Abstract

The decoder-only Transformer architecture with causal masking and relative position encoding (RPE) has become the de facto choice in language modeling. Despite its exceptional performance across various tasks, we have identified two limitations: First, it prevents all attended tokens from having zero weights during the softmax stage, even if the current embedding has sufficient self-contained information. This compels the model to assign disproportional excessive attention to specific tokens. Second, RPE-based Transformers are not universal approximators due to their limited capacity at encoding absolute positional information, which limits their application in position-critical tasks. In this work, we propose StableMask: a parameter-free method to address both limitations by refining the causal mask. It introduces pseudo-attention values to balance attention distributions and encodes absolute positional information via a progressively decreasing mask ratio. StableMask’s effectiveness is validated both theoretically and empirically, showing significant enhancements in language models with parameter sizes ranging from 71M to 1.4B across diverse datasets and encoding methods. We further show that it supports integration with existing optimization techniques, making it easily usable in practical applications.