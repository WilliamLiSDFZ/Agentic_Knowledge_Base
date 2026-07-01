---
title: "Improving Subgroup Robustness via Data Selection"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/abbbb25cddb2c2cd08714e6bfa2f0634-Abstract-Conference.html"
categories: ['fairness-aware-machine-learning-methods', 'machine-learning-theory-and-evaluation-methods']
tags: ['subgroup-robustness', 'data-selection', 'dataset-balancing']
venue: "NeurIPS 2024"
tldr: "Introduces a data selection method to improve subgroup robustness in ML models without requiring full group annotations or discarding large data portions."
---

# Improving Subgroup Robustness via Data Selection

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/abbbb25cddb2c2cd08714e6bfa2f0634-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/abbbb25cddb2c2cd08714e6bfa2f0634-Abstract-Conference.html)

**TLDR**: Introduces a data selection method to improve subgroup robustness in ML models without requiring full group annotations or discarding large data portions.

## Abstract

Machine learning models can often fail on subgroups that are underrepresentedduring training. While dataset balancing can improve performance onunderperforming groups, it requires access to training group annotations and canend up removing large portions of the dataset. In this paper, we introduceData Debiasing with Datamodels (D3M), a debiasing approachwhich isolates and removes specific training examples that drive the model'sfailures on minority groups. Our approach enables us to efficiently traindebiased classifiers while removing only a small number of examples, and doesnot require training group annotations or additional hyperparameter tuning.