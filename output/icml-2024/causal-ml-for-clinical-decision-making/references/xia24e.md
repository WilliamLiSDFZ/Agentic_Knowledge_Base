---
title: "Contrastive Learning for Clinical Outcome Prediction with Partial Data Sources"
source: "https://proceedings.mlr.press/v235/xia24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xia24e/xia24e.pdf"
categories: ['causal-ml-for-clinical-decision-making', 'learning-with-imperfect-data-and-bias']
tags: ['contrastive-learning', 'EHR', 'missing-data']
venue: "ICML 2024"
tldr: "A contrastive learning framework for clinical outcome prediction that handles partial data sources in longitudinal electronic health records."
---

# Contrastive Learning for Clinical Outcome Prediction with Partial Data Sources

**Source**: [https://proceedings.mlr.press/v235/xia24e.html](https://proceedings.mlr.press/v235/xia24e.html)

**TLDR**: A contrastive learning framework for clinical outcome prediction that handles partial data sources in longitudinal electronic health records.

## Abstract

The use of machine learning models to predict clinical outcomes from (longitudinal) electronic health record (EHR) data is becoming increasingly popular due to advances in deep architectures, representation learning, and the growing availability of large EHR datasets. Existing models generally assume access to the same data sources during both training and inference stages. However, this assumption is often challenged by the fact that real-world clinical datasets originate from various data sources (with distinct sets of covariates), which though can be available for training (in a research or retrospective setting), are more realistically only partially available (a subset of such sets) for inference when deployed. So motivated, we introduce Contrastive Learning for clinical Outcome Prediction with Partial data Sources (CLOPPS), that trains encoders to capture information across different data sources and then leverages them to build classifiers restricting access to a single data source. This approach can be used with existing cross-sectional or longitudinal outcome classification models. We present experiments on two real-world datasets demonstrating that CLOPPS consistently outperforms strong baselines in several practical scenarios.