---
title: "PcLast: Discovering Plannable Continuous Latent States"
source: "https://proceedings.mlr.press/v235/koul24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/koul24a/koul24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'continual-learning-memory-plasticity']
tags: ['goal-conditioned-planning', 'latent-representations', 'reachability', 'continuous-states', 'reinforcement-learning']
venue: "ICML 2024"
tldr: "A method for discovering plannable continuous latent states that incorporates reachability constraints for improved goal-conditioned planning."
---

# PcLast: Discovering Plannable Continuous Latent States

**Source**: [https://proceedings.mlr.press/v235/koul24a.html](https://proceedings.mlr.press/v235/koul24a.html)

**TLDR**: A method for discovering plannable continuous latent states that incorporates reachability constraints for improved goal-conditioned planning.

## Abstract

Goal-conditioned planning benefits from learned low-dimensional representations of rich observations. While compact latent representations typically learned from variational autoencoders or inverse dynamics enable goal-conditioned decision making, they ignore state reachability, hampering their performance. In this paper, we learn a representation that associates reachable states together for effective planning and goal-conditioned policy learning. We first learn a latent representation with multi-step inverse dynamics (to remove distracting information), and then transform this representation to associate reachable states together in $\ell_2$ space. Our proposals are rigorously tested in various simulation testbeds. Numerical results in reward-based settings show significant improvements in sampling efficiency. Further, in reward-free settings this approach yields layered state abstractions that enable computationally efficient hierarchical planning for reaching ad hoc goals with zero additional samples.