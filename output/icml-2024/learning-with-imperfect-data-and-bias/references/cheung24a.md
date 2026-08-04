---
title: "Leveraging (Biased) Information: Multi-armed Bandits with Offline Data"
source: "https://proceedings.mlr.press/v235/cheung24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cheung24a/cheung24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'learning-with-imperfect-data-and-bias']
tags: ['multi-armed-bandits', 'offline-data', 'biased-information']
venue: "ICML 2024"
tldr: "Offline data with potentially different distributions is leveraged to improve online multi-armed bandit learning with theoretical performance guarantees."
---

# Leveraging (Biased) Information: Multi-armed Bandits with Offline Data

**Source**: [https://proceedings.mlr.press/v235/cheung24a.html](https://proceedings.mlr.press/v235/cheung24a.html)

**TLDR**: Offline data with potentially different distributions is leveraged to improve online multi-armed bandit learning with theoretical performance guarantees.

## Abstract

We leverage offline data to facilitate online learning in stochastic multi-armed bandits. The probability distributions that govern the offline data and the online rewards can be different. Without any non-trival upper bound on their difference, we show that no non-anticipatory policy can out-perform the UCB policy by (Auer et al. 2002), even in the presence of offline data. In complement, we propose an online policy MIN-UCB, which outperforms UCB when a non-trivial upper bound is given. MIN-UCB adaptively chooses to utilize the offline data when they are deemed informative, and to ignore them otherwise. MIN-UCB is shown to be tight in terms of both instance indepedent and dependent regret bounds. Finally, we corroborate the theoretical results with numerical experiments.