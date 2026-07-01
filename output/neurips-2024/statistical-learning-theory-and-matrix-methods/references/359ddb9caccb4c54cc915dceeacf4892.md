---
title: "Implicit Regularization Paths of Weighted Neural Representations"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/359ddb9caccb4c54cc915dceeacf4892-Abstract-Conference.html"
categories: ['deep-learning-optimization-and-generalization-theory', 'statistical-learning-theory-and-matrix-methods']
tags: ['implicit-regularization', 'weighted-representations', 'pretrained-features']
venue: "NeurIPS 2024"
tldr: "Derives equivalence paths between weighting and regularization schemes for pretrained feature matrices using free probability theory."
---

# Implicit Regularization Paths of Weighted Neural Representations

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/359ddb9caccb4c54cc915dceeacf4892-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/359ddb9caccb4c54cc915dceeacf4892-Abstract-Conference.html)

**TLDR**: Derives equivalence paths between weighting and regularization schemes for pretrained feature matrices using free probability theory.

## Abstract

We study the implicit regularization effects induced by (observation) weighting of pretrained features.For weight and feature matrices of bounded operator norms that are infinitesimally free with respect to (normalized) trace functionals, we derive equivalence paths connecting different weighting matrices and ridge regularization levels.Specifically, we show that ridge estimators trained on weighted features along the same path are asymptotically equivalent when evaluated against test vectors of bounded norms.These paths can be interpreted as matching the effective degrees of freedom of ridge estimators fitted with weighted features.For the special case of subsampling without replacement, our results apply to independently sampled random features and kernel features and confirm recent conjectures (Conjectures 7 and 8) of the authors on the existence of such paths in Patil and Du (2023).We also present an additive risk decomposition for ensembles of weighted estimators and show that the risks are equivalent along the paths when the ensemble size goes to infinity.As a practical consequence of the path equivalences, we develop an efficient cross-validation method for tuning and apply it to subsampled pretrained representations across several models (e.g., ResNet-50) and datasets (e.g., CIFAR-100).