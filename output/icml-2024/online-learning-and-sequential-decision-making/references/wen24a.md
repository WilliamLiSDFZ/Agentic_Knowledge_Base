---
title: "Contrastive Representation for Data Filtering in Cross-Domain Offline Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/wen24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wen24a/wen24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'learning-with-imperfect-data-and-bias']
tags: ['cross-domain', 'offline-reinforcement-learning', 'contrastive-representation', 'data-filtering']
venue: "ICML 2024"
tldr: "A contrastive representation method filters source domain data to mitigate dynamics mismatch in cross-domain offline reinforcement learning."
---

# Contrastive Representation for Data Filtering in Cross-Domain Offline Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/wen24a.html](https://proceedings.mlr.press/v235/wen24a.html)

**TLDR**: A contrastive representation method filters source domain data to mitigate dynamics mismatch in cross-domain offline reinforcement learning.

## Abstract

Cross-domain offline reinforcement learning leverages source domain data with diverse transition dynamics to alleviate the data requirement for the target domain. However, simply merging the data of two domains leads to performance degradation due to the dynamics mismatch. Existing methods address this problem by measuring the dynamics gap via domain classifiers while relying on the assumptions of the transferability of paired domains. In this paper, we propose a novel representation-based approach to measure the domain gap, where the representation is learned through a contrastive objective by sampling transitions from different domains. We show that such an objective recovers the mutual-information gap of transition functions in two domains without suffering from the unbounded issue of the dynamics gap in handling significantly different domains. Based on the representations, we introduce a data filtering algorithm that selectively shares transitions from the source domain according to the contrastive score functions. Empirical results on various tasks demonstrate that our method achieves superior performance, using only 10% of the target data to achieve 89.2% of the performance on 100% target dataset with state-of-the-art methods.