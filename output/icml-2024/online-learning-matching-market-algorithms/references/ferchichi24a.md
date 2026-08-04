---
title: "Active Ranking and Matchmaking, with Perfect Matchings"
source: "https://proceedings.mlr.press/v235/ferchichi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ferchichi24a/ferchichi24a.pdf"
categories: ['online-learning-matching-market-algorithms']
tags: ['active-ranking', 'matchmaking', 'perfect-matchings']
venue: "ICML 2024"
tldr: "Addresses active ranking of players under noisy comparisons with the constraint that each iteration forms a perfect matching over all items."
---

# Active Ranking and Matchmaking, with Perfect Matchings

**Source**: [https://proceedings.mlr.press/v235/ferchichi24a.html](https://proceedings.mlr.press/v235/ferchichi24a.html)

**TLDR**: Addresses active ranking of players under noisy comparisons with the constraint that each iteration forms a perfect matching over all items.

## Abstract

We address the challenge of actively ranking a set of items/players with varying values/strengths. The comparison outcomes are random, with a greater noise the closer the values. A crucial requirement is that, at each iteration of the algorithm, all items must be compared once, i.e., an iteration is a perfect matching. Furthermore, we presume that comparing two players with closely matched strengths incurs no cost and, in contrast, a unit cost is associated with comparing players whose strength difference is more substantial. Our secondary objective is to determine an optimal matching between players based on this cost function: we propose and analyze an algorithm that draws on concepts from both AKS sorting networks and bandit theory. Our algorithm achieves both objectives with high probability, and the total cost is optimal (up to logarithmic terms).