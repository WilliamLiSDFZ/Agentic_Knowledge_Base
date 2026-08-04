---
title: "Don’t Label Twice: Quantity Beats Quality when Comparing Binary Classifiers on a Budget"
source: "https://proceedings.mlr.press/v235/dorner24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dorner24a/dorner24a.pdf"
categories: ['data-selection-and-active-learning-methods', 'learning-with-imperfect-data-and-bias']
tags: ['noisy-labels', 'binary-classification', 'budget-allocation', 'majority-vote']
venue: "ICML 2024"
tldr: "This paper proves that spreading a labeling budget over more data points with noisy labels outperforms aggregating multiple labels per point when comparing two binary classifiers."
---

# Don’t Label Twice: Quantity Beats Quality when Comparing Binary Classifiers on a Budget

**Source**: [https://proceedings.mlr.press/v235/dorner24a.html](https://proceedings.mlr.press/v235/dorner24a.html)

**TLDR**: This paper proves that spreading a labeling budget over more data points with noisy labels outperforms aggregating multiple labels per point when comparing two binary classifiers.

## Abstract

We study how to best spend a budget of noisy labels to compare the accuracy of two binary classifiers. It’s common practice to collect and aggregate multiple noisy labels for a given data point into a less noisy label via a majority vote. We prove a theorem that runs counter to conventional wisdom. If the goal is to identify the better of two classifiers, we show it’s best to spend the budget on collecting a single label for more samples. Our result follows from a non-trivial application of Cramér’s theorem, a staple in the theory of large deviations. We discuss the implications of our work for the design of machine learning benchmarks, where they overturn some time-honored recommendations. In addition, our results provide sample size bounds superior to what follows from Hoeffding’s bound.