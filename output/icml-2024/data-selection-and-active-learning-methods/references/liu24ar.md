---
title: "Learning with Partial-Label and Unlabeled Data: A Uniform Treatment for Supervision Redundancy and Insufficiency"
source: "https://proceedings.mlr.press/v235/liu24ar.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24ar/liu24ar.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'data-selection-and-active-learning-methods']
tags: ['partial-label-learning', 'semi-supervised', 'weakly-supervised']
venue: "ICML 2024"
tldr: "A unified framework for learning with partial labels and unlabeled data that handles both supervision redundancy and insufficiency consistently."
---

# Learning with Partial-Label and Unlabeled Data: A Uniform Treatment for Supervision Redundancy and Insufficiency

**Source**: [https://proceedings.mlr.press/v235/liu24ar.html](https://proceedings.mlr.press/v235/liu24ar.html)

**TLDR**: A unified framework for learning with partial labels and unlabeled data that handles both supervision redundancy and insufficiency consistently.

## Abstract

One major challenge in weakly supervised learning is learning from inexact supervision, ranging from partial labels (PLs) with redundant information to the extreme of unlabeled data with insufficient information. While recent work has made significant strides in specific inexact supervision contexts, supervision forms typically coexist in complex combinations. This is exemplified in semi-supervised partial label learning, where PLs act as the exclusive supervision in a semi-supervised setting. Current strategies addressing combined inexact scenarios are usually composite, which can lead to incremental solutions that essentially replicate existing methods. In this paper, we propose a novel approach to uniformly tackle both label redundancy and insufficiency, derived from a mutual information-based perspective. We design a label channel that facilitates dynamic label exchange within the candidate label sets, which identifies potential true labels and filters out likely incorrect ones, thereby minimizing error accumulation. Experimental results demonstrate the superiority of our method over existing state-of-the-art PL and semi-supervised learning approaches by directly integrating them. Furthermore, our extended experiments on partial-complementary label learning underscore the flexibility of our uniform treatment in managing diverse supervision scenarios.