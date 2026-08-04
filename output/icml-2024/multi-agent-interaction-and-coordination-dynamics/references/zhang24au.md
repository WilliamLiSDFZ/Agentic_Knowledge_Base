---
title: "Sequential Asynchronous Action Coordination in Multi-Agent Systems: A Stackelberg Decision Transformer Approach"
source: "https://proceedings.mlr.press/v235/zhang24au.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24au/zhang24au.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'multi-agent-mdp-structure-and-dependencies']
tags: ['multi-agent-systems', 'stackelberg-game', 'transformer', 'asynchronous-coordination', 'reinforcement-learning']
venue: "ICML 2024"
tldr: "Proposes a Stackelberg Decision Transformer for scalable asynchronous action coordination in multi-agent systems modeled as Stackelberg games."
---

# Sequential Asynchronous Action Coordination in Multi-Agent Systems: A Stackelberg Decision Transformer Approach

**Source**: [https://proceedings.mlr.press/v235/zhang24au.html](https://proceedings.mlr.press/v235/zhang24au.html)

**TLDR**: Proposes a Stackelberg Decision Transformer for scalable asynchronous action coordination in multi-agent systems modeled as Stackelberg games.

## Abstract

Asynchronous action coordination presents a pervasive challenge in Multi-Agent Systems (MAS), which can be represented as a Stackelberg game (SG). However, the scalability of existing Multi-Agent Reinforcement Learning (MARL) methods based on SG is severely restricted by network architectures or environmental settings. To address this issue, we propose the Stackelberg Decision Transformer (STEER). It efficiently manages decision-making processes by incorporating the hierarchical decision structure of SG, the modeling capability of autoregressive sequence models, and the exploratory learning methodology of MARL. Our approach exhibits broad applicability across diverse task types and environmental configurations in MAS. Experimental results demonstrate both the convergence of our method towards Stackelberg equilibrium strategies and its superiority over strong baselines in complex scenarios.