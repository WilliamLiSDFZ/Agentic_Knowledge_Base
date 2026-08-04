---
title: "How Free is Parameter-Free Stochastic Optimization?"
source: "https://proceedings.mlr.press/v235/attia24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/attia24a/attia24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'online-learning-and-sequential-decision-making']
tags: ['parameter-free-optimization', 'stochastic-optimization', 'convergence-rates', 'hyperparameter-free']
venue: "ICML 2024"
tldr: "Investigates conditions under which fully parameter-free stochastic optimization methods can match optimally tuned convergence rates."
---

# How Free is Parameter-Free Stochastic Optimization?

**Source**: [https://proceedings.mlr.press/v235/attia24a.html](https://proceedings.mlr.press/v235/attia24a.html)

**TLDR**: Investigates conditions under which fully parameter-free stochastic optimization methods can match optimally tuned convergence rates.

## Abstract

We study the problem of parameter-free stochastic optimization, inquiring whether, and under what conditions, do fully parameter-free methods exist: these are methods that achieve convergence rates competitive with optimally tuned methods, without requiring significant knowledge of the true problem parameters. Existing parameter-free methods can only be considered “partially” parameter-free, as they require some non-trivial knowledge of the true problem parameters, such as a bound on the stochastic gradient norms, a bound on the distance to a minimizer, etc. In the non-convex setting, we demonstrate that a simple hyperparameter search technique results in a fully parameter-free method that outperforms more sophisticated state-of-the-art algorithms. We also provide a similar result in the convex setting with access to noisy function values under mild noise assumptions. Finally, assuming only access to stochastic gradients, we establish a lower bound that renders fully parameter-free stochastic convex optimization infeasible, and provide a method which is (partially) parameter-free up to the limit indicated by our lower bound.