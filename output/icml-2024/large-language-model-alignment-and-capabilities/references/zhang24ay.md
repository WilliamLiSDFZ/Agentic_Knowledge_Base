---
title: "How Language Model Hallucinations Can Snowball"
source: "https://proceedings.mlr.press/v235/zhang24ay.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ay/zhang24ay.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-geometry-and-interpretability-research']
tags: ['hallucination', 'language-models', 'snowballing-errors', 'factuality', 'LLM-reasoning']
venue: "ICML 2024"
tldr: "Demonstrates that LLM hallucinations can snowball from initial errors even when the model could separately identify those errors as incorrect."
---

# How Language Model Hallucinations Can Snowball

**Source**: [https://proceedings.mlr.press/v235/zhang24ay.html](https://proceedings.mlr.press/v235/zhang24ay.html)

**TLDR**: Demonstrates that LLM hallucinations can snowball from initial errors even when the model could separately identify those errors as incorrect.

## Abstract

A major risk of using language models in practical applications is their tendency to hallucinate incorrect statements. Hallucinations are often attributed to knowledge gaps in LMs, but we show that LMs sometimes produce hallucinations that they can separately recognize as incorrect. To do this, we construct three question-answering datasets where LMs often state an incorrect answer which is followed by an explanation with at least one incorrect claim. Crucially, we find that GPT-3.5, GPT-4, and LLaMA2-70B-chat can identify 67%, 87%, and 94% of these incorrect claims, respectively. We show that this phenomenon doesn’t disappear under higher temperatures sampling, beam search, and zero-shot chain-of-thought prompting. These findings reveal that LM hallucinations can snowball: early mistakes by an LM can lead to more mistakes that otherwise would not be made.