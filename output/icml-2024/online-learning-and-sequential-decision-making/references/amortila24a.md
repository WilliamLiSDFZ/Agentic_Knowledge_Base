---
title: "Scalable Online Exploration via Coverability"
source: "https://proceedings.mlr.press/v235/amortila24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/amortila24a/amortila24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'information-retrieval-and-recommendation-systems']
tags: ['reinforcement-learning', 'exploration', 'coverability']
venue: "ICML 2024"
tldr: "This paper proposes coverability-based exploration objectives to enable scalable online exploration for reward-agnostic downstream reinforcement learning."
---

# Scalable Online Exploration via Coverability

**Source**: [https://proceedings.mlr.press/v235/amortila24a.html](https://proceedings.mlr.press/v235/amortila24a.html)

**TLDR**: This paper proposes coverability-based exploration objectives to enable scalable online exploration for reward-agnostic downstream reinforcement learning.

## Abstract

Exploration is a major challenge in reinforcement learning, especially for high-dimensional domains that require function approximation. We propose exploration objectives—policy optimization objectives that enable downstream maximization of any reward function—as a conceptual framework to systematize the study of exploration. We introduce a new objective, L1-Coverage, which generalizes previous exploration schemes and supports three fundamental desiderata: 1. Intrinsic complexity control. L1-Coverage is associated with a structural parameter, L1-Coverability, which reflects the intrinsic statistical difficulty of the underlying MDP, subsuming Block and Low-Rank MDPs. 2. Efficient planning. For a known MDP, L1-Coverage efficiently reduces to standard policy optimization, allowing flexible integration with off-the-shelf methods such as policy gradient and Q-learning approaches. 3. Efficient exploration. L1-Coverage enables the first computationally efficient model-based and model-free algorithms for online (reward-free or reward-driven) reinforcement learning in MDPs with low coverability. Empirically, we find that L1-Coverage effectively drives off-the-shelf policy optimization algorithms to explore the state space.