---
title: "Acquisition Conditioned Oracle for Nongreedy Active Feature Acquisition"
source: "https://proceedings.mlr.press/v235/valancius24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/valancius24a/valancius24a.pdf"
categories: ['data-selection-and-active-learning-methods', 'ai-explainability-uncertainty-human-decision-making']
tags: ['active-feature-acquisition', 'non-greedy', 'oracle-conditioning']
venue: "ICML 2024"
tldr: "Introduces an acquisition-conditioned oracle enabling non-greedy active feature acquisition for cost-efficient inference."
---

# Acquisition Conditioned Oracle for Nongreedy Active Feature Acquisition

**Source**: [https://proceedings.mlr.press/v235/valancius24a.html](https://proceedings.mlr.press/v235/valancius24a.html)

**TLDR**: Introduces an acquisition-conditioned oracle enabling non-greedy active feature acquisition for cost-efficient inference.

## Abstract

We develop novel methodology for active feature acquisition (AFA), the study of sequentially acquiring a dynamic subset of features that minimizes acquisition costs whilst still yielding accurate inference. The AFA framework can be useful in a myriad of domains, including health care applications where the cost of acquiring additional features for a patient (in terms of time, money, risk, etc.) can be weighed against the expected improvement to diagnostic performance. Previous approaches for AFA have employed either: deep learning RL techniques, which have difficulty training policies due to a complicated state and action space; deep learning surrogate generative models, which require modeling complicated multidimensional conditional distributions; or greedy policies, which cannot account for jointly informative feature acquisitions. We show that we can bypass many of these challenges with a novel, nonparametric oracle based approach, which we coin the acquisition conditioned oracle (ACO). Extensive experiments show the superiority of the ACO to state-of-the-art AFA methods when acquiring features for both predictions and general decision-making.