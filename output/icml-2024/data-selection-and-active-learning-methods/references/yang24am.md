---
title: "What is Dataset Distillation Learning?"
source: "https://proceedings.mlr.press/v235/yang24am.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24am/yang24am.pdf"
categories: ['data-selection-and-active-learning-methods']
tags: ['dataset-distillation', 'synthetic-data', 'knowledge-compression', 'representation-learning']
venue: "ICML 2024"
tldr: "An analysis of what dataset distillation actually learns and encodes from the original dataset is presented."
---

# What is Dataset Distillation Learning?

**Source**: [https://proceedings.mlr.press/v235/yang24am.html](https://proceedings.mlr.press/v235/yang24am.html)

**TLDR**: An analysis of what dataset distillation actually learns and encodes from the original dataset is presented.

## Abstract

Dataset distillation has emerged as a strategy to overcome the hurdles associated with large datasets by learning a compact set of synthetic data that retains essential information from the original dataset. While distilled data can be used to train high performing models, little is understood about how the information is stored. In this study, we posit and answer three questions about the behavior, representativeness, and point-wise information content of distilled data. We reveal distilled data cannot serve as a substitute for real data during training outside the standard evaluation setting for dataset distillation. Additionally, the distillation process retains high task performance by compressing information related to the early training dynamics of real models. Finally, we provide an framework for interpreting distilled data and reveal that individual distilled data points contain meaningful semantic information. This investigation sheds light on the intricate nature of distilled data, providing a better understanding on how they can be effectively utilized.