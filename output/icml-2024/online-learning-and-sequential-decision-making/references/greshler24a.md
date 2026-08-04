---
title: "A Bayesian Approach to Online Planning"
source: "https://proceedings.mlr.press/v235/greshler24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/greshler24a/greshler24a.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'online-learning-and-sequential-decision-making']
tags: ['bayesian-planning', 'monte-carlo-tree-search', 'uncertainty-estimation']
venue: "ICML 2024"
tldr: "This paper proposes a Bayesian planning approach that incorporates uncertainty estimates over neural network outputs to improve Monte Carlo tree search."
---

# A Bayesian Approach to Online Planning

**Source**: [https://proceedings.mlr.press/v235/greshler24a.html](https://proceedings.mlr.press/v235/greshler24a.html)

**TLDR**: This paper proposes a Bayesian planning approach that incorporates uncertainty estimates over neural network outputs to improve Monte Carlo tree search.

## Abstract

The combination of Monte Carlo tree search and neural networks has revolutionized online planning. As neural network approximations are often imperfect, we ask whether uncertainty estimates about the network outputs could be used to improve planning. We develop a Bayesian planning approach that facilitates such uncertainty quantification, inspired by classical ideas from the meta-reasoning literature. We propose a Thompson sampling based algorithm for searching the tree of possible actions, for which we prove the first (to our knowledge) finite time Bayesian regret bound, and propose an efficient implementation for a restricted family of posterior distributions. In addition we propose a variant of the Bayes-UCB method applied to trees. Empirically, we demonstrate that on the ProcGen Maze and Leaper environments, when the uncertainty estimates are accurate but the neural network output is inaccurate, our Bayesian approach searches the tree much more effectively. In addition, we investigate whether popular uncertainty estimation methods are accurate enough to yield significant gains in planning.