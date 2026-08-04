---
title: "Piecewise Constant and Linear Regression Trees: An Optimal Dynamic Programming Approach"
source: "https://proceedings.mlr.press/v235/van-den-bos24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/van-den-bos24a/van-den-bos24a.pdf"
categories: ['decision-tree-learning-algorithms-optimization', 'dynamic-algorithms-and-complexity-theory']
tags: ['regression-trees', 'dynamic-programming', 'optimal-decision-trees']
venue: "ICML 2024"
tldr: "Presents an optimal dynamic programming approach for computing piecewise constant and linear regression trees efficiently."
---

# Piecewise Constant and Linear Regression Trees: An Optimal Dynamic Programming Approach

**Source**: [https://proceedings.mlr.press/v235/van-den-bos24a.html](https://proceedings.mlr.press/v235/van-den-bos24a.html)

**TLDR**: Presents an optimal dynamic programming approach for computing piecewise constant and linear regression trees efficiently.

## Abstract

Regression trees are a human-comprehensible machine-learning model that can represent complex relationships. They are typically trained using greedy heuristics because computing optimal regression trees is NP-hard. Contrary to this standard practice, we consider optimal methods and improve the scalability of optimal methods by developing three new dynamic programming approaches. First, we improve the performance of a piecewise constant regression tree method using a special algorithm for trees of depth two. Second, we provide the first optimal dynamic programming method for piecewise multiple linear regression. Third, we develop the first optimal method for piecewise simple linear regression, for which we also provide a special algorithm for trees of depth two. The experimental results show that our methods improve scalability by one or more orders of magnitude over the state-of-the-art optimal methods while performing similarly or better in out-of-sample performance.