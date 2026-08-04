---
title: "Interplay of ROC and Precision-Recall AUCs: Theoretical Limits and Practical Implications in Binary Classification"
source: "https://proceedings.mlr.press/v235/mihelich24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mihelich24a/mihelich24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'fairness-aware-algorithmic-decision-making']
tags: ['ROC-AUC', 'precision-recall', 'binary-classification']
venue: "ICML 2024"
tldr: "Derives theoretical bounds on the relationship between ROC AUC and Precision-Recall AUC with practical implications for binary classification evaluation."
---

# Interplay of ROC and Precision-Recall AUCs: Theoretical Limits and Practical Implications in Binary Classification

**Source**: [https://proceedings.mlr.press/v235/mihelich24a.html](https://proceedings.mlr.press/v235/mihelich24a.html)

**TLDR**: Derives theoretical bounds on the relationship between ROC AUC and Precision-Recall AUC with practical implications for binary classification evaluation.

## Abstract

In this paper, we present two key theorems that should have significant implications for machine learning practitioners working with binary classification models. The first theorem provides a formula to calculate the maximum and minimum Precision-Recall AUC ($AUC_{PR}$) for a fixed Receiver Operating Characteristic AUC ($AUC_{ROC}$), demonstrating the variability of $AUC_{PR}$ even with a high $AUC_{ROC}$. This is particularly relevant for imbalanced datasets, where a good $AUC_{ROC}$ does not necessarily imply a high $AUC_{PR}$. The second theorem inversely establishes the bounds of $AUC_{ROC}$ given a fixed $AUC_{PR}$. Our findings highlight that in certain situations, especially for imbalanced datasets, it is more informative to prioritize $AUC_{PR}$ over $AUC_{ROC}$. Additionally, we introduce a method to determine when a higher $AUC_{ROC}$ in one model implies a higher $AUC_{PR}$ in another and vice versa, streamlining the model evaluation process.