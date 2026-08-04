---
title: "Partial Multi-View Multi-Label Classification via Semantic Invariance Learning and Prototype Modeling"
source: "https://proceedings.mlr.press/v235/liu24bv.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bv/liu24bv.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'learning-with-imperfect-data-and-bias']
tags: ['multi-view-learning', 'multi-label-classification', 'partial-labels', 'semantic-invariance', 'prototype-modeling']
venue: "ICML 2024"
tldr: "A framework for partial multi-view multi-label classification that jointly learns semantic-invariant cross-view representations and prototype models under missing views and labels."
---

# Partial Multi-View Multi-Label Classification via Semantic Invariance Learning and Prototype Modeling

**Source**: [https://proceedings.mlr.press/v235/liu24bv.html](https://proceedings.mlr.press/v235/liu24bv.html)

**TLDR**: A framework for partial multi-view multi-label classification that jointly learns semantic-invariant cross-view representations and prototype models under missing views and labels.

## Abstract

The difficulty of partial multi-view multi-label learning lies in coupling the consensus of multi-view data with the task relevance of multi-label classification, under the condition where partial views and labels are unavailable. In this paper, we seek to compress cross-view representation to maximize the proportion of shared information to better predict semantic tags. To achieve this, we establish a model consistent with the information bottleneck theory for learning cross-view shared representation, minimizing non-shared information while maintaining feature validity to help increase the purity of task-relevant information. Furthermore, we model multi-label prototype instances in the latent space and learn label correlations in a data-driven manner. Our method outperforms existing state-of-the-art methods on multiple public datasets while exhibiting good compatibility with both partial and complete data. Finally, we experimentally reveal the importance of condensing shared information under the premise of information balancing, in the process of multi-view information encoding and compression.