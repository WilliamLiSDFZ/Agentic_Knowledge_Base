---
title: "Adaptively Learning to Select-Rank in Online Platforms"
source: "https://proceedings.mlr.press/v235/wang24l.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24l/wang24l.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'online-learning-matching-market-algorithms']
tags: ['ranking', 'online-learning', 'personalization', 'heterogeneous-users', 'recommendation']
venue: "ICML 2024"
tldr: "An adaptive select-rank algorithm for online platforms learns to personalize item rankings for heterogeneous users with provable regret guarantees."
---

# Adaptively Learning to Select-Rank in Online Platforms

**Source**: [https://proceedings.mlr.press/v235/wang24l.html](https://proceedings.mlr.press/v235/wang24l.html)

**TLDR**: An adaptive select-rank algorithm for online platforms learns to personalize item rankings for heterogeneous users with provable regret guarantees.

## Abstract

Ranking algorithms are fundamental to various online platforms across e-commerce sites to content streaming services. Our research addresses the challenge of adaptively ranking items from a candidate pool for heterogeneous users, a key component in personalizing user experience. We develop a user response model that considers diverse user preferences and the varying effects of item positions, aiming to optimize overall user satisfaction with the ranked list. We frame this problem within a contextual bandits framework, with each ranked list as an action. Our approach incorporates an upper confidence bound to adjust predicted user satisfaction scores and selects the ranking action that maximizes these adjusted scores, efficiently solved via maximum weight imperfect matching. We demonstrate that our algorithm achieves a cumulative regret bound of $O(d\sqrt{NKT})$ for ranking $K$ out of $N$ items in a $d$-dimensional context space over $T$ rounds, under the assumption that user responses follow a generalized linear model. This regret alleviates dependence on the ambient action space, whose cardinality grows exponentially with $N$ and $K$ (thus rendering direct application of existing adaptive learning algorithms – such as UCB or Thompson sampling – infeasible). Experiments conducted on both simulated and real-world datasets demonstrate our algorithm outperforms the baseline.