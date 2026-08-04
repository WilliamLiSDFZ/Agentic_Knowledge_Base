---
title: "ODIM: Outlier Detection via Likelihood of Under-Fitted Generative Models"
source: "https://proceedings.mlr.press/v235/kim24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kim24h/kim24h.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'generative-models-and-variational-inference']
tags: ['outlier-detection', 'under-fitted-generative-models', 'likelihood-based']
venue: "ICML 2024"
tldr: "Proposes ODIM, an unsupervised outlier detection method using the likelihood of intentionally under-fitted generative models to distinguish inliers from outliers."
---

# ODIM: Outlier Detection via Likelihood of Under-Fitted Generative Models

**Source**: [https://proceedings.mlr.press/v235/kim24h.html](https://proceedings.mlr.press/v235/kim24h.html)

**TLDR**: Proposes ODIM, an unsupervised outlier detection method using the likelihood of intentionally under-fitted generative models to distinguish inliers from outliers.

## Abstract

The unsupervised outlier detection (UOD) problem refers to a task to identify inliers given training data which contain outliers as well as inliers, without any labeled information about inliers and outliers. It has been widely recognized that using fully-trained likelihood-based deep generative models (DGMs) often results in poor performance in distinguishing inliers from outliers. In this study, we claim that the likelihood itself could serve as powerful evidence for identifying inliers in UOD tasks, provided that DGMs are carefully under-fitted. Our approach begins with a novel observation called the inlier-memorization (IM) effect–when training a deep generative model with data including outliers, the model initially memorizes inliers before outliers. Based on this finding, we develop a new method called the outlier detection via the IM effect (ODIM). Remarkably, the ODIM requires only a few updates, making it computationally efficient–at least tens of times faster than other deep-learning-based algorithms. Also, the ODIM filters out outliers excellently, regardless of the data type, including tabular, image, and text data. To validate the superiority and efficiency of our method, we provide extensive empirical analyses on close to 60 datasets.