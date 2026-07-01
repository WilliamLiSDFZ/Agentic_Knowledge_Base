---
title: "Stratified Prediction-Powered Inference for Effective Hybrid Evaluation of Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/c9fcd02e6445c7dfbad6986abee53d0d-Abstract-Conference.html"
categories: ['statistical-inference-and-text-generation-methods\n\nhmm,-let-me-reconsider---looking-more-carefully-at-the-cluster:\n\n**score-matching-and-sampling-methods**', 'ai-benchmarking-and-evaluation-methodology']
tags: ['prediction-powered-inference', 'stratification', 'language-model-evaluation', 'hybrid-evaluation', 'statistical-estimation']
venue: "NeurIPS 2024"
tldr: "Improves prediction-powered inference for language model evaluation by incorporating stratification to reduce variance and increase efficiency with limited human labels."
---

# Stratified Prediction-Powered Inference for Effective Hybrid Evaluation of Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/c9fcd02e6445c7dfbad6986abee53d0d-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/c9fcd02e6445c7dfbad6986abee53d0d-Abstract-Conference.html)

**TLDR**: Improves prediction-powered inference for language model evaluation by incorporating stratification to reduce variance and increase efficiency with limited human labels.

## Abstract

Prediction-powered inference (PPI) is a method that improves statistical estimates based on limited human-labeled data.  PPI achieves this by combining small amounts of human-labeled data with larger amounts of data labeled by a reasonably accurate---but potentially biased---automatic system, in a way that results in tighter confidence intervals for certain parameters of interest (e.g., the mean performance of a language model). In this paper, we propose a method called Stratified Prediction-Powered Inference (StratPPI), in which we show that the basic PPI estimates can be considerably improved by employing simple data stratification strategies. Without making any assumptions on the underlying automatic labeling system or data distribution, we derive an algorithm for computing provably valid confidence intervals for parameters of any dimensionality that is based on stratified sampling. In particular, we show both theoretically and empirically that, with appropriate choices of stratification and sample allocation, our approach can provide substantially tighter confidence intervals than  unstratified  approaches. Specifically, StratPPI  is expected to improve in cases where the performance of the autorater varies across different conditional distributions of the target data.