---
title: "High-Probability Bound for Non-Smooth Non-Convex Stochastic Optimization with Heavy Tails"
source: "https://proceedings.mlr.press/v235/liu24bo.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bo/liu24bo.pdf"
categories: ['optimization-algorithms-convergence-theory', 'online-learning-and-sequential-decision-making']
tags: ['non-convex-optimization', 'heavy-tailed-noise', 'high-probability-bounds', 'stochastic-optimization', 'online-to-non-convex']
venue: "ICML 2024"
tldr: "This paper improves high-probability complexity bounds for finding stationary points in non-smooth non-convex stochastic optimization under heavy-tailed noise."
---

# High-Probability Bound for Non-Smooth Non-Convex Stochastic Optimization with Heavy Tails

**Source**: [https://proceedings.mlr.press/v235/liu24bo.html](https://proceedings.mlr.press/v235/liu24bo.html)

**TLDR**: This paper improves high-probability complexity bounds for finding stationary points in non-smooth non-convex stochastic optimization under heavy-tailed noise.

## Abstract

Recently, Cutkosky et al. introduce the online-to-non-convex framework, which utilizes online learning methods to solve non-smooth non-convex optimization problems, and achieves an $\mathcal{O}(\epsilon^{-3}\delta^{-1})$ gradient complexity for finding $(\delta,\epsilon)$-stationary points. However, their results rely on the bounded variance assumption of stochastic gradients and only hold in expectation. To address these limitations, we investigate the case that stochastic gradients obey heavy-tailed distributions with finite $\mathfrak{p}$-th moments for some $\mathfrak{p}\in(1,2]$, and propose a novel algorithm which is able to identify a $(\delta,\epsilon)$-stationary point with high probability, after consuming $\tilde{\mathcal{O}}(\epsilon^{-\frac{2\mathfrak{p}-1}{\mathfrak{p}-1}}\delta^{-1})$ stochastic gradients. The key idea is first incorporating the gradient clipping technique into the online-to-non-convex framework to produce a sequence of points, the averaged gradient norms of which is no greater than $\epsilon$. Then, we propose a validation method to select one $(\delta,\epsilon)$-stationary point among the candidates. When gradient distributions have bounded variance, i.e., $\mathfrak{p}=2$, our result turns into $\tilde{\mathcal{O}}(\epsilon^{-3}\delta^{-1})$, which improves the existing $\tilde{\mathcal{O}}(\epsilon^{-4}\delta^{-1})$ high-probability bound. When the objective is smooth, our algorithm can also find an $\epsilon$-stationary point with $\tilde{\mathcal{O}}(\epsilon^{-\frac{3\mathfrak{p}-2}{\mathfrak{p}-1}})$ gradient queries.