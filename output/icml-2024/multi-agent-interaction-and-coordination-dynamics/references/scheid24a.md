---
title: "Incentivized Learning in Principal-Agent Bandit Games"
source: "https://proceedings.mlr.press/v235/scheid24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/scheid24a/scheid24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['principal-agent', 'bandit', 'incentives', 'contract-design', 'online-learning']
venue: "ICML 2024"
tldr: "A repeated principal-agent bandit game is studied where the principal influences agent decisions through incentive contracts to align objectives despite misaligned goals."
---

# Incentivized Learning in Principal-Agent Bandit Games

**Source**: [https://proceedings.mlr.press/v235/scheid24a.html](https://proceedings.mlr.press/v235/scheid24a.html)

**TLDR**: A repeated principal-agent bandit game is studied where the principal influences agent decisions through incentive contracts to align objectives despite misaligned goals.

## Abstract

This work considers a repeated principal-agent bandit game, where the principal can only interact with her environment through the agent. The principal and the agent have misaligned objectives and the choice of action is only left to the agent. However, the principal can influence the agent’s decisions by offering incentives which add up to his rewards. The principal aims to iteratively learn an incentive policy to maximize her own total utility. This framework extends usual bandit problems and is motivated by several practical applications, such as healthcare or ecological taxation, where traditionally used mechanism design theories often overlook the learning aspect of the problem. We present nearly optimal (with respect to a horizon $T$) learning algorithms for the principal’s regret in both multi-armed and linear contextual settings. Finally, we support our theoretical guarantees through numerical experiments.