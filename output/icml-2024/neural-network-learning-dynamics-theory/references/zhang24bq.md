---
title: "Exploring the Benefit of Activation Sparsity in Pre-training"
source: "https://proceedings.mlr.press/v235/zhang24bq.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24bq/zhang24bq.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'neural-network-learning-dynamics-theory']
tags: ['sparse-activation', 'pre-training', 'transformers', 'efficiency', 'representation-learning']
venue: "ICML 2024"
tldr: "Explores the benefits of activation sparsity during pre-training of Transformers, showing improvements in efficiency and performance."
---

# Exploring the Benefit of Activation Sparsity in Pre-training

**Source**: [https://proceedings.mlr.press/v235/zhang24bq.html](https://proceedings.mlr.press/v235/zhang24bq.html)

**TLDR**: Explores the benefits of activation sparsity during pre-training of Transformers, showing improvements in efficiency and performance.

## Abstract

Pre-trained Transformers inherently possess the characteristic of sparse activation, where only a small fraction of the neurons are activated for each token. While sparse activation has been explored through post-training methods, its potential in pre-training remains untapped. In this work, we first study how activation properties change during pre-training. Our examination reveals that Transformers exhibit sparse activation throughout the majority of the pre-training process while the activation correlation keeps evolving as training progresses. Leveraging this observation, we propose Switchable Sparse-Dense Learning (SSD). SSD adaptively switches between the Mixtures-of-Experts (MoE) based sparse training and the conventional dense training during the pre-training process, leveraging the efficiency of sparse training and avoiding the static activation correlation of sparse training. Compared to dense training, SSD achieves comparable performance with identical model size and reduces pre-training costs. Moreover, the models trained with SSD can be directly used as MoE models for sparse inference and achieve the same performance as dense models with up to $2\times$ faster inference speed. Codes are available at https://github.com/thunlp/moefication.