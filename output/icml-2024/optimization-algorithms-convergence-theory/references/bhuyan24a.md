---
title: "Best of Both Worlds Guarantees for Smoothed Online Quadratic Optimization"
source: "https://proceedings.mlr.press/v235/bhuyan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bhuyan24a/bhuyan24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['online-optimization', 'quadratic-optimization', 'best-of-both-worlds', 'smoothed-online']
venue: "ICML 2024"
tldr: "This paper provides best-of-both-worlds guarantees for smoothed online quadratic optimization, achieving strong performance in both adversarial and stochastic settings."
---

# Best of Both Worlds Guarantees for Smoothed Online Quadratic Optimization

**Source**: [https://proceedings.mlr.press/v235/bhuyan24a.html](https://proceedings.mlr.press/v235/bhuyan24a.html)

**TLDR**: This paper provides best-of-both-worlds guarantees for smoothed online quadratic optimization, achieving strong performance in both adversarial and stochastic settings.

## Abstract

We study the smoothed online quadratic optimization (SOQO) problem where, at each round $t$, a player plays an action $x_t$ in response to a quadratic hitting cost and an additional squared $\ell_2$-norm cost for switching actions. This problem class has strong connections to a wide range of application domains including smart grid management, adaptive control, and data center management, where switching-efficient algorithms are highly sought after. We study the SOQO problem in both adversarial and stochastic settings, and in this process, perform the first stochastic analysis of this class of problems. We provide the online optimal algorithm when the minimizers of the hitting cost function evolve as a general stochastic process, which, for the case of martingale process, takes the form of a distribution-agnostic dynamic interpolation algorithm that we call Lazy Adaptive Interpolation (LAI). Next, we present the stochastic-adversarial trade-off by proving an $\Omega(T)$ expected regret for the adversarial optimal algorithm in the literature (ROBD) with respect to LAI and, a sub-optimal competitive ratio for LAI in the adversarial setting. Finally, we present a best-of-both-worlds algorithm that obtains a robust adversarial performance while simultaneously achieving a near-optimal stochastic performance.