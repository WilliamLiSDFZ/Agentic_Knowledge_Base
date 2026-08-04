---
title: "Noise-Adaptive Confidence Sets for Linear Bandits and Application to Bayesian Optimization"
source: "https://proceedings.mlr.press/v235/jun24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jun24a/jun24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'bayesian-optimization-and-surrogate-methods']
tags: ['linear-bandits', 'noise-adaptation', 'confidence-sets', 'Bayesian-optimization']
venue: "ICML 2024"
tldr: "Develops noise-adaptive confidence sets for linear bandits that efficiently handle unknown noise levels with applications to Bayesian optimization."
---

# Noise-Adaptive Confidence Sets for Linear Bandits and Application to Bayesian Optimization

**Source**: [https://proceedings.mlr.press/v235/jun24a.html](https://proceedings.mlr.press/v235/jun24a.html)

**TLDR**: Develops noise-adaptive confidence sets for linear bandits that efficiently handle unknown noise levels with applications to Bayesian optimization.

## Abstract

Adapting to a priori unknown noise level is a very important but challenging problem in sequential decision-making as efficient exploration typically requires knowledge of the noise level, which is often loosely specified. We report significant progress in addressing this issue in linear bandits in two respects. First, we propose a novel confidence set that is ’semi-adaptive’ to the unknown sub-Gaussian parameter $\sigma_*^2$ in the sense that the (normalized) confidence width scales with $\sqrt{d\sigma_*^2 + \sigma_0^2}$ where $d$ is the dimension and $\sigma_0^2$ is the specified sub-Gaussian parameter (known) that can be much larger than $\sigma_*^2$. This is a significant improvement over $\sqrt{d\sigma_0^2}$ of the standard confidence set of Abbasi-Yadkori et al. (2011), especially when $d$ is large. We show that this leads to an improved regret bound in linear bandits. Second, for bounded rewards, we propose a novel variance-adaptive confidence set that has a much improved numerical performance upon prior art. We then apply this confidence set to develop, as we claim, the first practical variance-adaptive linear bandit algorithm via an optimistic approach, which is enabled by our novel regret analysis technique. Both of our confidence sets rely critically on ‘regret equality’ from online learning. Our empirical evaluation in Bayesian optimization tasks shows that our algorithms demonstrate better or comparable performance compared to existing methods.