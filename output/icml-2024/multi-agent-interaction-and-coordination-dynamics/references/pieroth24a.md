---
title: "Detecting Influence Structures in Multi-Agent Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/pieroth24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pieroth24a/pieroth24a.pdf"
categories: ['multi-agent-mdp-structure-and-dependencies', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['multi-agent-RL', 'influence-measurement', 'interdependency']
venue: "ICML 2024"
tldr: "A framework for quantifying influence between agents in multi-agent reinforcement learning via total and state influence measurement functions."
---

# Detecting Influence Structures in Multi-Agent Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/pieroth24a.html](https://proceedings.mlr.press/v235/pieroth24a.html)

**TLDR**: A framework for quantifying influence between agents in multi-agent reinforcement learning via total and state influence measurement functions.

## Abstract

We consider the problem of quantifying the amount of influence one agent can exert on another in the setting of multi-agent reinforcement learning (MARL). As a step towards a unified approach to express agents’ interdependencies, we introduce the total and state influence measurement functions. Both of these are valid for all common MARL systems, such as the discounted reward setting. Additionally, we propose novel quantities, called the total impact measurement (TIM) and state impact measurement (SIM), that characterize one agent’s influence on another by the maximum impact it can have on the other agents’ expected returns and represent instances of impact measurement functions in the average reward setting. Furthermore, we provide approximation algorithms for TIM and SIM with simultaneously learning approximations of agents’ expected returns, error bounds, stability analyses under changes of the policies, and convergence guarantees. The approximation algorithm relies only on observing other agents’ actions and is, other than that, fully decentralized. Through empirical studies, we validate our approach’s effectiveness in identifying intricate influence structures in complex interactions. Our work appears to be the first study of determining influence structures in the multi-agent average reward setting with convergence guarantees.