---
title: "Learning with Complementary Labels Revisited: The Selected-Completely-at-Random Setting Is More Practical"
source: "https://proceedings.mlr.press/v235/wang24ac.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24ac/wang24ac.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'data-selection-and-active-learning-methods']
tags: ['complementary-label-learning', 'weakly-supervised', 'label-noise', 'distribution-assumptions']
venue: "ICML 2024"
tldr: "A more practical selected-completely-at-random assumption is proposed for complementary-label learning, relaxing the uniform distribution requirement."
---

# Learning with Complementary Labels Revisited: The Selected-Completely-at-Random Setting Is More Practical

**Source**: [https://proceedings.mlr.press/v235/wang24ac.html](https://proceedings.mlr.press/v235/wang24ac.html)

**TLDR**: A more practical selected-completely-at-random assumption is proposed for complementary-label learning, relaxing the uniform distribution requirement.

## Abstract

Complementary-label learning is a weakly supervised learning problem in which each training example is associated with one or multiple complementary labels indicating the classes to which it does not belong. Existing consistent approaches have relied on the uniform distribution assumption to model the generation of complementary labels, or on an ordinary-label training set to estimate the transition matrix in non-uniform cases. However, either condition may not be satisfied in real-world scenarios. In this paper, we propose a novel consistent approach that does not rely on these conditions. Inspired by the positive-unlabeled (PU) learning literature, we propose an unbiased risk estimator based on the Selected-Completely-at-Random assumption for complementary-label learning. We then introduce a risk-correction approach to address overfitting problems. Furthermore, we find that complementary-label learning can be expressed as a set of negative-unlabeled binary classification problems when using the one-versus-rest strategy. Extensive experimental results on both synthetic and real-world benchmark datasets validate the superiority of our proposed approach over state-of-the-art methods.