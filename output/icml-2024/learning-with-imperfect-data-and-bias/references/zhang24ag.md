---
title: "Conditional Language Learning with Context"
source: "https://proceedings.mlr.press/v235/zhang24ag.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ag/zhang24ag.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'learning-with-imperfect-data-and-bias']
tags: ['language-modeling', 'conditional-learning', 'context-awareness']
venue: "ICML 2024"
tldr: "Proposes conditional causal language modeling that selectively learns from context to avoid absorbing spurious corpus statistics during fine-tuning."
---

# Conditional Language Learning with Context

**Source**: [https://proceedings.mlr.press/v235/zhang24ag.html](https://proceedings.mlr.press/v235/zhang24ag.html)

**TLDR**: Proposes conditional causal language modeling that selectively learns from context to avoid absorbing spurious corpus statistics during fine-tuning.

## Abstract

Language models can learn sophisticated language understanding skills from fitting raw text. They also unselectively learn useless corpus statistics and biases, especially during finetuning on domain-specific corpora. In this paper, we propose a simple modification to causal language modeling called conditional finetuning, which performs language modeling conditioned on a context. We show that a context can "explain away" certain corpus statistics and make the model avoid learning them. In this fashion, conditional finetuning achieves selective learning from a corpus, learning knowledge useful for downstream tasks while avoiding learning useless corpus statistics like topic biases. This selective learning effect leads to less forgetting and better stability-plasticity tradeoff in domain finetuning, potentially benefitting lifelong learning with language models.