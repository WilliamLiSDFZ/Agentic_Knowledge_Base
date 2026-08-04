---
title: "Generalized Neural Collapse for a Large Number of Classes"
source: "https://proceedings.mlr.press/v235/jiang24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jiang24i/jiang24i.pdf"
categories: ['neural-network-learning-dynamics-theory', 'clustering-methods-and-multi-view-learning']
tags: ['neural-collapse', 'last-layer-features', 'classification', 'large-number-of-classes']
venue: "ICML 2024"
tldr: "Generalized neural collapse theory is extended to characterize last-layer representation geometry for deep classification models with a large number of classes."
---

# Generalized Neural Collapse for a Large Number of Classes

**Source**: [https://proceedings.mlr.press/v235/jiang24i.html](https://proceedings.mlr.press/v235/jiang24i.html)

**TLDR**: Generalized neural collapse theory is extended to characterize last-layer representation geometry for deep classification models with a large number of classes.

## Abstract

Neural collapse provides an elegant mathematical characterization of learned last layer representations (a.k.a. features) and classifier weights in deep classification models. Such results not only provide insights but also motivate new techniques for improving practical deep models. However, most of the existing empirical and theoretical studies in neural collapse focus on the case that the number of classes is small relative to the dimension of the feature space. This paper extends neural collapse to cases where the number of classes are much larger than the dimension of feature space, which broadly occur for language models, retrieval systems, and face recognition applications. We show that the features and classifier exhibit a generalized neural collapse phenomenon, where the minimum one-vs-rest margins is maximized. We provide empirical study to verify the occurrence of generalized neural collapse in practical deep neural networks. Moreover, we provide theoretical study to show that the generalized neural collapse provably occurs under unconstrained feature model with spherical constraint, under certain technical conditions on feature dimension and number of classes.