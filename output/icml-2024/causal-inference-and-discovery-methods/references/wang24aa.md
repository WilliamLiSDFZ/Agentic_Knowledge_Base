---
title: "Optimal Kernel Choice for Score Function-based Causal Discovery"
source: "https://proceedings.mlr.press/v235/wang24aa.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24aa/wang24aa.pdf"
categories: ['causal-inference-and-discovery-methods', 'bayesian-optimization-and-surrogate-methods']
tags: ['causal-discovery', 'kernel-methods', 'score-functions', 'structure-learning']
venue: "ICML 2024"
tldr: "An optimal kernel selection method is proposed for score function-based causal discovery to better handle general data distributions."
---

# Optimal Kernel Choice for Score Function-based Causal Discovery

**Source**: [https://proceedings.mlr.press/v235/wang24aa.html](https://proceedings.mlr.press/v235/wang24aa.html)

**TLDR**: An optimal kernel selection method is proposed for score function-based causal discovery to better handle general data distributions.

## Abstract

Score-based methods have demonstrated their effectiveness in discovering causal relationships by scoring different causal structures based on their goodness of fit to the data. Recently, Huang et al. proposed a generalized score function that can handle general data distributions and causal relationships by modeling the relations in reproducing kernel Hilbert space (RKHS). The selection of an appropriate kernel within this score function is crucial for accurately characterizing causal relationships and ensuring precise causal discovery. However, the current method involves manual heuristic selection of kernel parameters, making the process tedious and less likely to ensure optimality. In this paper, we propose a kernel selection method within the generalized score function that automatically selects the optimal kernel that best fits the data. Specifically, we model the generative process of the variables involved in each step of the causal graph search procedure as a mixture of independent noise variables. Based on this model, we derive an automatic kernel selection method by maximizing the marginal likelihood of the variables involved in each search step. We conduct experiments on both synthetic data and real-world benchmarks, and the results demonstrate that our proposed method outperforms heuristic kernel selection methods.