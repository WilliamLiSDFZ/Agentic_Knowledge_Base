---
title: "Mollification Effects of Policy Gradient Methods"
source: "https://proceedings.mlr.press/v235/wang24x.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24x/wang24x.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['policy-gradient', 'mollification', 'reinforcement-learning', 'non-smooth-optimization', 'continuous-control']
venue: "ICML 2024"
tldr: "A rigorous theoretical framework explains how policy gradient methods mollify non-smooth optimization landscapes in continuous control reinforcement learning."
---

# Mollification Effects of Policy Gradient Methods

**Source**: [https://proceedings.mlr.press/v235/wang24x.html](https://proceedings.mlr.press/v235/wang24x.html)

**TLDR**: A rigorous theoretical framework explains how policy gradient methods mollify non-smooth optimization landscapes in continuous control reinforcement learning.

## Abstract

Policy gradient methods have enabled deep reinforcement learning (RL) to approach challenging continuous control problems, even when the underlying systems involve highly nonlinear dynamics that generate complex non-smooth optimization landscapes. We develop a rigorous framework for understanding how policy gradient methods mollify non-smooth optimization landscapes to enable effective policy search, as well as the downside of it: while making the objective function smoother and easier to optimize, the stochastic objective deviates further from the original problem. We demonstrate the equivalence between policy gradient methods and solving backward heat equations. Following the ill-posedness of backward heat equations from PDE theory, we present a fundamental challenge to the use of policy gradient under stochasticity. Moreover, we make the connection between this limitation and the uncertainty principle in harmonic analysis to understand the effects of exploration with stochastic policies in RL. We also provide experimental results to illustrate both the positive and negative aspects of mollification effects in practice.