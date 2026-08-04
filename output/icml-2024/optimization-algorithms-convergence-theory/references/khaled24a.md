---
title: "Tuning-Free Stochastic Optimization"
source: "https://proceedings.mlr.press/v235/khaled24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/khaled24a/khaled24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'online-learning-and-sequential-decision-making']
tags: ['tuning-free-optimization', 'hyperparameter-free', 'stochastic-optimization']
venue: "ICML 2024"
tldr: "Formalizes and develops tuning-free stochastic optimization algorithms that automatically match the performance of optimally-tuned counterparts."
---

# Tuning-Free Stochastic Optimization

**Source**: [https://proceedings.mlr.press/v235/khaled24a.html](https://proceedings.mlr.press/v235/khaled24a.html)

**TLDR**: Formalizes and develops tuning-free stochastic optimization algorithms that automatically match the performance of optimally-tuned counterparts.

## Abstract

Large-scale machine learning problems make the cost of hyperparameter tuning ever more prohibitive. This creates a need for algorithms that can tune themselves on-the-fly. We formalize the notion of “tuning-free” algorithms that can match the performance of optimally-tuned optimization algorithms up to polylogarithmic factors given only loose hints on the relevant problem parameters. We consider in particular algorithms that can match optimally-tuned Stochastic Gradient Descent (SGD). When the domain of optimization is bounded, we show tuning-free matching of SGD is possible and achieved by several existing algorithms. We prove that for the task of minimizing a convex and smooth or Lipschitz function over an unbounded domain, tuning-free optimization is impossible. We discuss conditions under which tuning-free optimization is possible even over unbounded domains. In particular, we show that the recently proposed DoG and DoWG algorithms are tuning-free when the noise distribution is sufficiently well-behaved. For the task of finding a stationary point of a smooth and potentially nonconvex function, we give a variant of SGD that matches the best-known high-probability convergence rate for tuned SGD at only an additional polylogarithmic cost. However, we also give an impossibility result that shows no algorithm can hope to match the optimal expected convergence rate for tuned SGD with high probability.