---
title: "On the Role of Information Structure in Reinforcement Learning for Partially-Observable Sequential Teams and Games"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/0cbbdfb0a4098af8dc7a497a5e59aff7-Abstract-Conference.html"
categories: ['reinforcement-learning-optimization-and-decision-making']
tags: ['information-structure', 'partial-observability', 'sequential-games', 'reinforcement-learning', 'multi-agent']
venue: "NeurIPS 2024"
tldr: "A study of how information structure shapes reinforcement learning in partially observable sequential team and game settings."
---

# On the Role of Information Structure in Reinforcement Learning for Partially-Observable Sequential Teams and Games

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/0cbbdfb0a4098af8dc7a497a5e59aff7-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/0cbbdfb0a4098af8dc7a497a5e59aff7-Abstract-Conference.html)

**TLDR**: A study of how information structure shapes reinforcement learning in partially observable sequential team and game settings.

## Abstract

In sequential decision-making problems, the information structure describes the causal dependencies between system variables, encompassing the dynamics of the environment and the agents' actions. Classical models of reinforcement learning (e.g., MDPs, POMDPs) assume a restricted and highly regular information structure, while more general models like predictive state representations do not explicitly model the information structure. By contrast, real-world sequential decision-making problems typically involve a complex and time-varying interdependence of system variables, requiring a rich and flexible representation of information structure. In this paper, we formalize a novel reinforcement learning model which explicitly represents the information structure.We then use this model to carry out an information-structural analysis of the statistical complexity of general sequential decision-making problems, obtaining a characterization via a graph-theoretic quantity of the DAG representation of the information structure. We prove an upper bound on the sample complexity of learning a general sequential decision-making problem in terms of its information structure by exhibiting an algorithm achieving the upper bound. This recovers known tractability results and gives a novel perspective on reinforcement learning in general sequential decision-making problems, providing a systematic way of identifying new tractable classes of problems.