---
title: "Adaptively Perturbed Mirror Descent for Learning in Games"
source: "https://proceedings.mlr.press/v235/abe24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/abe24a/abe24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['mirror-descent', 'game-theory', 'payoff-perturbation', 'noise-robustness']
venue: "ICML 2024"
tldr: "Proposes adaptive payoff perturbation for Mirror Descent in monotone games to achieve convergence under noisy gradient conditions."
---

# Adaptively Perturbed Mirror Descent for Learning in Games

**Source**: [https://proceedings.mlr.press/v235/abe24a.html](https://proceedings.mlr.press/v235/abe24a.html)

**TLDR**: Proposes adaptive payoff perturbation for Mirror Descent in monotone games to achieve convergence under noisy gradient conditions.

## Abstract

This paper proposes a payoff perturbation technique for the Mirror Descent (MD) algorithm in games where the gradient of the payoff functions is monotone in the strategy profile space, potentially containing additive noise. The optimistic family of learning algorithms, exemplified by optimistic MD, successfully achieves last-iterate convergence in scenarios devoid of noise, leading the dynamics to a Nash equilibrium. A recent re-emerging trend underscores the promise of the perturbation approach, where payoff functions are perturbed based on the distance from an anchoring, or slingshot, strategy. In response, we propose Adaptively Perturbed MD (APMD), which adjusts the magnitude of the perturbation by repeatedly updating the slingshot strategy at a predefined interval. This innovation empowers us to find a Nash equilibrium of the underlying game with guaranteed rates. Empirical demonstrations affirm that our algorithm exhibits significantly accelerated convergence.