---
title: "On Interpolating Experts and Multi-Armed Bandits"
source: "https://proceedings.mlr.press/v235/chen24p.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24p/chen24p.pdf"
categories: ['online-learning-and-sequential-decision-making', 'online-learning-matching-market-algorithms']
tags: ['online-learning', 'expert-advice', 'multi-armed-bandits', 'interpolation']
venue: "ICML 2024"
tldr: "A unified framework interpolating between learning with expert advice and multi-armed bandits by controlling per-arm observable feedback."
---

# On Interpolating Experts and Multi-Armed Bandits

**Source**: [https://proceedings.mlr.press/v235/chen24p.html](https://proceedings.mlr.press/v235/chen24p.html)

**TLDR**: A unified framework interpolating between learning with expert advice and multi-armed bandits by controlling per-arm observable feedback.

## Abstract

Learning with expert advice and multi-armed bandit are two classic online decision problems which differ on how the information is observed in each round of the game. We study a family of problems interpolating the two. For a vector $\mathbf{m}=(m_1,…,m_K)\in \mathbb N^K$, an instance of $\mathbf m$-MAB indicates that the arms are partitioned into $K$ groups and the $i$-th group contains $m_i$ arms. Once an arm is pulled, the losses of all arms in the same group are observed. We prove tight minimax regret bounds for $\mathbf m$-MAB and design an optimal PAC algorithm for its pure exploration version, $\mathbf m$-BAI, where the goal is to identify the arm with minimum loss with as few rounds as possible. We show that the minimax regret of $\mathbf m$-MAB is $\Theta\left(\sqrt{T\sum_{k=1}^K\log (m_k+1)}\right)$ and the minimum number of pulls for an $(\varepsilon,0.05)$-PAC algorithm of $\mathbf m$-BAI is $\Theta\left(\frac{1}{\varepsilon^2}\cdot \sum_{k=1}^K\log (m_k+1)\right)$. Both our upper bounds and lower bounds for $\mathbf m$-MAB can be extended to a more general setting, namely the bandit with graph feedback, in terms of the clique cover and related graph parameters. As consequences, we obtained tight minimax regret bounds for several families of feedback graphs.