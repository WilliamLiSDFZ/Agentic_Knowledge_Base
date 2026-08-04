---
title: "Proactive DP: A Multiple Target Optimization Framework for DP-SGD"
source: "https://proceedings.mlr.press/v235/van-dijk24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/van-dijk24a/van-dijk24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'optimization-algorithms-convergence-theory']
tags: ['differential-privacy', 'DP-SGD', 'privacy-budget']
venue: "ICML 2024"
tldr: "Introduces a proactive multiple-target optimization framework for DP-SGD that selects parameters a priori based on fixed privacy budgets."
---

# Proactive DP: A Multiple Target Optimization Framework for DP-SGD

**Source**: [https://proceedings.mlr.press/v235/van-dijk24a.html](https://proceedings.mlr.press/v235/van-dijk24a.html)

**TLDR**: Introduces a proactive multiple-target optimization framework for DP-SGD that selects parameters a priori based on fixed privacy budgets.

## Abstract

We introduce a multiple target optimization framework for DP-SGD referred to as pro-active DP. In contrast to traditional DP accountants, which are used to track the expenditure of privacy budgets, the pro-active DP scheme allows one to a-priori select parameters of DP-SGD based on a fixed privacy budget (in terms of $\epsilon$ and $\delta$) in such a way to optimize the anticipated utility (test accuracy) the most. To achieve this objective, we first propose significant improvements to the moment account method, presenting a closed-form $(\epsilon,\delta)$-DP guarantee that connects all parameters in the DP-SGD setup. Generally, DP-SGD is $(\epsilon\leq 1/2,\delta=1/N)$-DP if $\sigma=\sqrt{2(\epsilon +\ln(1/\delta))/\epsilon}$ with $T$ at least $\approx 2k^2/\epsilon$ and $(2/e)^2k^2-1/2\geq \ln(N)$, where $T$ is the total number of rounds, and $K=kN$ is the total number of gradient computations where $k$ measures $K$ in number of epochs of size $N$ of the local data set. We prove that our expression is close to tight in that if $T$ is more than a constant factor $\approx 4$ smaller than the lower bound $\approx 2k^2/\epsilon$, then the $(\epsilon,\delta)$-DP guarantee is violated. Our enhanced DP theory allows us to create a utility graph and DP calculator. These tools link privacy and utility objectives and search for optimal experiment setups, efficiently taking into account both accuracy and privacy objectives, as well as implementation goals. We furnish a comprehensive implementation flow of our proactive DP, with rigorous experiments to showcase the proof-of-concept.