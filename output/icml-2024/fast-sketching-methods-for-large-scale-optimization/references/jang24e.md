---
title: "Efficient Low-Rank Matrix Estimation, Experimental Design, and Arm-Set-Dependent Low-Rank Bandits"
source: "https://proceedings.mlr.press/v235/jang24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jang24e/jang24e.pdf"
categories: ['online-learning-and-sequential-decision-making', 'fast-sketching-methods-for-large-scale-optimization']
tags: ['low-rank-matrix-estimation', 'bandits', 'experimental-design', 'trace-regression', 'arm-set']
venue: "ICML 2024"
tldr: "LowPopArt is a novel low-rank matrix estimation method with tight recovery guarantees enabling efficient experimental design and low-rank bandit algorithms."
---

# Efficient Low-Rank Matrix Estimation, Experimental Design, and Arm-Set-Dependent Low-Rank Bandits

**Source**: [https://proceedings.mlr.press/v235/jang24e.html](https://proceedings.mlr.press/v235/jang24e.html)

**TLDR**: LowPopArt is a novel low-rank matrix estimation method with tight recovery guarantees enabling efficient experimental design and low-rank bandit algorithms.

## Abstract

We study low-rank matrix trace regression and the related problem of low-rank matrix bandits. Assuming access to the distribution of the covariates, we propose a novel low-rank matrix estimation method called LowPopArt and provide its recovery guarantee that depends on a novel quantity denoted by $B(Q)$ that characterizes the hardness of the problem, where $Q$ is the covariance matrix of the measurement distribution. We show that our method can provide tighter recovery guarantees than classical nuclear norm penalized least squares (Koltchinskii et al., 2011) in several problems. To perform an efficient estimation with a limited number of measurements from an arbitrarily given measurement set $\mathcal{A}$, we also propose a novel experimental design criterion that minimizes $B(Q)$ with computational efficiency. We leverage our novel estimator and design of experiments to derive two low-rank linear bandit algorithms for general arm sets that enjoy improved regret upper bounds. This improves over previous works on low-rank bandits, which make somewhat restrictive assumptions that the arm set is the unit ball or that an efficient exploration distribution is given. To our knowledge, our experimental design criterion is the first one tailored to low-rank matrix estimation beyond the naive reduction to linear regression, which can be of independent interest.