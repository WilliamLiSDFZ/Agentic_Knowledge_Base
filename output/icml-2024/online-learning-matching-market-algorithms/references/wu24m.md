---
title: "Borda Regret Minimization for Generalized Linear Dueling Bandits"
source: "https://proceedings.mlr.press/v235/wu24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24m/wu24m.pdf"
categories: ['online-learning-and-sequential-decision-making', 'online-learning-matching-market-algorithms']
tags: ['dueling-bandits', 'borda-score', 'regret-minimization', 'generalized-linear-models', 'preference-feedback']
venue: "ICML 2024"
tldr: "Studies Borda regret minimization for generalized linear dueling bandits, identifying the highest Borda score item while minimizing cumulative regret."
---

# Borda Regret Minimization for Generalized Linear Dueling Bandits

**Source**: [https://proceedings.mlr.press/v235/wu24m.html](https://proceedings.mlr.press/v235/wu24m.html)

**TLDR**: Studies Borda regret minimization for generalized linear dueling bandits, identifying the highest Borda score item while minimizing cumulative regret.

## Abstract

Dueling bandits are widely used to model preferential feedback prevalent in many applications such as recommendation systems and ranking. In this paper, we study the Borda regret minimization problem for dueling bandits, which aims to identify the item with the highest Borda score while minimizing the cumulative regret. We propose a rich class of generalized linear dueling bandit models, which cover many existing models. We first prove a regret lower bound of order $\Omega(d^{2/3} T^{2/3})$ for the Borda regret minimization problem, where $d$ is the dimension of contextual vectors and $T$ is the time horizon. To attain this lower bound, we propose an explore-then-commit type algorithm for the stochastic setting, which has a nearly matching regret upper bound $\tilde{O}(d^{2/3} T^{2/3})$. We also propose an EXP3-type algorithm for the adversarial linear setting, where the underlying model parameter can change in each round. Our algorithm achieves an $\tilde{O}(d^{2/3} T^{2/3})$ regret, which is also optimal. Empirical evaluations on both synthetic data and a simulated real-world environment are conducted to corroborate our theoretical analysis.