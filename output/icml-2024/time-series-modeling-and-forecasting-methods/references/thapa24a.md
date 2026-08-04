---
title: "SleepFM: Multi-modal Representation Learning for Sleep Across Brain Activity, ECG and Respiratory Signals"
source: "https://proceedings.mlr.press/v235/thapa24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/thapa24a/thapa24a.pdf"
categories: ['time-series-modeling-and-forecasting-methods', 'multi-region-brain-connectivity-modeling']
tags: ['sleep-analysis', 'multimodal-learning', 'polysomnography']
venue: "ICML 2024"
tldr: "SleepFM is a multi-modal foundation model trained on over 100,000 hours of sleep recordings spanning brain, cardiac, and respiratory signals for sleep stage and event classification."
---

# SleepFM: Multi-modal Representation Learning for Sleep Across Brain Activity, ECG and Respiratory Signals

**Source**: [https://proceedings.mlr.press/v235/thapa24a.html](https://proceedings.mlr.press/v235/thapa24a.html)

**TLDR**: SleepFM is a multi-modal foundation model trained on over 100,000 hours of sleep recordings spanning brain, cardiac, and respiratory signals for sleep stage and event classification.

## Abstract

Sleep is a complex physiological process evaluated through various modalities recording electrical brain, cardiac, and respiratory activities. We curate a large polysomnography dataset from over 14,000 participants comprising over 100,000 hours of multi-modal sleep recordings. Leveraging this extensive dataset, we developed SleepFM, the first multi-modal foundation model for sleep analysis. We show that a novel leave-one-out approach for contrastive learning significantly improves downstream task performance compared to representations from standard pairwise contrastive learning. A logistic regression model trained on SleepFM’s learned embeddings outperforms an end-to-end trained convolutional neural network (CNN) on sleep stage classification (macro AUROC 0.88 vs 0.72 and macro AUPRC 0.72 vs 0.48) and sleep disordered breathing detection (AUROC 0.85 vs 0.69 and AUPRC 0.77 vs 0.61). Notably, the learned embeddings achieve 48% top-1 average accuracy in retrieving modality clip pairs from 90,000 candidates. This work demonstrates the value of holistic multi-modal sleep modeling to fully capture the richness of sleep recordings. SleepFM is open source and available at https://anonymous.4open.science/r/sleepfm.