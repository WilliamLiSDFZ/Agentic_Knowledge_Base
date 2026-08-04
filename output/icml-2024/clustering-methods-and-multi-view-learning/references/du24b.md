---
title: "SimPro: A Simple Probabilistic Framework Towards Realistic Long-Tailed Semi-Supervised Learning"
source: "https://proceedings.mlr.press/v235/du24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/du24b/du24b.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'clustering-methods-and-multi-view-learning']
tags: ['semi-supervised-learning', 'long-tailed', 'class-imbalance', 'probabilistic-framework']
venue: "ICML 2024"
tldr: "SimPro is a simple probabilistic framework that handles unknown and mismatched unlabeled class distributions in long-tailed semi-supervised learning."
---

# SimPro: A Simple Probabilistic Framework Towards Realistic Long-Tailed Semi-Supervised Learning

**Source**: [https://proceedings.mlr.press/v235/du24b.html](https://proceedings.mlr.press/v235/du24b.html)

**TLDR**: SimPro is a simple probabilistic framework that handles unknown and mismatched unlabeled class distributions in long-tailed semi-supervised learning.

## Abstract

Recent advancements in semi-supervised learning have focused on a more realistic yet challenging task: addressing imbalances in labeled data while the class distribution of unlabeled data remains both unknown and potentially mismatched. Current approaches in this sphere often presuppose rigid assumptions regarding the class distribution of unlabeled data, thereby limiting the adaptability of models to only certain distribution ranges. In this study, we propose a novel approach, introducing a highly adaptable framework, designated as SimPro, which does not rely on any predefined assumptions about the distribution of unlabeled data. Our framework, grounded in a probabilistic model, innovatively refines the expectation-maximization (EM) method by separating the modeling of conditional and marginal class distributions. This separation facilitates a closed-form solution for class distribution estimation during the maximization phase, leading to the formulation of a Bayes classifier. The Bayes classifier, in turn, enhances the quality of pseudo-labels in the expectation phase. Remarkably, the SimPro framework is not only straightforward to implement but also comes with theoretical guarantees. Moreover, we introduce two novel class distributions broadening the scope of the evaluation. Our method showcases consistent state-of-the-art performance across diverse benchmarks and data distribution scenarios. benchmarks and data distribution scenarios. Our code is available at https://github.com/LeapLabTHU/SimPro.