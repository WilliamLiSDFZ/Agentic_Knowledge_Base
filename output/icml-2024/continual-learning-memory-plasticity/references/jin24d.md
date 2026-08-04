---
title: "What Will My Model Forget? Forecasting Forgotten Examples in Language Model Refinement"
source: "https://proceedings.mlr.press/v235/jin24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jin24d/jin24d.pdf"
categories: ['continual-learning-memory-plasticity', 'large-language-model-alignment-and-capabilities']
tags: ['catastrophic-forgetting', 'language-model-refinement', 'forecasting-forgetting', 'continual-learning']
venue: "ICML 2024"
tldr: "A method is proposed to forecast which examples a language model will forget during refinement, enabling targeted replay to prevent catastrophic forgetting."
---

# What Will My Model Forget? Forecasting Forgotten Examples in Language Model Refinement

**Source**: [https://proceedings.mlr.press/v235/jin24d.html](https://proceedings.mlr.press/v235/jin24d.html)

**TLDR**: A method is proposed to forecast which examples a language model will forget during refinement, enabling targeted replay to prevent catastrophic forgetting.

## Abstract

Language models deployed in the wild make errors. However, simply updating the model with the corrected error instances causes catastrophic forgetting—the updated model makes errors on instances learned during the instruction tuning or upstream training phase. Randomly replaying upstream data yields unsatisfactory performance and often comes with high variance and poor controllability. To this end, we try to forecast upstream examples that will be forgotten due to a model update for improved controllability of the replay process and interpretability. We train forecasting models given a collection of online learned examples and corresponding forgotten upstream pre-training examples. We propose a partially interpretable forecasting model based on the observation that changes in pre-softmax logit scores of pretraining examples resemble that of online learned examples, which performs decently on BART but fails on T5 models. We further show a black-box classifier based on inner products of example representations achieves better forecasting performance over a series of setups. Finally, we show that we reduce forgetting of upstream pretraining examples by replaying examples that are forecasted to be forgotten, demonstrating the practical utility of forecasting example forgetting.