---
title: "Probability Distribution of Hypervolume Improvement in Bi-objective Bayesian Optimization"
source: "https://proceedings.mlr.press/v235/wang24ce.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24ce/wang24ce.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'generative-models-and-variational-inference']
tags: ['multi-objective-Bayesian-optimization', 'hypervolume-improvement', 'probability-distribution', 'acquisition-functions']
venue: "ICML 2024"
tldr: "Derives the exact probability distribution of hypervolume improvement for bi-objective Bayesian optimization to enable principled acquisition function design."
---

# Probability Distribution of Hypervolume Improvement in Bi-objective Bayesian Optimization

**Source**: [https://proceedings.mlr.press/v235/wang24ce.html](https://proceedings.mlr.press/v235/wang24ce.html)

**TLDR**: Derives the exact probability distribution of hypervolume improvement for bi-objective Bayesian optimization to enable principled acquisition function design.

## Abstract

Hypervolume improvement (HVI) is commonly employed in multi-objective Bayesian optimization algorithms to define acquisition functions due to its Pareto-compliant property. Rather than focusing on specific statistical moments of HVI, this work aims to provide the exact expression of HVI’s probability distribution for bi-objective problems. Considering a bi-variate Gaussian random variable resulting from Gaussian process (GP) modeling, we derive the probability distribution of its hypervolume improvement via a cell partition-based method. Our exact expression is superior in numerical accuracy and computation efficiency compared to the Monte Carlo approximation of HVI’s distribution. Utilizing this distribution, we propose a novel acquisition function - $\varepsilon$-probability of hypervolume improvement ($\varepsilon$-PoHVI). Experimentally, we show that on many widely-applied bi-objective test problems, $\varepsilon$-PoHVI significantly outperforms other related acquisition functions, e.g., $\varepsilon$-PoI, and expected hypervolume improvement, when the GP model exhibits a large the prediction uncertainty.