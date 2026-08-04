---
title: "Collaborative Heterogeneous Causal Inference Beyond Meta-analysis"
source: "https://proceedings.mlr.press/v235/guo24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/guo24c/guo24c.pdf"
categories: ['causal-inference-and-discovery-methods', 'privacy-preserving-federated-and-distributed-learning']
tags: ['causal-inference', 'federated-learning', 'heterogeneity', 'multi-site', 'covariate-shift']
venue: "ICML 2024"
tldr: "A collaborative causal inference framework that handles heterogeneity across data centers beyond standard meta-analysis reweighting."
---

# Collaborative Heterogeneous Causal Inference Beyond Meta-analysis

**Source**: [https://proceedings.mlr.press/v235/guo24c.html](https://proceedings.mlr.press/v235/guo24c.html)

**TLDR**: A collaborative causal inference framework that handles heterogeneity across data centers beyond standard meta-analysis reweighting.

## Abstract

Collaboration between different data centers is often challenged by heterogeneity across sites. To account for the heterogeneity, the state-of-the-art method is to re-weight the covariate distributions in each site to match the distribution of the target population. Nevertheless, this method still relies on the concept of traditional meta-analysis after adjusting for the distribution shift. This work proposes a collaborative inverse propensity score weighting estimator for causal inference with heterogeneous data. Instead of adjusting the distribution shift separately, we use weighted propensity score models to collaboratively adjust for the distribution shift. Our method shows significant improvements over the methods based on meta-analysis when heterogeneity increases. By incorporating outcome regression models, we prove the asymptotic normality when the covariates have dimension $d<8$. Our methods preserve privacy at individual sites by implementing federated learning protocols.