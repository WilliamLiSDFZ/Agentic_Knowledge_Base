---
title: "A Primal-Dual Algorithm for Offline Constrained Reinforcement Learning with Linear MDPs"
source: "https://proceedings.mlr.press/v235/hong24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hong24e/hong24e.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['offline-rl', 'constrained-mdp', 'linear-mdp', 'primal-dual', 'policy-optimization']
venue: "ICML 2024"
tldr: "Presents a primal-dual algorithm for offline constrained RL with linear MDPs that relaxes uniform data coverage requirements."
---

# A Primal-Dual Algorithm for Offline Constrained Reinforcement Learning with Linear MDPs

**Source**: [https://proceedings.mlr.press/v235/hong24e.html](https://proceedings.mlr.press/v235/hong24e.html)

**TLDR**: Presents a primal-dual algorithm for offline constrained RL with linear MDPs that relaxes uniform data coverage requirements.

## Abstract

We study offline reinforcement learning (RL) with linear MDPs under the infinite-horizon discounted setting which aims to learn a policy that maximizes the expected discounted cumulative reward using a pre-collected dataset. Existing algorithms for this setting either require a uniform data coverage assumptions or are computationally inefficient for finding an $\epsilon$-optimal policy with $\mathcal{O}(\epsilon^{-2})$ sample complexity. In this paper, we propose a primal dual algorithm for offline RL with linear MDPs in the infinite-horizon discounted setting. Our algorithm is the first computationally efficient algorithm in this setting that achieves sample complexity of $\mathcal{O}(\epsilon^{-2})$ with partial data coverage assumption. Our work is an improvement upon a recent work that requires $\mathcal{O}(\epsilon^{-4})$ samples. Moreover, we extend our algorithm to work in the offline constrained RL setting that enforces constraints on additional reward signals.