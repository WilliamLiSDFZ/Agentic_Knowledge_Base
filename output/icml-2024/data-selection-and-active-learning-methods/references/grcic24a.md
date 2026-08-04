---
title: "Fine-grained Classes and How to Find Them"
source: "https://proceedings.mlr.press/v235/grcic24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/grcic24a/grcic24a.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'data-selection-and-active-learning-methods']
tags: ['fine-grained-classification', 'coarse-labels', 'unsupervised-discovery']
venue: "ICML 2024"
tldr: "This paper proposes a method to leverage coarse-grained labels for unsupervised discovery of fine-grained class structure."
---

# Fine-grained Classes and How to Find Them

**Source**: [https://proceedings.mlr.press/v235/grcic24a.html](https://proceedings.mlr.press/v235/grcic24a.html)

**TLDR**: This paper proposes a method to leverage coarse-grained labels for unsupervised discovery of fine-grained class structure.

## Abstract

In many practical applications, coarse-grained labels are readily available compared to fine-grained labels that reflect subtle differences between classes. However, existing methods cannot leverage coarse labels to infer fine-grained labels in an unsupervised manner. To bridge this gap, we propose FALCON, a method that discovers fine-grained classes from coarsely labeled data without any supervision at the fine-grained level. FALCON simultaneously infers unknown fine-grained classes and underlying relationships between coarse and fine-grained classes. Moreover, FALCON is a modular method that can effectively learn from multiple datasets labeled with different strategies. We evaluate FALCON on eight image classification tasks and a single-cell classification task. FALCON outperforms baselines by a large margin, achieving 22% improvement over the best baseline on the tieredImageNet dataset with over 600 fine-grained classes.