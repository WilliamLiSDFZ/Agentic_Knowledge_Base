---
title: "Online Learning in CMDPs: Handling Stochastic and Adversarial Constraints"
source: "https://proceedings.mlr.press/v235/stradi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/stradi24a/stradi24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['constrained-MDP', 'online-learning', 'regret-bounds', 'stochastic-constraints', 'adversarial-constraints']
venue: "ICML 2024"
tldr: "Online learning algorithms are developed for episodic CMDPs handling both stochastic and adversarial reward and constraint settings with provable regret bounds."
---

# Online Learning in CMDPs: Handling Stochastic and Adversarial Constraints

**Source**: [https://proceedings.mlr.press/v235/stradi24a.html](https://proceedings.mlr.press/v235/stradi24a.html)

**TLDR**: Online learning algorithms are developed for episodic CMDPs handling both stochastic and adversarial reward and constraint settings with provable regret bounds.

## Abstract

We study online learning in episodic constrained Markov decision processes (CMDPs), where the learner aims at collecting as much reward as possible over the episodes, while satisfying some long-term constraints during the learning process. Rewards and constraints can be selected either stochastically or adversarially, and the transition function is not known to the learner. While online learning in classical (unconstrained) MDPs has received considerable attention over the last years, the setting of CMDPs is still largely unexplored. This is surprising, since in real-world applications, such as, e.g., autonomous driving, automated bidding, and recommender systems, there are usually additional constraints and specifications that an agent has to obey during the learning process. In this paper, we provide the first best-of-both-worlds algorithm for CMDPs with long-term constraints, in the flavor of Balseiro et al. (2023). Our algorithm is capable of handling settings in which rewards and constraints are selected either stochastically or adversarially, without requiring any knowledge of the underling process. Moreover, our algorithm matches state-of-the-art regret and constraint violation bounds for settings in which constraints are selected stochastically, while it is the first to provide guarantees in the case in which they are chosen adversarially.