---
title: "Vector Quantization Pretraining for EEG Time Series with Random Projection and Phase Alignment"
source: "https://proceedings.mlr.press/v235/gui24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gui24a/gui24a.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['EEG', 'self-supervised-learning', 'vector-quantization', 'masked-modeling', 'random-projection']
venue: "ICML 2024"
tldr: "A BERT-style self-supervised model using vector quantization and phase alignment for EEG time-series analysis."
---

# Vector Quantization Pretraining for EEG Time Series with Random Projection and Phase Alignment

**Source**: [https://proceedings.mlr.press/v235/gui24a.html](https://proceedings.mlr.press/v235/gui24a.html)

**TLDR**: A BERT-style self-supervised model using vector quantization and phase alignment for EEG time-series analysis.

## Abstract

In this paper, we propose a BERT-style self-supervised learning model, VQ-MTM (Vector Quantization Masked Time-Series Modeling), for the EEG time series data analysis. At its core, VQ-MTM comprises a theoretically grounded random-projection quantization module and a phase-aligning module guided by the Time-Phase-Shift Equivariance of Fourier Transform, the two modules can generate well-defined semantic units (akin to words in natural language) for the corrupted and periodic time series, thus offering robust and consistent learning signals for the EEG self-supervised learning. VQ-MTM also owns low model complexity and can easily adapt to large-scale datasets. We conduct experiments on five real-world datasets including two large-scale datasets to verify the efficacy of our proposed model, the experiment results show that VQ-MTM is able to consistently surpass the existing methods by large margins on both seizure detection and classification tasks. Our code is available at https://github.com/HaokunGUI/VQ_MTM.