---
title: "Optimal Batched Linear Bandits"
source: "https://proceedings.mlr.press/v235/ren24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ren24a/ren24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'online-learning-matching-market-algorithms']
tags: ['linear-bandits', 'batched-learning', 'minimax-optimal-regret', 'explore-exploit', 'online-learning']
venue: "ICML 2024"
tldr: "The E4 algorithm achieves minimax optimal regret for the batched linear bandit problem using only O(log log T) batches."
---

# Optimal Batched Linear Bandits

**Source**: [https://proceedings.mlr.press/v235/ren24a.html](https://proceedings.mlr.press/v235/ren24a.html)

**TLDR**: The E4 algorithm achieves minimax optimal regret for the batched linear bandit problem using only O(log log T) batches.

## Abstract

We introduce the E$^4$ algorithm for the batched linear bandit problem, incorporating an Explore-Estimate-Eliminate-Exploit framework. With a proper choice of exploration rate, we prove E$^4$ achieves the finite-time minimax optimal regret with only $O(\log\log T)$ batches, and the asymptotically optimal regret with only $3$ batches as $T\rightarrow\infty$, where $T$ is the time horizon. We further prove a lower bound on the batch complexity of liner contextual bandits showing that any asymptotically optimal algorithm must require at least $3$ batches in expectation as $T\rightarrow \infty$, which indicates E$^4$ achieves the asymptotic optimality in regret and batch complexity simultaneously. To the best of our knowledge, E$^4$ is the first algorithm for linear bandits that simultaneously achieves the minimax and asymptotic optimality in regret with the corresponding optimal batch complexities. In addition, we show that with another choice of exploration rate E$^4$ achieves an instance-dependent regret bound requiring at most $O(\log T)$ batches, and maintains the minimax optimality and asymptotic optimality. We conduct thorough experiments to evaluate our algorithm on randomly generated instances and the challenging End of Optimism instances (Lattimore & Szepesvari, 2017) which were shown to be hard to learn for optimism based algorithms. Empirical results show that E$^4$ consistently outperforms baseline algorithms with respect to regret minimization, batch complexity, and computational efficiency.