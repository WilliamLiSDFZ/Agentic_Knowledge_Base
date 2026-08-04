---
title: "Balancing Feature Similarity and Label Variability for Optimal Size-Aware One-shot Subset Selection"
source: "https://proceedings.mlr.press/v235/acharya24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/acharya24a/acharya24a.pdf"
categories: ['data-selection-and-active-learning-methods']
tags: ['coreset-selection', 'one-shot', 'data-efficiency', 'subset-selection']
venue: "ICML 2024"
tldr: "Proposes a one-shot subset selection method balancing feature similarity and label variability for efficient deep learning training."
---

# Balancing Feature Similarity and Label Variability for Optimal Size-Aware One-shot Subset Selection

**Source**: [https://proceedings.mlr.press/v235/acharya24a.html](https://proceedings.mlr.press/v235/acharya24a.html)

**TLDR**: Proposes a one-shot subset selection method balancing feature similarity and label variability for efficient deep learning training.

## Abstract

Subset or core-set selection offers a data-efficient way for training deep learning models. One-shot subset selection poses additional challenges as subset selection is only performed once and full set data become unavailable after the selection. However, most existing methods tend to choose either diverse or difficult data samples, which fail to faithfully represent the joint data distribution that is comprised of both feature and label information. The selection is also performed independently from the subset size, which plays an essential role in choosing what types of samples. To address this critical gap, we propose to conduct Feature similarity and Label variability Balanced One-shot Subset Selection (BOSS), aiming to construct an optimal size-aware subset for data-efficient deep learning. We show that a novel balanced core-set loss bound theoretically justifies the need to simultaneously consider both diversity and difficulty to form an optimal subset. It also reveals how the subset size influences the bound. We further connect the inaccessible bound to a practical surrogate target which is tailored to subset sizes and varying levels of overall difficulty. We design a novel Beta-scoring importance function to delicately control the optimal balance of diversity and difficulty. Comprehensive experiments conducted on both synthetic and real data justify the important theoretical properties and demonstrate the superior performance of BOSS as compared with the competitive baselines.