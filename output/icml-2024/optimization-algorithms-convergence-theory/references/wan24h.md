---
title: "Non-stationary Online Convex Optimization with Arbitrary Delays"
source: "https://proceedings.mlr.press/v235/wan24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wan24h/wan24h.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['online-convex-optimization', 'delayed-gradients', 'non-stationary', 'dynamic-regret', 'bandit-feedback']
venue: "ICML 2024"
tldr: "This paper analyzes online convex optimization with arbitrary delays in non-stationary environments and derives dynamic regret bounds."
---

# Non-stationary Online Convex Optimization with Arbitrary Delays

**Source**: [https://proceedings.mlr.press/v235/wan24h.html](https://proceedings.mlr.press/v235/wan24h.html)

**TLDR**: This paper analyzes online convex optimization with arbitrary delays in non-stationary environments and derives dynamic regret bounds.

## Abstract

Online convex optimization (OCO) with arbitrary delays, in which gradients or other information of functions could be arbitrarily delayed, has received increasing attention recently. Different from previous studies that focus on stationary environments, this paper investigates the delayed OCO in non-stationary environments, and aims to minimize the dynamic regret with respect to any sequence of comparators. To this end, we first propose a simple algorithm, namely DOGD, which performs a gradient descent step for each delayed gradient according to their arrival order. Despite its simplicity, our novel analysis shows that the dynamic regret of DOGD can be automatically bounded by $O(\sqrt{\bar{d}T}(P_T+1))$ under mild assumptions, and $O(\sqrt{dT}(P_T+1))$ in the worst case, where $\bar{d}$ and $d$ denote the average and maximum delay respectively, $T$ is the time horizon, and $P_T$ is the path-length of comparators. Furthermore, we develop an improved algorithm, which reduces those dynamic regret bounds achieved by DOGD to $O(\sqrt{\bar{d}T(P_T+1)})$ and $O(\sqrt{dT(P_T+1)})$, respectively. The key idea is to run multiple DOGD with different learning rates, and utilize a meta-algorithm to track the best one based on their delayed performance. Finally, we demonstrate that our improved algorithm is optimal in the worst case by deriving a matching lower bound.