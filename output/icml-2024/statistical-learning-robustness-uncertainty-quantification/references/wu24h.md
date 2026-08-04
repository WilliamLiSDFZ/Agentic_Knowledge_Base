---
title: "A Resilient and Accessible Distribution-Preserving Watermark for Large Language Models"
source: "https://proceedings.mlr.press/v235/wu24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24h/wu24h.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['LLM-watermarking', 'distribution-preservation', 'resilience', 'text-generation']
venue: "ICML 2024"
tldr: "Proposes a watermarking scheme for LLMs that embeds covert signals while provably preserving the original output token distribution."
---

# A Resilient and Accessible Distribution-Preserving Watermark for Large Language Models

**Source**: [https://proceedings.mlr.press/v235/wu24h.html](https://proceedings.mlr.press/v235/wu24h.html)

**TLDR**: Proposes a watermarking scheme for LLMs that embeds covert signals while provably preserving the original output token distribution.

## Abstract

Watermarking techniques offer a promising way to identify machine-generated content via embedding covert information into the contents generated from language models. A challenge in the domain lies in preserving the distribution of original generated content after watermarking. Our research extends and improves upon existing watermarking framework, placing emphasis on the importance of a Distribution-Preserving (DiP) watermark. Contrary to the current strategies, our proposed DiPmark simultaneously preserves the original token distribution during watermarking (distribution-preserving), is detectable without access to the language model API and prompts (accessible), and is provably robust to moderate changes of tokens (resilient). DiPmark operates by selecting a random set of tokens prior to the generation of a word, then modifying the token distribution through a distribution-preserving reweight function to enhance the probability of these selected tokens during the sampling process. Extensive empirical evaluation on various language models and tasks demonstrates our approach’s distribution-preserving property, accessibility, and resilience, making it a effective solution for watermarking tasks that demand impeccable quality preservation.