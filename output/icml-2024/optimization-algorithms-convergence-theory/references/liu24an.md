---
title: "Convergence of Online Learning Algorithm for a Mixture of Multiple Linear Regressions"
source: "https://proceedings.mlr.press/v235/liu24an.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24an/liu24an.pdf"
categories: ['optimization-algorithms-convergence-theory', 'generative-models-and-variational-inference']
tags: ['mixture-of-regressions', 'online-learning', 'convergence-analysis']
venue: "ICML 2024"
tldr: "An online learning algorithm for mixture of multiple linear regressions with provable convergence guarantees via Ljung's ODE method."
---

# Convergence of Online Learning Algorithm for a Mixture of Multiple Linear Regressions

**Source**: [https://proceedings.mlr.press/v235/liu24an.html](https://proceedings.mlr.press/v235/liu24an.html)

**TLDR**: An online learning algorithm for mixture of multiple linear regressions with provable convergence guarantees via Ljung's ODE method.

## Abstract

This paper considers the parameter learning and data clustering problem for MLR with multiple sub-models and arbitrary mixing weights. To deal with the data streaming case, we propose an online learning algorithm to estimate the unknown parameters. By utilizing Ljung’s ODE method, we establish the almost sure convergence results of this MLR problem without the traditional i.i.d. assumption on the input data for the first time. Based on the convergence property and using the classical stochastic Lyapunov function method, we also obtain the convergence rate analysis of the proposed algorithm for the first time. In addition, the data clustering can asymptotically achieve the same performance as the case with known parameters. Future work will consider how to relax the asymptotically stationary and ergodic assumption on the input data, and how to design algorithms with global convergence performance for the MLR problem.