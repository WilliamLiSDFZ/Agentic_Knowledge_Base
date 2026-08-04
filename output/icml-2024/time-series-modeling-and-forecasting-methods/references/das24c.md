---
title: "A decoder-only foundation model for time-series forecasting"
source: "https://proceedings.mlr.press/v235/das24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/das24c/das24c.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'transformer-architecture-efficiency-and-scaling']
tags: ['time-series-forecasting', 'foundation-model', 'decoder-only', 'zero-shot', 'large-language-models']
venue: "ICML 2024"
tldr: "Proposes a decoder-only transformer foundation model for time-series forecasting that achieves near state-of-the-art zero-shot performance across diverse datasets."
---

# A decoder-only foundation model for time-series forecasting

**Source**: [https://proceedings.mlr.press/v235/das24c.html](https://proceedings.mlr.press/v235/das24c.html)

**TLDR**: Proposes a decoder-only transformer foundation model for time-series forecasting that achieves near state-of-the-art zero-shot performance across diverse datasets.

## Abstract

Motivated by recent advances in large language models for Natural Language Processing (NLP), we design a time-series foundation model for forecasting whose out-of-the-box zero-shot performance on a variety of public datasets comes close to the accuracy of state-of-the-art supervised forecasting models for each individual dataset. Our model is based on pretraining a decoder style attention model with input patching, using a large time-series corpus comprising both real-world and synthetic datasets. Experiments on a diverse set of previously unseen forecasting datasets suggests that the model can yield accurate zero-shot forecasts across different domains, forecasting horizons and temporal granularities.