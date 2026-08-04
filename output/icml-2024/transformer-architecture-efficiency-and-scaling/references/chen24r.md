---
title: "Exact Conversion of In-Context Learning to Model Weights in Linearized-Attention Transformers"
source: "https://proceedings.mlr.press/v235/chen24r.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24r/chen24r.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'sequence-models-for-memory-and-state']
tags: ['in-context-learning', 'linearized-attention', 'weight-conversion', 'transformers']
venue: "ICML 2024"
tldr: "In-context learning in linearized-attention transformers can be exactly converted into equivalent model weight updates, providing a mechanistic interpretation."
---

# Exact Conversion of In-Context Learning to Model Weights in Linearized-Attention Transformers

**Source**: [https://proceedings.mlr.press/v235/chen24r.html](https://proceedings.mlr.press/v235/chen24r.html)

**TLDR**: In-context learning in linearized-attention transformers can be exactly converted into equivalent model weight updates, providing a mechanistic interpretation.

## Abstract

In-Context Learning (ICL) has been a powerful emergent property of large language models that has attracted increasing attention in recent years. In contrast to regular gradient-based learning, ICL is highly interpretable and does not require parameter updates. In this paper, we show that, for linearized transformer networks, ICL can be made explicit and permanent through the inclusion of bias terms. We mathematically demonstrate the equivalence between a model with ICL demonstration prompts and the same model with the additional bias terms. Our algorithm (ICLCA) allows for exact conversion in an inexpensive manner. Existing methods are not exact and require expensive parameter updates. We demonstrate the efficacy of our approach through experiments that show the exact incorporation of ICL tokens into a linear transformer. We further suggest how our method can be adapted to achieve cheap approximate conversion of ICL tokens, even in regular transformer networks that are not linearized. Our experiments on GPT-2 show that, even though the conversion is only approximate, the model still gains valuable context from the included bias terms.