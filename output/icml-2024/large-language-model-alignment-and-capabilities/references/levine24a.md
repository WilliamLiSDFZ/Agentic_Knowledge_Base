---
title: "Cell2Sentence: Teaching Large Language Models the Language of Biology"
source: "https://proceedings.mlr.press/v235/levine24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/levine24a/levine24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'algebraic-structures-in-machine-learning']
tags: ['single-cell-transcriptomics', 'large-language-models', 'gene-expression', 'cell-sentences', 'biological-adaptation']
venue: "ICML 2024"
tldr: "Introduces Cell2Sentence, a method that transforms gene expression data into text-like sequences to adapt large language models for single-cell biology tasks."
---

# Cell2Sentence: Teaching Large Language Models the Language of Biology

**Source**: [https://proceedings.mlr.press/v235/levine24a.html](https://proceedings.mlr.press/v235/levine24a.html)

**TLDR**: Introduces Cell2Sentence, a method that transforms gene expression data into text-like sequences to adapt large language models for single-cell biology tasks.

## Abstract

We introduce Cell2Sentence (C2S), a novel method to directly adapt large language models to a biological context, specifically single-cell transcriptomics. By transforming gene expression data into "cell sentences," C2S bridges the gap between natural language processing and biology. We demonstrate cell sentences enable the fine-tuning of language models for diverse tasks in biology, including cell generation, complex cell-type annotation, and direct data-driven text generation. Our experiments reveal that GPT-2, when fine-tuned with C2S, can generate biologically valid cells based on cell type inputs, and accurately predict cell types from cell sentences. This illustrates that language models, through C2S fine-tuning, can acquire a significant understanding of single-cell biology while maintaining robust text generation capabilities. C2S offers a flexible, accessible framework to integrate natural language processing with transcriptomics, utilizing existing models and libraries for a wide range of biological applications.