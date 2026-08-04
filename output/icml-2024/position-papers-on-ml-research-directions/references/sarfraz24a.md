---
title: "Position: Quo Vadis, Unsupervised Time Series Anomaly Detection?"
source: "https://proceedings.mlr.press/v235/sarfraz24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sarfraz24a/sarfraz24a.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'position-papers-on-ml-research-directions']
tags: ['anomaly-detection', 'time-series', 'evaluation-metrics', 'benchmarking', 'deep-learning']
venue: "ICML 2024"
tldr: "A position paper arguing that unsupervised time series anomaly detection research is undermined by flawed evaluation metrics, inconsistent benchmarks, and unjustified model design choices."
---

# Position: Quo Vadis, Unsupervised Time Series Anomaly Detection?

**Source**: [https://proceedings.mlr.press/v235/sarfraz24a.html](https://proceedings.mlr.press/v235/sarfraz24a.html)

**TLDR**: A position paper arguing that unsupervised time series anomaly detection research is undermined by flawed evaluation metrics, inconsistent benchmarks, and unjustified model design choices.

## Abstract

The current state of machine learning scholarship in Timeseries Anomaly Detection (TAD) is plagued by the persistent use of flawed evaluation metrics, inconsistent benchmarking practices, and a lack of proper justification for the choices made in novel deep learning-based model designs. Our paper presents a critical analysis of the status quo in TAD, revealing the misleading track of current research and highlighting problematic methods, and evaluation practices. Our position advocates for a shift in focus from solely pursuing novel model designs to improving benchmarking practices, creating non-trivial datasets, and critically evaluating the utility of complex methods against simpler baselines. Our findings demonstrate the need for rigorous evaluation protocols, the creation of simple baselines, and the revelation that state-of-the-art deep anomaly detection models effectively learn linear mappings. These findings suggest the need for more exploration and development of simple and interpretable TAD methods. The increment of model complexity in the state-of-the-art deep-learning based models unfortunately offers very little improvement. We offer insights and suggestions for the field to move forward.