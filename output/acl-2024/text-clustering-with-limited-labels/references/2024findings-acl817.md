---
title: "Combating Label Sparsity in Short Text Topic Modeling via Nearest Neighbor Augmentation"
source: "https://aclanthology.org/2024.findings-acl.817/"
categories: ['topic-modeling-and-essay-evaluation', 'text-clustering-with-limited-labels']
tags: ['short-text-topic-modeling', 'label-sparsity', 'nearest-neighbor-augmentation']
venue: "ACL 2024"
tldr: "Nearest neighbor augmentation combats label sparsity in short text topic modeling by enriching sparse documents."
---

# Combating Label Sparsity in Short Text Topic Modeling via Nearest Neighbor Augmentation

**Source**: [https://aclanthology.org/2024.findings-acl.817/](https://aclanthology.org/2024.findings-acl.817/)

**TLDR**: Nearest neighbor augmentation combats label sparsity in short text topic modeling by enriching sparse documents.

## Abstract

AbstractExtracting semantic topics from short texts presents a significant challenge in the field of data mining. While efforts have been made to mitigate data sparsity issue, the limited length of short documents also results in the absence of semantically relevant words, causing biased evidence lower bound and incomplete labels for likelihood maximization. We refer to this issue as the label sparsity problem. To combat this problem, we propose kNNTM, a neural short text topic model that incorporates a k-Nearest-Neighbor-based label completion algorithm by augmenting the reconstruction label with k-nearest documents to complement these relevant but unobserved words. Furthermore, seeking a precise reflection of distances between documents, we propose a fused multi-view distances metric that takes both local word similarities and global topic semantics into consideration. Extensive experiments on multiple public short-text datasets show that kNNTM model outperforms the state-of-the-art baseline models and can derive both high-quality topics and document representations.