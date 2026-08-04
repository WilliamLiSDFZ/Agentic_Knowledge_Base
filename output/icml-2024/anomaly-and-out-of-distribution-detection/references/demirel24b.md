---
title: "An Unsupervised Approach for Periodic Source Detection in Time Series"
source: "https://proceedings.mlr.press/v235/demirel24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/demirel24b/demirel24b.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'anomaly-and-out-of-distribution-detection']
tags: ['periodicity-detection', 'time-series', 'unsupervised-learning', 'anomaly-detection', 'signal-processing']
venue: "ICML 2024"
tldr: "Presents an unsupervised method for detecting periodic patterns in noisy time series without requiring labels or clean reference signals."
---

# An Unsupervised Approach for Periodic Source Detection in Time Series

**Source**: [https://proceedings.mlr.press/v235/demirel24b.html](https://proceedings.mlr.press/v235/demirel24b.html)

**TLDR**: Presents an unsupervised method for detecting periodic patterns in noisy time series without requiring labels or clean reference signals.

## Abstract

Detection of periodic patterns of interest within noisy time series data plays a critical role in various tasks, spanning from health monitoring to behavior analysis. Existing learning techniques often rely on labels or clean versions of signals for detecting the periodicity, and those employing self-supervised methods are required to apply proper augmentations, which is already challenging for time series and can result in collapse—all representations collapse to a single point due to strong augmentation. In this work, we propose a novel method to detect the periodicity in time series without the need for any labels or requiring tailored positive or negative data generation mechanisms. We mitigate the collapse issue by ensuring the learned representations retain information from the original samples without imposing any variance constraints on the batch. Our experiments in three time-series tasks against state-of-the-art learning methods show that the proposed approach consistently outperforms prior works, achieving performance improvements of more than 45–50%, showing its effectiveness.