---
title: "BOtied: Multi-objective Bayesian optimization with tied multivariate ranks"
source: "https://proceedings.mlr.press/v235/park24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/park24k/park24k.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'submodular-optimization-and-combinatorial-algorithms']
tags: ['multi-objective-Bayesian-optimization', 'Pareto-optimality', 'acquisition-function', 'multivariate-ranks']
venue: "ICML 2024"
tldr: "Proposes BOtied, a multi-objective Bayesian optimization acquisition function based on tied multivariate ranks for efficient Pareto-optimal solution identification."
---

# BOtied: Multi-objective Bayesian optimization with tied multivariate ranks

**Source**: [https://proceedings.mlr.press/v235/park24k.html](https://proceedings.mlr.press/v235/park24k.html)

**TLDR**: Proposes BOtied, a multi-objective Bayesian optimization acquisition function based on tied multivariate ranks for efficient Pareto-optimal solution identification.

## Abstract

Many scientific and industrial applications require the joint optimization of multiple, potentially competing objectives. Multi-objective Bayesian optimization (MOBO) is a sample-efficient framework for identifying Pareto-optimal solutions. At the heart of MOBO is the acquisition function, which determines the next candidate to evaluate by navigating the best compromises among the objectives. Acquisition functions that rely on integrating over the objective space scale poorly to a large number of objectives. In this paper, we show a natural connection between the non-dominated solutions and the highest multivariate rank, which coincides with the extreme level line of the joint cumulative distribution function (CDF). Motivated by this link, we propose the CDF indicator, a Pareto-compliant metric for evaluating the quality of approximate Pareto sets, that can complement the popular hypervolume indicator. We then introduce an acquisition function based on the CDF indicator, called BOtied. BOtied can be implemented efficiently with copulas, a statistical tool for modeling complex, high-dimensional distributions. Our experiments on a variety of synthetic and real-world experiments demonstrate that BOtied outperforms state-of-the-art MOBO algorithms while being computationally efficient for many objectives.