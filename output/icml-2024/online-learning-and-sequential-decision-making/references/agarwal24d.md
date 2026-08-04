---
title: "Improved Differentially Private and Lazy Online Convex Optimization: Lower Regret without Smoothness Requirements"
source: "https://proceedings.mlr.press/v235/agarwal24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/agarwal24d/agarwal24d.pdf"
categories: ['online-learning-and-sequential-decision-making', 'privacy-preserving-federated-and-distributed-learning']
tags: ['differential-privacy', 'online-convex-optimization', 'regret-bounds', 'non-smooth']
venue: "ICML 2024"
tldr: "Designs differentially private OCO algorithms achieving optimal leading-order regret without smoothness requirements."
---

# Improved Differentially Private and Lazy Online Convex Optimization: Lower Regret without Smoothness Requirements

**Source**: [https://proceedings.mlr.press/v235/agarwal24d.html](https://proceedings.mlr.press/v235/agarwal24d.html)

**TLDR**: Designs differentially private OCO algorithms achieving optimal leading-order regret without smoothness requirements.

## Abstract

We design differentially private regret-minimizing algorithms in the online convex optimization (OCO) framework. Unlike recent results, our algorithms and analyses do not require smoothness, thus yielding the first private regret bounds with an optimal leading-order term for non-smooth loss functions. Additionally, even for smooth losses, the resulting regret guarantees improve upon previous results in terms their dependence of dimension. Our results provide the best known rates for DP-OCO in all practical regimes of the privacy parameter, barring when it is exceptionally small. The principal innovation in our algorithm design is the use of sampling from strongly log-concave densities which satisfy the Log-Sobolev Inequality. The resulting concentration of measure allows us to obtain a better trade-off for the dimension factors than prior work, leading to improved results. Following previous works on DP-OCO, the proposed algorithm explicitly limits the number of switches via rejection sampling. Thus, independently of privacy constraints, the algorithm also provides improved results for online convex optimization with a switching budget.