---
title: "Generalization Analysis for Multi-Label Learning"
source: "https://proceedings.mlr.press/v235/zhang24by.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24by/zhang24by.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'neural-network-learning-dynamics-theory']
tags: ['multi-label-learning', 'generalization-bounds', 'evaluation-metrics']
venue: "ICML 2024"
tldr: "Provides theoretical generalization analysis for multi-label learning across multiple evaluation metrics."
---

# Generalization Analysis for Multi-Label Learning

**Source**: [https://proceedings.mlr.press/v235/zhang24by.html](https://proceedings.mlr.press/v235/zhang24by.html)

**TLDR**: Provides theoretical generalization analysis for multi-label learning across multiple evaluation metrics.

## Abstract

Despite great advances in algorithms for multi-label learning, research on the theoretical analysis of generalization is still in the early stage. Some recent theoretical results has investigated the generalization performance of multi-label learning under several evaluation metrics, however, how to reduce the dependency on the number of labels, explicitly introduce label correlations, and quantitatively analyze the impact of various inductive biases in the generalization analysis of multi-label learning is still a crucial and open problem. In an attempt to make up for the gap in the generalization theory of multi-label learning, we develop several novel vector-contraction inequalities, which exploit the Lipschitz continuity of loss functions, and derive generalization bounds with a weaker dependency on the number of labels than the state of the art in the case of decoupling the relationship among different components, which serves as theoretical guarantees for the generalization of multi-label learning. In addition, we derive the generalization bound for Macro-Averaged AUC and analyze its relationship with class-imbalance. The mild bounds without strong assumptions explain the good generalization ability of multi-label learning with first-order label correlations and high-order label correlations induced by norm regularizers.