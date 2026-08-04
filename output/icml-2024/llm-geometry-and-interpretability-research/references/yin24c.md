---
title: "Characterizing Truthfulness in Large Language Model Generations with Local Intrinsic Dimension"
source: "https://proceedings.mlr.press/v235/yin24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yin24c/yin24c.pdf"
categories: ['llm-geometry-and-interpretability-research']
tags: ['LLM-truthfulness', 'intrinsic-dimension', 'uncertainty', 'hallucination']
venue: "ICML 2024"
tldr: "Local intrinsic dimension of LLM hidden representations is used to characterize and predict the truthfulness of generated text."
---

# Characterizing Truthfulness in Large Language Model Generations with Local Intrinsic Dimension

**Source**: [https://proceedings.mlr.press/v235/yin24c.html](https://proceedings.mlr.press/v235/yin24c.html)

**TLDR**: Local intrinsic dimension of LLM hidden representations is used to characterize and predict the truthfulness of generated text.

## Abstract

We study how to characterize and predict the truthfulness of texts generated from large language models (LLMs), which serves as a crucial step in building trust between humans and LLMs. Although several approaches based on entropy or verbalized uncertainty have been proposed to calibrate model predictions, these methods are often intractable, sensitive to hyperparameters, and less reliable when applied in generative tasks with LLMs. In this paper, we suggest investigating internal activations and quantifying LLM’s truthfulness using the local intrinsic dimension (LID) of model activations. Through experiments on four question answering (QA) datasets, we demonstrate the effectiveness of our proposed method. Additionally, we study intrinsic dimensions in LLMs and their relations with model layers, autoregressive language modeling, and the training of LLMs, revealing that intrinsic dimensions can be a powerful approach to understanding LLMs.