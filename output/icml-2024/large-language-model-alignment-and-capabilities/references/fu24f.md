---
title: "PinNet: Pinpoint Instructive Information for Retrieval Augmented Code-to-Text Generation"
source: "https://proceedings.mlr.press/v235/fu24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fu24f/fu24f.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'large-language-model-alignment-and-capabilities']
tags: ['retrieval-augmented-generation', 'code-summarization', 'information-pinpointing']
venue: "ICML 2024"
tldr: "PinNet selectively extracts instructive information from retrieved examples to improve retrieval-augmented code-to-text generation."
---

# PinNet: Pinpoint Instructive Information for Retrieval Augmented Code-to-Text Generation

**Source**: [https://proceedings.mlr.press/v235/fu24f.html](https://proceedings.mlr.press/v235/fu24f.html)

**TLDR**: PinNet selectively extracts instructive information from retrieved examples to improve retrieval-augmented code-to-text generation.

## Abstract

Automatically generating high-quality code descriptions greatly improves the readability and maintainability of the codebase. Recently, retrieval augmented code-to-text generation has proven to be an effective solution, which has achieved state-of-the-art results on various benchmarks. It brings out the potential to leverage large unlabeled code descriptions to further improve the generation quality. Despite the promising performance, retrieval-augmented models however suffer from being deluded by inconducive retrieved references, due to irrelevant or even misleading information contained therein. To this end, we design PinNet, a new framework for code-to-text generation. PinNet relies on a discriminator to measure how well the retrievals match the semantics of the input code. Remarkably, the hidden representation of the reference before the output layer of the discriminator can be leveraged to significantly improve the code-to-text generation by modifying the attention weights. It essentially pays high attention to valuable information and eliminates misleadingness. To effectively execute this idea, we also propose a novel contrastive learning method to quantify the semantical similarities between unlabeled references. Using extensive experiments on code summarization and SQL-to-text generation, we demonstrate that the proposed method can significantly outperform all of the baselines.