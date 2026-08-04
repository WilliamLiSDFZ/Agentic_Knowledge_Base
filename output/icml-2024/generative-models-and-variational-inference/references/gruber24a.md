---
title: "A Bias-Variance-Covariance Decomposition of Kernel Scores for Generative Models"
source: "https://proceedings.mlr.press/v235/gruber24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gruber24a/gruber24a.pdf"
categories: ['generative-models-and-variational-inference', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['bias-variance-decomposition', 'generative-models', 'uncertainty-estimation']
venue: "ICML 2024"
tldr: "This paper derives a bias-variance-covariance decomposition of kernel scores to theoretically characterize generalization and uncertainty in generative models."
---

# A Bias-Variance-Covariance Decomposition of Kernel Scores for Generative Models

**Source**: [https://proceedings.mlr.press/v235/gruber24a.html](https://proceedings.mlr.press/v235/gruber24a.html)

**TLDR**: This paper derives a bias-variance-covariance decomposition of kernel scores to theoretically characterize generalization and uncertainty in generative models.

## Abstract

Generative models, like large language models, are becoming increasingly relevant in our daily lives, yet a theoretical framework to assess their generalization behavior and uncertainty does not exist. Particularly, the problem of uncertainty estimation is commonly solved in an ad-hoc and task-dependent manner. For example, natural language approaches cannot be transferred to image generation. In this paper, we introduce the first bias-variance-covariance decomposition for kernel scores. This decomposition represents a theoretical framework from which we derive a kernel-based variance and entropy for uncertainty estimation. We propose unbiased and consistent estimators for each quantity which only require generated samples but not the underlying model itself. Based on the wide applicability of kernels, we demonstrate our framework via generalization and uncertainty experiments for image, audio, and language generation. Specifically, kernel entropy for uncertainty estimation is more predictive of performance on CoQA and TriviaQA question answering datasets than existing baselines and can also be applied to closed-source models.