---
title: "Embarrassingly Parallel GFlowNets"
source: "https://proceedings.mlr.press/v235/silva24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/silva24a/silva24a.pdf"
categories: ['probabilistic-generating-circuits-research', 'sampling-compression-and-dimensionality-reduction']
tags: ['GFlowNets', 'parallel-sampling', 'posterior-inference']
venue: "ICML 2024"
tldr: "Introduces an embarrassingly parallel training framework for GFlowNets to enable scalable discrete compositional sampling."
---

# Embarrassingly Parallel GFlowNets

**Source**: [https://proceedings.mlr.press/v235/silva24a.html](https://proceedings.mlr.press/v235/silva24a.html)

**TLDR**: Introduces an embarrassingly parallel training framework for GFlowNets to enable scalable discrete compositional sampling.

## Abstract

GFlowNets are a promising alternative to MCMC sampling for discrete compositional random variables. Training GFlowNets requires repeated evaluations of the unnormalized target distribution, or reward function. However, for large-scale posterior sampling, this may be prohibitive since it incurs traversing the data several times. Moreover, if the data are distributed across clients, employing standard GFlowNets leads to intensive client-server communication. To alleviate both these issues, we propose embarrassingly parallel GFlowNet (EP-GFlowNet). EP-GFlowNet is a provably correct divide-and-conquer method to sample from product distributions of the form $R(\cdot) \propto R_1(\cdot) ... R_N(\cdot)$ — e.g., in parallel or federated Bayes, where each $R_n$ is a local posterior defined on a data partition. First, in parallel, we train a local GFlowNet targeting each $R_n$ and send the resulting models to the server. Then, the server learns a global GFlowNet by enforcing our newly proposed aggregating balance condition, requiring a single communication step. Importantly, EP-GFlowNets can also be applied to multi-objective optimization and model reuse. Our experiments illustrate the effectiveness of EP-GFlowNets on multiple tasks, including parallel Bayesian phylogenetics, multi-objective multiset and sequence generation, and federated Bayesian structure learning.