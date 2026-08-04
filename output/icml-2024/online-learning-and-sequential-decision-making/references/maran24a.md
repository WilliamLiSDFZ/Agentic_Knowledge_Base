---
title: "No-Regret Reinforcement Learning in Smooth MDPs"
source: "https://proceedings.mlr.press/v235/maran24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/maran24a/maran24a.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['reinforcement-learning', 'continuous-state-spaces', 'no-regret']
venue: "ICML 2024"
tldr: "No-regret reinforcement learning guarantees for smooth MDPs with continuous state and action spaces."
---

# No-Regret Reinforcement Learning in Smooth MDPs

**Source**: [https://proceedings.mlr.press/v235/maran24a.html](https://proceedings.mlr.press/v235/maran24a.html)

**TLDR**: No-regret reinforcement learning guarantees for smooth MDPs with continuous state and action spaces.

## Abstract

Obtaining no-regret guarantees for reinforcement learning (RL) in the case of problems with continuous state and/or action spaces is still one of the major open challenges in the field. Recently, a variety of solutions have been proposed, but besides very specific settings, the general problem remains unsolved. In this paper, we introduce a novel structural assumption on the Markov decision processes (MDPs), namely $\nu-$smoothness, that generalizes most of the settings proposed so far (e.g., linear MDPs and Lipschitz MDPs). To face this challenging scenario, we propose two algorithms for regret minimization in $\nu-$smooth MDPs. Both algorithms build upon the idea of constructing an MDP representation through an orthogonal feature map based on Legendre polynomials. The first algorithm, Legendre-Eleanor, archives the no-regret property under weaker assumptions but is computationally inefficient, whereas the second one, Legendre-LSVI, runs in polynomial time, although for a smaller class of problems. After analyzing their regret properties, we compare our results with state-of-the-art ones from RL theory, showing that our algorithms achieve the best guarantees.