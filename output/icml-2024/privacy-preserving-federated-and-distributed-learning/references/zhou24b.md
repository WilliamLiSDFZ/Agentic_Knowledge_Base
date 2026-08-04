---
title: "Differentially Private Worst-group Risk Minimization"
source: "https://proceedings.mlr.press/v235/zhou24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24b/zhou24b.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'fairness-aware-algorithmic-decision-making']
tags: ['differential-privacy', 'worst-group-risk', 'distributionally-robust']
venue: "ICML 2024"
tldr: "Provides the first systematic study of worst-group risk minimization under differential privacy, deriving sample complexity bounds for privately finding models minimizing maximal subpopulation risk."
---

# Differentially Private Worst-group Risk Minimization

**Source**: [https://proceedings.mlr.press/v235/zhou24b.html](https://proceedings.mlr.press/v235/zhou24b.html)

**TLDR**: Provides the first systematic study of worst-group risk minimization under differential privacy, deriving sample complexity bounds for privately finding models minimizing maximal subpopulation risk.

## Abstract

We initiate a systematic study of worst-group risk minimization under $(\epsilon, \delta)$-differential privacy (DP). The goal is to privately find a model that approximately minimizes the maximal risk across $p$ sub-populations (groups) with different distributions, where each group distribution is accessed via a sample oracle. We first present a new algorithm that achieves excess worst-group population risk of $\tilde{O}(\frac{p\sqrt{d}}{K\epsilon} + \sqrt{\frac{p}{K}})$, where $K$ is the total number of samples drawn from all groups and $d$ is the problem dimension. Our rate is nearly optimal when each distribution is observed via a fixed-size dataset of size $K/p$. Our result is based on a new stability-based analysis for the generalization error. In particular, we show that $\Delta$-uniform argument stability implies $\tilde{O}(\Delta + \frac{1}{\sqrt{n}})$ generalization error w.r.t. the worst-group risk, where $n$ is the number of samples drawn from each sample oracle. Next, we propose an algorithmic framework for worst-group population risk minimization using any DP online convex optimization algorithm as a subroutine. Hence, we give another excess risk bound of $\tilde{O}\left( \sqrt{\frac{d^{1/2}}{\epsilon K}} +\sqrt{\frac{p}{K\epsilon^2}} + \sqrt{\frac{p}{K}} \right)$. Assuming the typical setting of $\epsilon=\Theta(1)$, this bound is more favorable than our first bound in a certain range of $p$ as a function of $K$ and $d$. Finally, we study differentially private worst-group empirical risk minimization in the offline setting, where each group distribution is observed by a fixed-size dataset. We present a new algorithm with nearly optimal excess risk of $\tilde{O}(\frac{p\sqrt{d}}{K\epsilon})$.