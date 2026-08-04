---
title: "Two Stones Hit One Bird: Bilevel Positional Encoding for Better Length Extrapolation"
source: "https://proceedings.mlr.press/v235/he24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/he24c/he24c.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'large-language-model-alignment-and-capabilities']
tags: ['positional-encoding', 'length-extrapolation', 'transformers']
venue: "ICML 2024"
tldr: "Bilevel Positional Encoding blends intra-segment and inter-segment encodings to improve length extrapolation in Transformer models."
---

# Two Stones Hit One Bird: Bilevel Positional Encoding for Better Length Extrapolation

**Source**: [https://proceedings.mlr.press/v235/he24c.html](https://proceedings.mlr.press/v235/he24c.html)

**TLDR**: Bilevel Positional Encoding blends intra-segment and inter-segment encodings to improve length extrapolation in Transformer models.

## Abstract

In this work, we leverage the intrinsic segmentation of language sequences and design a new positional encoding method called Bilevel Positional Encoding (BiPE). For each position, our BiPE blends an intra-segment encoding and an inter-segment encoding. The intra-segment encoding identifies the locations within a segment and helps the model capture the semantic information therein via absolute positional encoding. The inter-segment encoding specifies the segment index, models the relationships between segments, and aims to improve extrapolation capabilities via relative positional encoding. Theoretical analysis shows this disentanglement of positional information makes learning more effective. The empirical results also show that our BiPE has superior length extrapolation capabilities across a wide range of tasks in diverse text modalities.