---
title: "Neural Collapse in Multi-label Learning with Pick-all-label Loss"
source: "https://proceedings.mlr.press/v235/li24ai.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24ai/li24ai.pdf"
categories: ['neural-network-learning-dynamics-theory', 'algebraic-structures-in-machine-learning']
tags: ['neural-collapse', 'multi-label-learning', 'deep-neural-networks', 'classification', 'geometry']
venue: "ICML 2024"
tldr: "Neural collapse phenomena are studied and characterized for multi-label classification using a pick-all-label loss framework."
---

# Neural Collapse in Multi-label Learning with Pick-all-label Loss

**Source**: [https://proceedings.mlr.press/v235/li24ai.html](https://proceedings.mlr.press/v235/li24ai.html)

**TLDR**: Neural collapse phenomena are studied and characterized for multi-label classification using a pick-all-label loss framework.

## Abstract

We study deep neural networks for the multi-label classification (MLab) task through the lens of neural collapse (NC). Previous works have been restricted to the multi-class classification setting and discovered a prevalent NC phenomenon comprising of the following properties for the last-layer features: (i) the variability of features within every class collapses to zero, (ii) the set of feature means form an equi-angular tight frame (ETF), and (iii) the last layer classifiers collapse to the feature mean upon some scaling. We generalize the study to multi-label learning, and prove for the first time that a generalized NC phenomenon holds with the "pick-all-label” formulation, which we term as MLab NC. While the ETF geometry remains consistent for features with a single label, multi-label scenarios introduce a unique combinatorial aspect we term the "tag-wise average" property, where the means of features with multiple labels are the scaled averages of means for single-label instances. Theoretically, under proper assumptions on the features, we establish that the only global optimizer of the pick-all-label cross-entropy loss satisfy the multi-label NC. In practice, we demonstrate that our findings can lead to better test performance with more efficient training techniques for MLab learning.