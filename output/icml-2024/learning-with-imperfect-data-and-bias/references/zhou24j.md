---
title: "Pedestrian Attribute Recognition as Label-balanced Multi-label Learning"
source: "https://proceedings.mlr.press/v235/zhou24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24j/zhou24j.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'learning-with-imperfect-data-and-bias']
tags: ['pedestrian-attribute-recognition', 'label-imbalance', 'multi-label-learning']
venue: "ICML 2024"
tldr: "Addresses label and semantic imbalance in pedestrian attribute recognition through a label-balanced multi-label learning framework."
---

# Pedestrian Attribute Recognition as Label-balanced Multi-label Learning

**Source**: [https://proceedings.mlr.press/v235/zhou24j.html](https://proceedings.mlr.press/v235/zhou24j.html)

**TLDR**: Addresses label and semantic imbalance in pedestrian attribute recognition through a label-balanced multi-label learning framework.

## Abstract

Rooting in the scarcity of most attributes, realistic pedestrian attribute datasets exhibit unduly skewed data distribution, from which two types of model failures are delivered: (1) label imbalance: model predictions lean greatly towards the side of majority labels; (2) semantics imbalance: model is easily overfitted on the under-represented attributes due to their insufficient semantic diversity. To render perfect label balancing, we propose a novel framework that successfully decouples label-balanced data re-sampling from the curse of attributes co-occurrence, i.e., we equalize the sampling prior of an attribute while not biasing that of the co-occurred others. To diversify the attributes semantics and mitigate the feature noise, we propose a Bayesian feature augmentation method to introduce true in-distribution novelty. Handling both imbalances jointly, our work achieves best accuracy on various popular benchmarks, and importantly, with minimal computational budget.