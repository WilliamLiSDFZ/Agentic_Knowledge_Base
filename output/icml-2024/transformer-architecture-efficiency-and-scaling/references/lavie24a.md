---
title: "Towards Understanding Inductive Bias in Transformers: A View From Infinity"
source: "https://proceedings.mlr.press/v235/lavie24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lavie24a/lavie24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'neural-network-learning-dynamics-theory']
tags: ['transformers', 'inductive-bias', 'Gaussian-process', 'permutation-symmetry', 'representation-theory']
venue: "ICML 2024"
tldr: "A study of transformer inductive bias in the infinite-width Gaussian process limit, showing transformers favor permutation-symmetric functions via symmetric group representation theory."
---

# Towards Understanding Inductive Bias in Transformers: A View From Infinity

**Source**: [https://proceedings.mlr.press/v235/lavie24a.html](https://proceedings.mlr.press/v235/lavie24a.html)

**TLDR**: A study of transformer inductive bias in the infinite-width Gaussian process limit, showing transformers favor permutation-symmetric functions via symmetric group representation theory.

## Abstract

We study inductive bias in Transformers in the infinitely over-parameterized Gaussian process limit and argue transformers tend to be biased towards more permutation symmetric functions in sequence space. We show that the representation theory of the symmetric group can be used to give quantitative analytical predictions when the dataset is symmetric to permutations between tokens. We present a simplified transformer block and solve the model at the limit, including accurate predictions for the learning curves and network outputs. We show that in common setups, one can derive tight bounds in the form of a scaling law for the learnability as a function of the context length. Finally, we argue WikiText dataset, does indeed possess a degree of permutation symmetry.