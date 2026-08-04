---
title: "Parameter Estimation in DAGs from Incomplete Data via Optimal Transport"
source: "https://proceedings.mlr.press/v235/vo24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/vo24a/vo24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'generative-models-and-variational-inference']
tags: ['DAG', 'parameter-estimation', 'missing-data', 'optimal-transport', 'probabilistic-graphical-models']
venue: "ICML 2024"
tldr: "Proposes an optimal transport-based approach for parameter estimation in directed acyclic graphical models from incomplete data with latent variables."
---

# Parameter Estimation in DAGs from Incomplete Data via Optimal Transport

**Source**: [https://proceedings.mlr.press/v235/vo24a.html](https://proceedings.mlr.press/v235/vo24a.html)

**TLDR**: Proposes an optimal transport-based approach for parameter estimation in directed acyclic graphical models from incomplete data with latent variables.

## Abstract

Estimating the parameters of a probabilistic directed graphical model from incomplete data is a long-standing challenge. This is because, in the presence of latent variables, both the likelihood function and posterior distribution are intractable without assumptions about structural dependencies or model classes. While existing learning methods are fundamentally based on likelihood maximization, here we offer a new view of the parameter learning problem through the lens of optimal transport. This perspective licenses a general framework that operates on any directed graphs without making unrealistic assumptions on the posterior over the latent variables or resorting to variational approximations. We develop a theoretical framework and support it with extensive empirical evidence demonstrating the versatility and robustness of our approach. Across experiments, we show that not only can our method effectively recover the ground-truth parameters but it also performs comparably or better than competing baselines on downstream applications.