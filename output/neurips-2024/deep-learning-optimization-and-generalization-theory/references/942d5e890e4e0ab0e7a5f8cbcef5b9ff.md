---
title: "The Implicit Bias of Gradient Descent on Separable Multiclass Data"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/942d5e890e4e0ab0e7a5f8cbcef5b9ff-Abstract-Conference.html"
categories: ['deep-learning-optimization-and-generalization-theory', 'machine-learning-theory-and-evaluation-methods']
tags: ['implicit-bias', 'gradient-descent', 'multiclass-classification']
venue: "NeurIPS 2024"
tldr: "This work extends implicit bias theory of gradient descent from binary to multiclass separable data settings."
---

# The Implicit Bias of Gradient Descent on Separable Multiclass Data

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/942d5e890e4e0ab0e7a5f8cbcef5b9ff-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/942d5e890e4e0ab0e7a5f8cbcef5b9ff-Abstract-Conference.html)

**TLDR**: This work extends implicit bias theory of gradient descent from binary to multiclass separable data settings.

## Abstract

Implicit bias describes the phenomenon where optimization-based training algorithms, without explicit regularization, show a preference for simple estimators even when more complex estimators have equal objective values. Multiple works have developed the theory of implicit bias for binary classification under the assumption that the loss satisfies an exponential tail property. However, there is a noticeable gap in analysis for multiclass classification, with only a handful of results which themselves are restricted to the cross-entropy loss. In this work, we employ the framework of Permutation Equivariant and Relative Margin-based (PERM) losses [Wang and Scott, 2024] to introduce a multiclass extension of the exponential tail property. This class of losses includes not only cross-entropy but also other losses. Using this framework, we extend the implicit bias result of Soudry et al. [2018] to multiclass classification. Furthermore, our proof techniques closely mirror those of the binary case, thus illustrating the power of the PERM framework for bridging the binary-multiclass gap.