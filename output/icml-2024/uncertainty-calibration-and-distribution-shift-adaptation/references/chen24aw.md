---
title: "Split-Ensemble: Efficient OOD-aware Ensemble via Task and Model Splitting"
source: "https://proceedings.mlr.press/v235/chen24aw.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24aw/chen24aw.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['OOD-detection', 'ensemble', 'uncertainty-estimation', 'model-splitting']
venue: "ICML 2024"
tldr: "Proposes Split-Ensemble, an efficient OOD-aware method that splits tasks and models to improve uncertainty estimation without extra OOD data."
---

# Split-Ensemble: Efficient OOD-aware Ensemble via Task and Model Splitting

**Source**: [https://proceedings.mlr.press/v235/chen24aw.html](https://proceedings.mlr.press/v235/chen24aw.html)

**TLDR**: Proposes Split-Ensemble, an efficient OOD-aware method that splits tasks and models to improve uncertainty estimation without extra OOD data.

## Abstract

Uncertainty estimation is crucial for deep learning models to detect out-of-distribution (OOD) inputs. However, the naive deep learning classifiers produce uncalibrated uncertainty for OOD data. Improving the uncertainty estimation typically requires external data for OOD-aware training or considerable costs to build an ensemble. In this work, we improve on uncertainty estimation without extra OOD data or additional inference costs using an alternative Split-Ensemble method. Specifically, we propose a novel subtask-splitting ensemble training objective where a task is split into several complementary subtasks based on feature similarity. Each subtask considers part of the data as in distribution while all the rest as OOD data. Diverse submodels can therefore be trained on each subtask with OOD-aware objectives, learning generalizable uncertainty estimation. To avoid overheads, we enable low-level feature sharing among submodels, building a tree-like Split-Ensemble architecture via iterative splitting and pruning. Empirical study shows Split-Ensemble, without additional computational cost, improves accuracy over a single model by 0.8%, 1.8%, and 25.5% on CIFAR-10, CIFAR-100, and Tiny-ImageNet, respectively. OOD detection for the same backbone and in-distribution datasets surpasses a single model baseline by 2.2%, 8.1%, and 29.6% in mean AUROC, respectively.