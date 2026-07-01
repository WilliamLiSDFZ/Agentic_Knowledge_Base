---
title: "AutoTimes: Autoregressive Time Series Forecasters via Large Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/dcf88cbc8d01ce7309b83d0ebaeb9d29-Abstract-Conference.html"
categories: ['time-series-forecasting-and-analysis', 'llm-training-and-optimization-techniques']
tags: ['time-series-forecasting', 'large-language-models', 'autoregressive-pretraining']
venue: "NeurIPS 2024"
tldr: "AutoTimes adapts LLMs for scalable autoregressive time series forecasting by exploiting the sequential similarity between time series and natural language."
---

# AutoTimes: Autoregressive Time Series Forecasters via Large Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/dcf88cbc8d01ce7309b83d0ebaeb9d29-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/dcf88cbc8d01ce7309b83d0ebaeb9d29-Abstract-Conference.html)

**TLDR**: AutoTimes adapts LLMs for scalable autoregressive time series forecasting by exploiting the sequential similarity between time series and natural language.

## Abstract

Foundation models of time series have not been fully developed due to the limited availability of time series corpora and the underexploration of scalable pre-training. Based on the similar sequential formulation of time series and natural language, increasing research demonstrates the feasibility of leveraging large language models (LLM) for time series. Nevertheless, the inherent autoregressive property and decoder-only architecture of LLMs have not been fully considered, resulting in insufficient utilization of LLM abilities. To fully revitalize the general-purpose token transition and multi-step generation capability of large language models, we propose AutoTimes to repurpose LLMs as autoregressive time series forecasters, which projects time series into the embedding space of language tokens and autoregressively generates future predictions with arbitrary lengths. Compatible with any decoder-only LLMs, the consequent forecaster exhibits the flexibility of the lookback length and scalability with larger LLMs. Further, we formulate time series as prompts, extending the context for prediction beyond the lookback window, termed in-context forecasting. By introducing LLM-embedded textual timestamps, AutoTimes can utilize chronological information to align multivariate time series. Empirically, AutoTimes achieves state-of-the-art with 0.1% trainable parameters and over $5\times$ training/inference speedup compared to advanced LLM-based forecasters. Code is available at this repository: https://github.com/thuml/AutoTimes.