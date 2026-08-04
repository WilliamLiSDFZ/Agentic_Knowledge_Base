---
title: "MALIBO: Meta-learning for Likelihood-free Bayesian Optimization"
source: "https://proceedings.mlr.press/v235/pan24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pan24b/pan24b.pdf"
categories: ['bayesian-optimization-and-surrogate-methods']
tags: ['Bayesian-optimization', 'meta-learning', 'likelihood-free', 'surrogate-models']
venue: "ICML 2024"
tldr: "Proposes MALIBO, a meta-learning approach for likelihood-free Bayesian optimization that scales across related tasks."
---

# MALIBO: Meta-learning for Likelihood-free Bayesian Optimization

**Source**: [https://proceedings.mlr.press/v235/pan24b.html](https://proceedings.mlr.press/v235/pan24b.html)

**TLDR**: Proposes MALIBO, a meta-learning approach for likelihood-free Bayesian optimization that scales across related tasks.

## Abstract

Bayesian optimization (BO) is a popular method to optimize costly black-box functions, and meta-learning has emerged as a way to leverage knowledge from related tasks to optimize new tasks faster. However, existing meta-learning methods for BO rely on surrogate models that are not scalable or are sensitive to varying input scales and noise types across tasks. Moreover, they often overlook the uncertainty associated with task similarity, leading to unreliable task adaptation when a new task differs significantly or has not been sufficiently explored yet. We propose a novel meta-learning BO approach that bypasses the surrogate model and directly learns the utility of queries across tasks. It explicitly models task uncertainty and includes an auxiliary model to enable robust adaptation to new tasks. Extensive experiments show that our method achieves strong performance and outperforms multiple meta-learning BO methods across various benchmarks.