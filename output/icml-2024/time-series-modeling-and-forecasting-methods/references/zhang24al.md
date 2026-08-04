---
title: "UP2ME: Univariate Pre-training to Multivariate Fine-tuning as a General-purpose Framework for Multivariate Time Series Analysis"
source: "https://proceedings.mlr.press/v235/zhang24al.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24al/zhang24al.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'test-time-adaptation-methods-and-evaluation']
tags: ['time-series', 'self-supervised-pretraining', 'multivariate-forecasting']
venue: "ICML 2024"
tldr: "A general pre-training to fine-tuning framework for multivariate time series that uses univariate pre-training and multivariate adaptation."
---

# UP2ME: Univariate Pre-training to Multivariate Fine-tuning as a General-purpose Framework for Multivariate Time Series Analysis

**Source**: [https://proceedings.mlr.press/v235/zhang24al.html](https://proceedings.mlr.press/v235/zhang24al.html)

**TLDR**: A general pre-training to fine-tuning framework for multivariate time series that uses univariate pre-training and multivariate adaptation.

## Abstract

Despite the success of self-supervised pre-training in texts and images, applying it to multivariate time series (MTS) falls behind tailored methods for tasks like forecasting, imputation and anomaly detection. We propose a general-purpose framework, named UP2ME (Univariate Pre-training to Multivariate Fine-tuning). It conducts task-agnostic pre-training when downstream tasks are unspecified. Once the task and setting (e.g. forecasting length) are determined, it gives sensible solutions with frozen pre-trained parameters, which has not been achieved before. UP2ME is further refined by fine-tuning. A univariate-to-multivariate paradigm is devised to address the heterogeneity of temporal and cross-channel dependencies. In univariate pre-training, univariate instances with diverse lengths are generated for Masked AutoEncoder (MAE) pre-training, discarding cross-channel dependency. The pre-trained model handles downstream tasks by formulating them into specific mask-reconstruction problems. In multivariate fine-tuning, it constructs a dependency graph among channels using the pre-trained encoder to enhance cross-channel dependency capture. Experiments on eight real-world datasets show its SOTA performance in forecasting and imputation, approaching task-specific performance in anomaly detection. Our code is available at https://github.com/Thinklab-SJTU/UP2ME.