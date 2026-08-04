---
title: "MD tree: a model-diagnostic tree grown on loss landscape"
source: "https://proceedings.mlr.press/v235/zhou24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24d/zhou24d.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'neural-network-learning-dynamics-theory']
tags: ['model-diagnosis', 'loss-landscape', 'failure-mode-classification']
venue: "ICML 2024"
tldr: "Proposes a model-diagnostic tree framework that classifies sources of neural network failure by analyzing loss landscape characteristics without prior knowledge of failure modes."
---

# MD tree: a model-diagnostic tree grown on loss landscape

**Source**: [https://proceedings.mlr.press/v235/zhou24d.html](https://proceedings.mlr.press/v235/zhou24d.html)

**TLDR**: Proposes a model-diagnostic tree framework that classifies sources of neural network failure by analyzing loss landscape characteristics without prior knowledge of failure modes.

## Abstract

This paper considers ”model diagnosis”, which we formulate as a classification problem. Given a pre-trained neural network (NN), the goal is to predict the source of failure from a set of failure modes (such as a wrong hyperparameter, inadequate model size, and insufficient data) without knowing the training configuration of the pre-trained NN. The conventional diagnosis approach uses training and validation errors to determine whether the model is underfitting or overfitting. However, we show that rich information about NN performance is encoded in the optimization loss landscape, which provides more actionable insights than validation-based measurements. Therefore, we propose a diagnosis method called MD tree based on loss landscape metrics and experimentally demonstrate its advantage over classical validation-based approaches. We verify the effectiveness of MD tree in multiple practical scenarios: (1) use several models trained on one dataset to diagnose a model trained on another dataset, essentially a few-shot dataset transfer problem; (2) use small models (or models trained with small data) to diagnose big models (or models trained with big data), essentially a scale transfer problem. In a dataset transfer task, MD tree achieves an accuracy of 87.7%, outperforming validation-based approaches by 14.88%. Our code is available at https://github.com/YefanZhou/ModelDiagnosis.