---
title: "Restoring balance: principled under/oversampling of data for optimal classification"
source: "https://proceedings.mlr.press/v235/loffredo24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/loffredo24a/loffredo24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['class-imbalance', 'oversampling', 'undersampling', 'classification', 'optimal-resampling']
venue: "ICML 2024"
tldr: "Provides principled theoretical analysis of under/oversampling strategies to achieve optimal classification under class imbalance."
---

# Restoring balance: principled under/oversampling of data for optimal classification

**Source**: [https://proceedings.mlr.press/v235/loffredo24a.html](https://proceedings.mlr.press/v235/loffredo24a.html)

**TLDR**: Provides principled theoretical analysis of under/oversampling strategies to achieve optimal classification under class imbalance.

## Abstract

Class imbalance in real-world data poses a common bottleneck for machine learning tasks, since achieving good generalization on under-represented examples is often challenging. Mitigation strategies, such as under or oversampling the data depending on their abundances, are routinely proposed and tested empirically, but how they should adapt to the data statistics remains poorly understood. In this work, we determine exact analytical expressions of the generalization curves in the high-dimensional regime for linear classifiers (Support Vector Machines). We also provide a sharp prediction of the effects of under/oversampling strategies depending on class imbalance, first and second moments of the data, and the metrics of performance considered. We show that mixed strategies involving under and oversampling of data lead to performance improvement. Through numerical experiments, we show the relevance of our theoretical predictions on real datasets, on deeper architectures and with sampling strategies based on unsupervised probabilistic models.