---
title: "Relaxing the Accurate Imputation Assumption in Doubly Robust Learning for Debiased Collaborative Filtering"
source: "https://proceedings.mlr.press/v235/li24cq.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24cq/li24cq.pdf"
categories: ['information-retrieval-and-recommendation-systems']
tags: ['collaborative-filtering', 'debiasing', 'doubly-robust']
venue: "ICML 2024"
tldr: "This paper relaxes the accurate imputation assumption in doubly robust learning to improve debiased collaborative filtering."
---

# Relaxing the Accurate Imputation Assumption in Doubly Robust Learning for Debiased Collaborative Filtering

**Source**: [https://proceedings.mlr.press/v235/li24cq.html](https://proceedings.mlr.press/v235/li24cq.html)

**TLDR**: This paper relaxes the accurate imputation assumption in doubly robust learning to improve debiased collaborative filtering.

## Abstract

Recommender system aims to recommend items or information that may interest users based on their behaviors and preferences. However, there may be sampling selection bias in the data collection process, i.e., the collected data is not a representative of the target population. Many debiasing methods are developed based on pseudo-labelings. Nevertheless, the validity of these methods relies heavily on accurate pseudo-labelings (i.e., the imputed labels), which is difficult to satisfy in practice. In this paper, we theoretically propose several novel doubly robust estimators that are unbiased when either (a) the pseudo-labelings deviate from the true labels with an arbitrary user-specific inductive bias, item-specific inductive bias, or a combination of both, or (b) the learned propensities are accurate. We further propose a propensity reconstruction learning approach that adaptively updates the constraint weights using an attention mechanism and effectively controls the variance. Extensive experiments show that our approach outperforms the state-of-the-art on one semi-synthetic and three real-world datasets.