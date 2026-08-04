---
title: "Learning with Adaptive Resource Allocation"
source: "https://proceedings.mlr.press/v235/wang24cj.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24cj/wang24cj.pdf"
categories: ['data-selection-and-active-learning-methods']
tags: ['resource-allocation', 'active-learning', 'multi-task-learning']
venue: "ICML 2024"
tldr: "This paper studies machine learning under adaptive and limited resource allocation across multiple simultaneous learning tasks."
---

# Learning with Adaptive Resource Allocation

**Source**: [https://proceedings.mlr.press/v235/wang24cj.html](https://proceedings.mlr.press/v235/wang24cj.html)

**TLDR**: This paper studies machine learning under adaptive and limited resource allocation across multiple simultaneous learning tasks.

## Abstract

The study of machine learning under limited resources has gathered increasing attention, considering improving the learning efficiency and effectiveness with budgeted resources. However, previous efforts mainly focus on single learning task, and a common resource-limited scenario is less explored: to handle multiple time-constrained learning tasks concurrently with budgeted computational resources. In this paper, we point out that this is a very challenging task because it demands the learner to be concerned about not only the progress of the learning tasks but also the coordinative allocation of computational resources. We present the Learning with Adaptive Resource Allocation (LARA) approach, which comprises an efficient online estimator for learning progress prediction, an adaptive search method for computational resource allocation, and a balancing strategy for alleviating prediction-allocation compounding errors. Empirical studies validate the effectiveness of our proposed approach.