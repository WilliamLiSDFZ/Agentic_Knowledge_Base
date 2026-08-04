---
title: "Roping in Uncertainty: Robustness and Regularization in Markov Games"
source: "https://proceedings.mlr.press/v235/mcmahan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mcmahan24a/mcmahan24a.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics']
tags: ['robust-Markov-games', 'Nash-equilibrium', 'regularization']
venue: "ICML 2024"
tldr: "Establishes equivalence between robust Nash equilibria in s-rectangular Markov games and Nash equilibria of regularized Markov games."
---

# Roping in Uncertainty: Robustness and Regularization in Markov Games

**Source**: [https://proceedings.mlr.press/v235/mcmahan24a.html](https://proceedings.mlr.press/v235/mcmahan24a.html)

**TLDR**: Establishes equivalence between robust Nash equilibria in s-rectangular Markov games and Nash equilibria of regularized Markov games.

## Abstract

We study robust Markov games (RMG) with $s$-rectangular uncertainty. We show a general equivalence between computing a robust Nash equilibrium (RNE) of a $s$-rectangular RMG and computing a Nash equilibrium (NE) of an appropriately constructed regularized MG. The equivalence result yields a planning algorithm for solving $s$-rectangular RMGs, as well as provable robustness guarantees for policies computed using regularized methods. However, we show that even for just reward-uncertain two-player zero-sum matrix games, computing an RNE is PPAD-hard. Consequently, we derive a special uncertainty structure called efficient player-decomposability and show that RNE for two-player zero-sum RMG in this class can be provably solved in polynomial time. This class includes commonly used uncertainty sets such as $L_1$ and $L_\infty$ ball uncertainty sets.