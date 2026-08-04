---
title: "A General Online Algorithm for Optimizing Complex Performance Metrics"
source: "https://proceedings.mlr.press/v235/kotlowski24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kotlowski24a/kotlowski24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'online-learning-matching-market-algorithms']
tags: ['online-learning', 'performance-metrics', 'confusion-matrix', 'non-decomposable', 'sequential-optimization']
venue: "ICML 2024"
tldr: "A general online algorithm for sequentially optimizing complex non-decomposable classifier performance metrics defined over confusion matrices."
---

# A General Online Algorithm for Optimizing Complex Performance Metrics

**Source**: [https://proceedings.mlr.press/v235/kotlowski24a.html](https://proceedings.mlr.press/v235/kotlowski24a.html)

**TLDR**: A general online algorithm for sequentially optimizing complex non-decomposable classifier performance metrics defined over confusion matrices.

## Abstract

We consider sequential maximization of performance metrics that are general functions of a confusion matrix of a classifier (such as precision, F-measure, or G-mean). Such metrics are, in general, non-decomposable over individual instances, making their optimization very challenging. While they have been extensively studied under different frameworks in the batch setting, their analysis in the online learning regime is very limited, with only a few distinguished exceptions. In this paper, we introduce and analyze a general online algorithm that can be used in a straightforward way with a variety of complex performance metrics in binary, multi-class, and multi-label classification problems. The algorithm’s update and prediction rules are appealingly simple and computationally efficient without the need to store any past data. We show the algorithm attains $\mathcal{O}(\frac{\ln n}{n})$ regret for concave and smooth metrics and verify the efficiency of the proposed algorithm in empirical studies.