---
title: "Positive and Unlabeled Learning with Controlled Probability Boundary Fence"
source: "https://proceedings.mlr.press/v235/li24p.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24p/li24p.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['PU-learning', 'binary-classification', 'probability-boundary', 'unlabeled-data', 'learning-theory']
venue: "ICML 2024"
tldr: "Derives a theorem on probability boundary fences in PU learning to improve binary classification from positive and unlabeled data."
---

# Positive and Unlabeled Learning with Controlled Probability Boundary Fence

**Source**: [https://proceedings.mlr.press/v235/li24p.html](https://proceedings.mlr.press/v235/li24p.html)

**TLDR**: Derives a theorem on probability boundary fences in PU learning to improve binary classification from positive and unlabeled data.

## Abstract

Positive and Unlabeled (PU) learning refers to a special case of binary classification, and technically, it aims to induce a binary classifier from a few labeled positive training instances and loads of unlabeled instances. In this paper, we derive a theorem indicating that the probability boundary of the asymmetric disambiguation-free expected risk of PU learning is controlled by its asymmetric penalty, and we further empirically evaluated this theorem. Inspired by the theorem and its empirical evaluations, we propose an easy-to-implement two-stage PU learning method, namely Positive and Unlabeled Learning with Controlled Probability Boundary Fence (PULCPBF). In the first stage, we train a set of weak binary classifiers concerning different probability boundaries by minimizing the asymmetric disambiguation-free empirical risks with specific asymmetric penalty values. We can interpret these induced weak binary classifiers as a probability boundary fence. For each unlabeled instance, we can use the predictions to locate its class posterior probability and generate a stochastic label. In the second stage, we train a strong binary classifier over labeled positive training instances and all unlabeled instances with stochastic labels in a self-training manner. Extensive empirical results demonstrate that PULCPBF can achieve competitive performance compared with the existing PU learning baselines.