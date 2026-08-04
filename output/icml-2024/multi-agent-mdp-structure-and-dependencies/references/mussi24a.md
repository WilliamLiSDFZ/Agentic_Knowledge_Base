---
title: "Factored-Reward Bandits with Intermediate Observations"
source: "https://proceedings.mlr.press/v235/mussi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mussi24a/mussi24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['bandits', 'factored-rewards', 'intermediate-observations', 'multi-action']
venue: "ICML 2024"
tldr: "Factored-Reward Bandits is introduced as a novel bandit setting where multiple actions each affect separate system components with observable intermediate effects."
---

# Factored-Reward Bandits with Intermediate Observations

**Source**: [https://proceedings.mlr.press/v235/mussi24a.html](https://proceedings.mlr.press/v235/mussi24a.html)

**TLDR**: Factored-Reward Bandits is introduced as a novel bandit setting where multiple actions each affect separate system components with observable intermediate effects.

## Abstract

In several real-world sequential decision problems, at every step, the learner is required to select different actions. Every action affects a specific part of the system and generates an observable intermediate effect. In this paper, we introduce the Factored-Reward Bandits (FRBs), a novel setting able to effectively capture and exploit the structure of this class of scenarios, where the reward is computed as the product of the action intermediate observations. We characterize the statistical complexity of the learning problem in the FRBs, by deriving worst-case and asymptotic instance-dependent regret lower bounds. Then, we devise and analyze two regret minimization algorithms. The former, F-UCB, is an anytime optimistic approach matching the worst-case lower bound (up to logarithmic factors) but fails to perform optimally from the instance-dependent perspective. The latter, F-Track, is a bound-tracking approach, that enjoys optimal asymptotic instance-dependent regret guarantees.