---
title: "Principled Preferential Bayesian Optimization"
source: "https://proceedings.mlr.press/v235/xu24y.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24y/xu24y.pdf"
categories: ['bayesian-optimization-and-surrogate-methods']
tags: ['preferential-Bayesian-optimization', 'preference-feedback', 'confidence-sets']
venue: "ICML 2024"
tldr: "A principled preferential Bayesian optimization framework is developed using likelihood-ratio-based confidence sets to optimize black-box functions from pairwise preference feedback."
---

# Principled Preferential Bayesian Optimization

**Source**: [https://proceedings.mlr.press/v235/xu24y.html](https://proceedings.mlr.press/v235/xu24y.html)

**TLDR**: A principled preferential Bayesian optimization framework is developed using likelihood-ratio-based confidence sets to optimize black-box functions from pairwise preference feedback.

## Abstract

We study the problem of preferential Bayesian optimization (BO), where we aim to optimize a black-box function with only preference feedback over a pair of candidate solutions. Inspired by the likelihood ratio idea, we construct a confidence set of the black-box function using only the preference feedback. An optimistic algorithm with an efficient computational method is then developed to solve the problem, which enjoys an information-theoretic bound on the total cumulative regret, a first-of-its-kind for preferential BO. This bound further allows us to design a scheme to report an estimated best solution, with a guaranteed convergence rate. Experimental results on sampled instances from Gaussian processes, standard test functions, and a thermal comfort optimization problem all show that our method stably achieves better or competitive performance as compared to the existing state-of-the-art heuristics, which, however, do not have theoretical guarantees on regret bounds or convergence.