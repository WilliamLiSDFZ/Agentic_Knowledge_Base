---
title: "Trustworthy Alignment of Retrieval-Augmented Large Language Models via Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/zhang24bg.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24bg/zhang24bg.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'information-retrieval-and-recommendation-systems']
tags: ['retrieval-augmented-generation', 'LLM-alignment', 'trustworthiness', 'reinforcement-learning', 'hallucination']
venue: "ICML 2024"
tldr: "Proposes a reinforcement learning framework to improve the trustworthiness of retrieval-augmented large language models."
---

# Trustworthy Alignment of Retrieval-Augmented Large Language Models via Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/zhang24bg.html](https://proceedings.mlr.press/v235/zhang24bg.html)

**TLDR**: Proposes a reinforcement learning framework to improve the trustworthiness of retrieval-augmented large language models.

## Abstract

Trustworthiness is an essential prerequisite for the real-world application of large language models. In this paper, we focus on the trustworthiness of language models with respect to retrieval augmentation. Despite being supported with external evidence, retrieval-augmented generation still suffers from hallucinations, one primary cause of which is the conflict between contextual and parametric knowledge. We deem that retrieval-augmented language models have the inherent capabilities of supplying response according to both contextual and parametric knowledge. Inspired by aligning language models with human preference, we take the first step towards aligning retrieval-augmented language models to a status where it responds relying merely on the external evidence and disregards the interference of parametric knowledge. Specifically, we propose a reinforcement learning based algorithm Trustworthy-Alignment, theoretically and experimentally demonstrating large language models’ capability of reaching a trustworthy status without explicit supervision on how to respond. Our work highlights the potential of large language models on exploring its intrinsic abilities by its own and expands the application scenarios of alignment from fulfilling human preference to creating trustworthy agents.