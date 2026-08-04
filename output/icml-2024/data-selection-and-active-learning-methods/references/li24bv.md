---
title: "Towards Realistic Model Selection for Semi-supervised Learning"
source: "https://proceedings.mlr.press/v235/li24bv.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bv/li24bv.pdf"
categories: ['data-selection-and-active-learning-methods', 'learning-with-imperfect-data-and-bias']
tags: ['semi-supervised-learning', 'model-selection', 'validation']
venue: "ICML 2024"
tldr: "Proposes a realistic model selection strategy for semi-supervised learning that handles the scarcity of labeled validation data."
---

# Towards Realistic Model Selection for Semi-supervised Learning

**Source**: [https://proceedings.mlr.press/v235/li24bv.html](https://proceedings.mlr.press/v235/li24bv.html)

**TLDR**: Proposes a realistic model selection strategy for semi-supervised learning that handles the scarcity of labeled validation data.

## Abstract

Semi-supervised Learning (SSL) has shown remarkable success in applications with limited supervision. However, due to the scarcity of labels in the training process, SSL algorithms are known to be impaired by the lack of proper model selection, as splitting a validation set will further reduce the limited labeled data, and the size of the validation set could be too small to provide a reliable indication to the generalization error. Therefore, we seek alternatives that do not rely on validation data to probe the generalization performance of SSL models. Specifically, we find that the distinct margin distribution in SSL can be effectively utilized in conjunction with the model’s spectral complexity, to provide a non-vacuous indication of the generalization error. Built upon this, we propose a novel model selection method, specifically tailored for SSL, known as Spectral-normalized Labeled-margin Minimization (SLAM). We prove that the model selected by SLAM has upper-bounded differences w.r.t. the best model within the search space. In addition, comprehensive experiments showcase that SLAM can achieve significant improvements compared to its counterparts, verifying its efficacy from both theoretical and empirical standpoints.