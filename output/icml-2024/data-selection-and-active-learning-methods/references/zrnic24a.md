---
title: "Active Statistical Inference"
source: "https://proceedings.mlr.press/v235/zrnic24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zrnic24a/zrnic24a.pdf"
categories: ['data-selection-and-active-learning-methods', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['active-inference', 'statistical-inference', 'active-learning', 'machine-learning-assisted', 'data-collection']
venue: "ICML 2024"
tldr: "Active inference combines active learning with statistical inference to optimally allocate a labeling budget for more efficient and accurate downstream inference."
---

# Active Statistical Inference

**Source**: [https://proceedings.mlr.press/v235/zrnic24a.html](https://proceedings.mlr.press/v235/zrnic24a.html)

**TLDR**: Active inference combines active learning with statistical inference to optimally allocate a labeling budget for more efficient and accurate downstream inference.

## Abstract

Inspired by the concept of active learning, we propose active inference—a methodology for statistical inference with machine-learning-assisted data collection. Assuming a budget on the number of labels that can be collected, the methodology uses a machine learning model to identify which data points would be most beneficial to label, thus effectively utilizing the budget. It operates on a simple yet powerful intuition: prioritize the collection of labels for data points where the model exhibits uncertainty, and rely on the model’s predictions where it is confident. Active inference constructs valid confidence intervals and hypothesis tests while leveraging any black-box machine learning model and handling any data distribution. The key point is that it achieves the same level of accuracy with far fewer samples than existing baselines relying on non-adaptively-collected data. This means that for the same number of collected samples, active inference enables smaller confidence intervals and more powerful tests. We evaluate active inference on datasets from public opinion research, census analysis, and proteomics.