---
title: "Exploration by Optimization with Hybrid Regularizers: Logarithmic Regret with Adversarial Robustness in Partial Monitoring"
source: "https://proceedings.mlr.press/v235/tsuchiya24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/tsuchiya24a/tsuchiya24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'adversarial-robustness-and-model-security']
tags: ['partial-monitoring', 'exploration-by-optimization', 'adversarial-robustness']
venue: "ICML 2024"
tldr: "Proposes hybrid regularizer-based exploration by optimization achieving logarithmic regret with adversarial robustness in partial monitoring."
---

# Exploration by Optimization with Hybrid Regularizers: Logarithmic Regret with Adversarial Robustness in Partial Monitoring

**Source**: [https://proceedings.mlr.press/v235/tsuchiya24a.html](https://proceedings.mlr.press/v235/tsuchiya24a.html)

**TLDR**: Proposes hybrid regularizer-based exploration by optimization achieving logarithmic regret with adversarial robustness in partial monitoring.

## Abstract

Partial monitoring is a generic framework of online decision-making problems with limited feedback. To make decisions from such limited feedback, it is necessary to find an appropriate distribution for exploration. Recently, a powerful approach for this purpose, exploration by optimization (ExO), was proposed, which achieves optimal bounds in adversarial environments with follow-the-regularized-leader for a wide range of online decision-making problems. However, a naive application of ExO in stochastic environments significantly degrades regret bounds. To resolve this issue in locally observable games, we first establish a new framework and analysis for ExO with a hybrid regularizer. This development allows us to significantly improve existing regret bounds of best-of-both-worlds (BOBW) algorithms, which achieves nearly optimal bounds both in stochastic and adversarial environments. In particular, we derive a stochastic regret bound of $O(\sum_{a \neq a^*} k^2 m^2 \log T / \Delta_a)$, where $k$, $m$, and $T$ are the numbers of actions, observations and rounds, $a^*$ is an optimal action, and $\Delta_a$ is the suboptimality gap for action $a$. This bound is roughly $\Theta(k^2 \log T)$ times smaller than existing BOBW bounds. In addition, for globally observable games, we provide a new BOBW algorithm with the first $O(\log T)$ stochastic bound.