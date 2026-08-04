---
title: "Category-Aware Active Domain Adaptation"
source: "https://proceedings.mlr.press/v235/xiao24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xiao24b/xiao24b.pdf"
categories: ['data-selection-and-active-learning-methods', 'test-time-adaptation-methods-and-evaluation']
tags: ['active-learning', 'domain-adaptation', 'category-aware']
venue: "ICML 2024"
tldr: "Category-aware active domain adaptation that addresses per-category performance imbalance in unsupervised domain adaptation via targeted sample selection."
---

# Category-Aware Active Domain Adaptation

**Source**: [https://proceedings.mlr.press/v235/xiao24b.html](https://proceedings.mlr.press/v235/xiao24b.html)

**TLDR**: Category-aware active domain adaptation that addresses per-category performance imbalance in unsupervised domain adaptation via targeted sample selection.

## Abstract

Active domain adaptation has shown promising results in enhancing unsupervised domain adaptation (DA), by actively selecting and annotating a small amount of unlabeled samples from the target domain. Despite its effectiveness in boosting overall performance, the gain usually concentrates on the categories that are readily improvable, while challenging categories that demand the utmost attention are often overlooked by existing models. To alleviate this discrepancy, we propose a novel category-aware active DA method that aims to boost the adaptation for the individual category without adversely affecting others. Specifically, our approach identifies the unlabeled data that are most important for the recognition of the targeted category. Our method assesses the impact of each unlabeled sample on the recognition loss of the target data via the influence function, which allows us to directly evaluate the sample importance, without relying on indirect measurements used by existing methods. Comprehensive experiments and in-depth explorations demonstrate the efficacy of our method on category-aware active DA over three datasets.