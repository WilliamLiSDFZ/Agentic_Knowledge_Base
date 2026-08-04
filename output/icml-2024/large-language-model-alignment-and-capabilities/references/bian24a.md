---
title: "Multi-Patch Prediction: Adapting Language Models for Time Series Representation Learning"
source: "https://proceedings.mlr.press/v235/bian24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bian24a/bian24a.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'large-language-model-alignment-and-capabilities']
tags: ['LLM', 'time-series', 'representation-learning', 'multi-patch-prediction']
venue: "ICML 2024"
tldr: "This paper introduces aLLM4TS, a framework adapting large language models for time-series representation learning via self-supervised multi-patch prediction."
---

# Multi-Patch Prediction: Adapting Language Models for Time Series Representation Learning

**Source**: [https://proceedings.mlr.press/v235/bian24a.html](https://proceedings.mlr.press/v235/bian24a.html)

**TLDR**: This paper introduces aLLM4TS, a framework adapting large language models for time-series representation learning via self-supervised multi-patch prediction.

## Abstract

In this study, we present $\text{aL\small{LM}4T\small{S}}$, an innovative framework that adapts Large Language Models (LLMs) for time-series representation learning. Central to our approach is that we reconceive time-series forecasting as a self-supervised, multi-patch prediction task, which, compared to traditional mask-and-reconstruction methods, captures temporal dynamics in patch representations more effectively. Our strategy encompasses two-stage training: (i). a causal continual pre-training phase on various time-series datasets, anchored on next patch prediction, effectively syncing LLM capabilities with the intricacies of time-series data; (ii). fine-tuning for multi-patch prediction in the targeted time-series context. A distinctive element of our framework is the patch-wise decoding layer, which departs from previous methods reliant on sequence-level decoding. Such a design directly transposes individual patches into temporal sequences, thereby significantly bolstering the model’s proficiency in mastering temporal patch-based representations. $\text{aL\small{LM}4T\small{S}}$ demonstrates superior performance in several downstream tasks, proving its effectiveness in deriving temporal representations with enhanced transferability and marking a pivotal advancement in the adaptation of LLMs for time-series analysis.