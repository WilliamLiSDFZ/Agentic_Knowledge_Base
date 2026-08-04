---
title: "Provably Scalable Black-Box Variational Inference with Structured Variational Families"
source: "https://proceedings.mlr.press/v235/ko24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ko24d/ko24d.pdf"
categories: ['generative-models-and-variational-inference', 'optimization-algorithms-convergence-theory']
tags: ['variational-inference', 'black-box', 'structured-families', 'scalability', 'covariance']
venue: "ICML 2024"
tldr: "Provably scalable black-box variational inference using structured variational families that overcome the computational limitations of full-rank approximations."
---

# Provably Scalable Black-Box Variational Inference with Structured Variational Families

**Source**: [https://proceedings.mlr.press/v235/ko24d.html](https://proceedings.mlr.press/v235/ko24d.html)

**TLDR**: Provably scalable black-box variational inference using structured variational families that overcome the computational limitations of full-rank approximations.

## Abstract

Variational families with full-rank covariance approximations are known not to work well in black-box variational inference (BBVI), both empirically and theoretically. In fact, recent computational complexity results for BBVI have established that full-rank variational families scale poorly with the dimensionality of the problem compared to e.g. mean-field families. This is particularly critical to hierarchical Bayesian models with local variables; their dimensionality increases with the size of the datasets. Consequently, one gets an iteration complexity with an explicit $\mathcal{O}(N^2)$ dependence on the dataset size $N$. In this paper, we explore a theoretical middle ground between mean-field variational families and full-rank families: structured variational families. We rigorously prove that certain scale matrix structures can achieve a better iteration complexity of $\mathcal{O}\left(N\right)$, implying better scaling with respect to $N$. We empirically verify our theoretical results on large-scale hierarchical models.