---
title: "Beyond the ROC Curve: Classification Trees Using Cost-Optimal Curves, with Application to Imbalanced Datasets"
source: "https://proceedings.mlr.press/v235/gabidolla24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gabidolla24a/gabidolla24a.pdf"
categories: ['decision-tree-learning-algorithms-optimization', 'fairness-aware-algorithmic-decision-making']
tags: ['classification-trees', 'imbalanced-datasets', 'cost-sensitive-learning', 'oblique-trees']
venue: "ICML 2024"
tldr: "This paper proposes cost-optimal curves beyond ROC analysis for building classification trees suited to imbalanced and cost-asymmetric datasets."
---

# Beyond the ROC Curve: Classification Trees Using Cost-Optimal Curves, with Application to Imbalanced Datasets

**Source**: [https://proceedings.mlr.press/v235/gabidolla24a.html](https://proceedings.mlr.press/v235/gabidolla24a.html)

**TLDR**: This paper proposes cost-optimal curves beyond ROC analysis for building classification trees suited to imbalanced and cost-asymmetric datasets.

## Abstract

Important applications such as fraud or spam detection or churn prediction involve binary classification problems where the datasets are imbalanced and the cost of false positives greatly differs from the cost of false negatives. We focus on classification trees, in particular oblique trees, which subsume both the traditional axis-aligned trees and logistic regression, but are more accurate than both while providing interpretable models. Rather than using ROC curves, we advocate a loss based on minimizing the false negatives subject to a maximum false positive rate, which we prove to be equivalent to minimizing a weighted 0/1 loss. This yields a curve of classifiers that provably dominates the ROC curve, but is hard to optimize due to the 0/1 loss. We give the first algorithm that can iteratively update the tree parameters globally so that the weighted 0/1 loss decreases monotonically. Experiments on various datasets with class imbalance or class costs show this indeed dominates ROC-based classifiers and significantly improves over previous approaches to learn trees based on weighted purity criteria or over- or undersampling.