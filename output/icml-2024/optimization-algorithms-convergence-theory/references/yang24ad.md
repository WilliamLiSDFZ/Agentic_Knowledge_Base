---
title: "Stability and Generalization of Stochastic Compositional Gradient Descent Algorithms"
source: "https://proceedings.mlr.press/v235/yang24ad.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24ad/yang24ad.pdf"
categories: ['optimization-algorithms-convergence-theory', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['stochastic-compositional-optimization', 'stability', 'generalization']
venue: "ICML 2024"
tldr: "A stability and generalization analysis of stochastic compositional gradient descent algorithms for nested expectation optimization problems."
---

# Stability and Generalization of Stochastic Compositional Gradient Descent Algorithms

**Source**: [https://proceedings.mlr.press/v235/yang24ad.html](https://proceedings.mlr.press/v235/yang24ad.html)

**TLDR**: A stability and generalization analysis of stochastic compositional gradient descent algorithms for nested expectation optimization problems.

## Abstract

Many machine learning tasks can be formulated as a stochastic compositional optimization (SCO) problem such as reinforcement learning, AUC maximization and meta-learning, where the objective function involves a nested composition associated with an expectation. Although many studies have been devoted to studying the convergence behavior of SCO algorithms, there is little work on understanding their generalization, that is, how these learning algorithms built from training data would behave on future test examples. In this paper, we provide the stability and generalization analysis of stochastic compositional gradient descent algorithms in the framework of statistical learning theory. Firstly, we introduce a stability concept called compositional uniform stability and establish its quantitative relation with generalization for SCO problems. Then, we establish the compositional uniform stability results for two notable stochastic compositional gradient descent algorithms, namely SCGD and SCSC. Finally, we derive dimension-independent excess risk bounds for SCGD and SCSC by balancing stability results and optimization errors. To the best of our knowledge, these are the first-ever known results on stability and generalization analysis of stochastic compositional gradient descent algorithms.