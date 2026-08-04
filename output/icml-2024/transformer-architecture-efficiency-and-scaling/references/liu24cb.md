---
title: "Timer: Generative Pre-trained Transformers Are Large Time Series Models"
source: "https://proceedings.mlr.press/v235/liu24cb.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24cb/liu24cb.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'transformer-architecture-efficiency-and-scaling']
tags: ['time-series', 'generative-pretraining', 'transformers', 'large-models', 'forecasting']
venue: "ICML 2024"
tldr: "Timer is a generative pre-trained transformer model for time series that serves as a large foundation model to overcome data-scarce performance bottlenecks."
---

# Timer: Generative Pre-trained Transformers Are Large Time Series Models

**Source**: [https://proceedings.mlr.press/v235/liu24cb.html](https://proceedings.mlr.press/v235/liu24cb.html)

**TLDR**: Timer is a generative pre-trained transformer model for time series that serves as a large foundation model to overcome data-scarce performance bottlenecks.

## Abstract

Deep learning has contributed remarkably to the advancement of time series analysis. Still, deep models can encounter performance bottlenecks in real-world data-scarce scenarios, which can be concealed due to the performance saturation with small models on current benchmarks. Meanwhile, large models have demonstrated great powers in these scenarios through large-scale pre-training. Continuous progress has been achieved with the emergence of large language models, exhibiting unprecedented abilities such as few-shot generalization, scalability, and task generality, which are however absent in small deep models. To change the status quo of training scenario-specific small models from scratch, this paper aims at the early development of large time series models (LTSM). During pre-training, we curate large-scale datasets with up to 1 billion time points, unify heterogeneous time series into single-series sequence (S3) format, and develop the GPT-style architecture toward LTSMs. To meet diverse application needs, we convert forecasting, imputation, and anomaly detection of time series into a unified generative task. The outcome of this study is a Time Series Transformer (Timer), which is generative pre-trained by next token prediction and adapted to various downstream tasks with promising capabilities as an LTSM. Code and datasets are available at: https://github.com/thuml/Large-Time-Series-Model.