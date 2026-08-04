---
title: "Bayesian Optimization of Function Networks with Partial Evaluations"
source: "https://proceedings.mlr.press/v235/buathong24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/buathong24a/buathong24a.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'optimization-algorithms-convergence-theory']
tags: ['bayesian-optimization', 'function-networks', 'partial-evaluations', 'acquisition-functions']
venue: "ICML 2024"
tldr: "Extends Bayesian optimization of function networks to support partial evaluations for more efficient optimization of networked objectives."
---

# Bayesian Optimization of Function Networks with Partial Evaluations

**Source**: [https://proceedings.mlr.press/v235/buathong24a.html](https://proceedings.mlr.press/v235/buathong24a.html)

**TLDR**: Extends Bayesian optimization of function networks to support partial evaluations for more efficient optimization of networked objectives.

## Abstract

Bayesian optimization is a powerful framework for optimizing functions that are expensive or time-consuming to evaluate. Recent work has considered Bayesian optimization of function networks (BOFN), where the objective function is given by a network of functions, each taking as input the output of previous nodes in the network as well as additional parameters. Leveraging this network structure has been shown to yield significant performance improvements. Existing BOFN algorithms for general-purpose networks evaluate the full network at each iteration. However, many real-world applications allow for evaluating nodes individually. To exploit this, we propose a novel knowledge gradient acquisition function that chooses which node and corresponding inputs to evaluate in a cost-aware manner, thereby reducing query costs by evaluating only on a part of the network at each step. We provide an efficient approach to optimizing our acquisition function and show that it outperforms existing BOFN methods and other benchmarks across several synthetic and real-world problems. Our acquisition function is the first to enable cost-aware optimization of a broad class of function networks.