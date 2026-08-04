---
title: "Accelerated Policy Gradient: On the Convergence Rates of the Nesterov Momentum for Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/chen24t.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24t/chen24t.pdf"
categories: ['optimization-algorithms-convergence-theory', 'online-learning-and-sequential-decision-making']
tags: ['policy-gradient', 'Nesterov-momentum', 'reinforcement-learning', 'convergence-rates']
venue: "ICML 2024"
tldr: "Nesterov momentum-based acceleration is applied to policy gradient methods in RL with provable convergence rate improvements."
---

# Accelerated Policy Gradient: On the Convergence Rates of the Nesterov Momentum for Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/chen24t.html](https://proceedings.mlr.press/v235/chen24t.html)

**TLDR**: Nesterov momentum-based acceleration is applied to policy gradient methods in RL with provable convergence rate improvements.

## Abstract

Various acceleration approaches for Policy Gradient (PG) have been analyzed within the realm of Reinforcement Learning (RL). However, the theoretical understanding of the widely used momentum-based acceleration method on PG remains largely open. In response to this gap, we adapt the celebrated Nesterov’s accelerated gradient (NAG) method to policy optimization in RL, termed Accelerated Policy Gradient (APG). To demonstrate the potential of APG in achieving fast convergence, we formally prove that with the true gradient and under the softmax policy parametrization, APG converges to an optimal policy at rates: (i) $\tilde{O}(1/t^2)$ with nearly constant step sizes; (ii) $O(e^{-ct})$ with time-varying step sizes. To the best of our knowledge, this is the first characterization of the convergence rates of NAG in the context of RL. Notably, our analysis relies on one interesting finding: Regardless of the parameter initialization, APG ends up entering a locally nearly-concave regime, where APG can significantly benefit from the momentum, within finite iterations. Through numerical validation and experiments on the Atari 2600 benchmarks, we confirm that APG exhibits a $\tilde{O}(1/t^2)$ rate with nearly constant step sizes and a linear convergence rate with time-varying step sizes, significantly improving convergence over the standard PG.