---
title: "Collaborative Learning with Different Labeling Functions"
source: "https://proceedings.mlr.press/v235/deng24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/deng24d/deng24d.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['collaborative-learning', 'PAC-learning', 'heterogeneous-labels', 'multi-task-learning', 'sample-complexity']
venue: "ICML 2024"
tldr: "Studies collaborative PAC learning where multiple agents have different labeling functions and derives sample complexity bounds without assuming a shared hypothesis."
---

# Collaborative Learning with Different Labeling Functions

**Source**: [https://proceedings.mlr.press/v235/deng24d.html](https://proceedings.mlr.press/v235/deng24d.html)

**TLDR**: Studies collaborative PAC learning where multiple agents have different labeling functions and derives sample complexity bounds without assuming a shared hypothesis.

## Abstract

We study a variant of Collaborative PAC Learning, in which we aim to learn an accurate classifier for each of the $n$ data distributions, while minimizing the number of samples drawn from them in total. Unlike in the usual collaborative learning setup, it is not assumed that there exists a single classifier that is simultaneously accurate for all distributions. We show that, when the data distributions satisfy a weaker realizability assumption, which appeared in (Crammer & Mansour, 2012) in the context of multi-task learning, sample-efficient learning is still feasible. We give a learning algorithm based on Empirical Risk Minimization (ERM) on a natural augmentation of the hypothesis class, and the analysis relies on an upper bound on the VC dimension of this augmented class. In terms of the computational efficiency, we show that ERM on the augmented hypothesis class is $\mathsf{NP}$-hard, which gives evidence against the existence of computationally efficient learners in general. On the positive side, for two special cases, we give learners that are both sample- and computationally-efficient.