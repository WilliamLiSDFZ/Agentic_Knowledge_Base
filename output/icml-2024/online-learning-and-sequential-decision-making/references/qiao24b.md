---
title: "Near-Optimal Reinforcement Learning with Self-Play under Adaptivity Constraints"
source: "https://proceedings.mlr.press/v235/qiao24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/qiao24b/qiao24b.pdf"
categories: ['multi-agent-mdp-structure-and-dependencies', 'online-learning-and-sequential-decision-making']
tags: ['multi-agent-RL', 'zero-sum-games', 'adaptivity-constraints', 'self-play', 'Markov-games']
venue: "ICML 2024"
tldr: "Near-optimal MARL algorithms for two-player zero-sum Markov Games under constraints on the number of policy updates."
---

# Near-Optimal Reinforcement Learning with Self-Play under Adaptivity Constraints

**Source**: [https://proceedings.mlr.press/v235/qiao24b.html](https://proceedings.mlr.press/v235/qiao24b.html)

**TLDR**: Near-optimal MARL algorithms for two-player zero-sum Markov Games under constraints on the number of policy updates.

## Abstract

We study the problem of multi-agent reinforcement learning (MARL) with adaptivity constraints — a new problem motivated by real-world applications where deployments of new policies are costly and the number of policy updates must be minimized. For two-player zero-sum Markov Games, we design a (policy) elimination based algorithm that achieves a regret of $\widetilde{O}(\sqrt{H^3 S^2 ABK})$, while the batch complexity is only $O(H+\log\log K)$. In the above, $S$ denotes the number of states, $A,B$ are the number of actions for the two players respectively, $H$ is the horizon and $K$ is the number of episodes. Furthermore, we prove a batch complexity lower bound $\Omega(\frac{H}{\log_{A}K}+\log\log K)$ for all algorithms with $\widetilde{O}(\sqrt{K})$ regret bound, which matches our upper bound up to logarithmic factors. As a byproduct, our techniques naturally extend to learning bandit games and reward-free MARL within near optimal batch complexity. To the best of our knowledge, these are the first line of results towards understanding MARL with low adaptivity.