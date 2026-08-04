---
title: "Online Matching with Stochastic Rewards: Provable Better Bound via Adversarial Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/zhang24bf.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24bf/zhang24bf.pdf"
categories: ['online-learning-matching-market-algorithms', 'online-learning-and-sequential-decision-making']
tags: ['online-bipartite-matching', 'adversarial-reinforcement-learning', 'competitive-ratio', 'stochastic-rewards', 'online-optimization']
venue: "ICML 2024"
tldr: "Uses adversarial reinforcement learning to derive provably better competitive ratio bounds for online bipartite matching with stochastic rewards."
---

# Online Matching with Stochastic Rewards: Provable Better Bound via Adversarial Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/zhang24bf.html](https://proceedings.mlr.press/v235/zhang24bf.html)

**TLDR**: Uses adversarial reinforcement learning to derive provably better competitive ratio bounds for online bipartite matching with stochastic rewards.

## Abstract

For a specific online optimization problem, for example, online bipartite matching (OBM), research efforts could be made in two directions before it is finally closed, i.e., the optimal competitive online algorithm is found. One is to continuously design algorithms with better performance. To this end, reinforcement learning (RL) has demonstrated great success in literature. However, little is known on the other direction: whether RL helps explore how hard an online problem is. In this paper, we study a generalized model of OBM, named online matching with stochastic rewards (OMSR, FOCS 2012), for which the optimal competitive ratio is still unknown. We adopt an adversarial RL approach that trains two RL agents adversarially and iteratively: the algorithm agent learns for algorithms with larger competitive ratios, while the adversarial agent learns to produce a family of hard instances. Through such a framework, agents converge at the end with a robust algorithm, which empirically outperforms the state of the art (STOC 2020). Much more significantly, it allows to track how the hard instances are generated. We succeed in distilling two structural properties from the learned graph patterns, which remarkably reduce the action space, and further enable theoretical improvement on the best-known hardness result of OMSR, from $0.621$ (FOCS 2012) to $0.597$. To the best of our knowledge, this gives the first evidence that RL can help enhance the theoretical understanding of an online problem.