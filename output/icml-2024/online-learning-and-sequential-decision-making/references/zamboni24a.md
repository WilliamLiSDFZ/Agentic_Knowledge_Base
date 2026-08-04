---
title: "How to Explore with Belief: State Entropy Maximization in POMDPs"
source: "https://proceedings.mlr.press/v235/zamboni24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zamboni24a/zamboni24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['state-entropy-maximization', 'POMDP', 'belief-state', 'exploration']
venue: "ICML 2024"
tldr: "Extends state entropy maximization for exploration to partially observable settings by planning over belief states in POMDPs."
---

# How to Explore with Belief: State Entropy Maximization in POMDPs

**Source**: [https://proceedings.mlr.press/v235/zamboni24a.html](https://proceedings.mlr.press/v235/zamboni24a.html)

**TLDR**: Extends state entropy maximization for exploration to partially observable settings by planning over belief states in POMDPs.

## Abstract

Recent works have studied state entropy maximization in reinforcement learning, in which the agent’s objective is to learn a policy inducing high entropy over states visitation (Hazan et al., 2019). They typically assume full observability of the state of the system, so that the entropy of the observations is maximized. In practice, the agent may only get partial observations, e.g., a robot perceiving the state of a physical space through proximity sensors and cameras. A significant mismatch between the entropy over observations and true states of the system can arise in those settings. In this paper, we address the problem of entropy maximization over the true states with a decision policy conditioned on partial observations only. The latter is a generalization of POMDPs, which is intractable in general. We develop a memory and computationally efficient policy gradient method to address a first-order relaxation of the objective defined on belief states, providing various formal characterizations of approximation gaps, the optimization landscape, and the hallucination problem. This paper aims to generalize state entropy maximization to more realistic domains that meet the challenges of applications.