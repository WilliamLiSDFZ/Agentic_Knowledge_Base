---
title: "CICLe: Conformal In-Context Learning for Largescale Multi-Class Food Risk Classification"
source: "https://aclanthology.org/2024.findings-acl.459/"
categories: ['nlp-text-classification-applied-tasks', 'label-noise-robust-annotation-learning']
tags: ['food-risk-classification', 'conformal-prediction', 'in-context-learning']
venue: "ACL 2024"
tldr: "CICLe applies conformal in-context learning for reliable large-scale multi-class food risk classification from web texts."
---

# CICLe: Conformal In-Context Learning for Largescale Multi-Class Food Risk Classification

**Source**: [https://aclanthology.org/2024.findings-acl.459/](https://aclanthology.org/2024.findings-acl.459/)

**TLDR**: CICLe applies conformal in-context learning for reliable large-scale multi-class food risk classification from web texts.

## Abstract

AbstractContaminated or adulterated food poses a substantial risk to human health. Given sets of labeled web texts for training, Machine Learning and Natural Language Processing can be applied to automatically detect such risks. We publish a dataset of 7,546 short texts describing public food recall announcements. Each text is manually labeled, on two granularity levels (coarse and fine), for food products and hazards that the recall corresponds to. We describe the dataset and benchmark naive, traditional, and Transformer models. Based on our analysis, Logistic Regression based on a TF-IDF representation outperforms RoBERTa and XLM-R on classes with low support. Finally, we discuss different prompting strategies and present an LLM-in-the-loop framework, based on Conformal Prediction, which boosts the performance of the base classifier while reducing energy consumption compared to normal prompting.