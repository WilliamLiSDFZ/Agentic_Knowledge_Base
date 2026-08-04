---
title: "Interpretable Deep Clustering for Tabular Data"
source: "https://proceedings.mlr.press/v235/svirsky24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/svirsky24a/svirsky24a.pdf"
categories: ['clustering-methods-and-multi-view-learning']
tags: ['deep-clustering', 'interpretability', 'tabular-data']
venue: "ICML 2024"
tldr: "An interpretable deep clustering method for tabular data provides reliable and understandable cluster assignments for downstream analysis."
---

# Interpretable Deep Clustering for Tabular Data

**Source**: [https://proceedings.mlr.press/v235/svirsky24a.html](https://proceedings.mlr.press/v235/svirsky24a.html)

**TLDR**: An interpretable deep clustering method for tabular data provides reliable and understandable cluster assignments for downstream analysis.

## Abstract

Clustering is a fundamental learning task widely used as a first step in data analysis. For example, biologists use cluster assignments to analyze genome sequences, medical records, or images. Since downstream analysis is typically performed at the cluster level, practitioners seek reliable and interpretable clustering models. We propose a new deep-learning framework for general domain tabular data that predicts interpretable cluster assignments at the instance and cluster levels. First, we present a self-supervised procedure to identify the subset of the most informative features from each data point. Then, we design a model that predicts cluster assignments and a gate matrix that provides cluster-level feature selection. Overall, our model provides cluster assignments with an indication of the driving feature for each sample and each cluster. We show that the proposed method can reliably predict cluster assignments in biological, text, image, and physics tabular datasets. Furthermore, using previously proposed metrics, we verify that our model leads to interpretable results at a sample and cluster level. Our code is available on https://github.com/jsvir/idc.