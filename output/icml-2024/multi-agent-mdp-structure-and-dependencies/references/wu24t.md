---
title: "Minimally Modifying a Markov Game to Achieve Any Nash Equilibrium and Value"
source: "https://proceedings.mlr.press/v235/wu24t.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24t/wu24t.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'multi-agent-mdp-structure-and-dependencies']
tags: ['markov-games', 'nash-equilibrium', 'game-modification', 'reward-shaping', 'zero-sum-games']
venue: "ICML 2024"
tldr: "Studies minimal reward function modifications to zero-sum Markov games that make a target policy profile the unique Markov perfect Nash equilibrium within a desired value range."
---

# Minimally Modifying a Markov Game to Achieve Any Nash Equilibrium and Value

**Source**: [https://proceedings.mlr.press/v235/wu24t.html](https://proceedings.mlr.press/v235/wu24t.html)

**TLDR**: Studies minimal reward function modifications to zero-sum Markov games that make a target policy profile the unique Markov perfect Nash equilibrium within a desired value range.

## Abstract

We study the game modification problem, where a benevolent game designer or a malevolent adversary modifies the reward function of a zero-sum Markov game so that a target deterministic or stochastic policy profile becomes the unique Markov perfect Nash equilibrium and has a value within a target range, in a way that minimizes the modification cost. We characterize the set of policy profiles that can be installed as the unique equilibrium of a game and establish sufficient and necessary conditions for successful installation. We propose an efficient algorithm that solves a convex optimization problem with linear constraints and then performs random perturbation to obtain a modification plan with a near-optimal cost.