---
title: "Scalable Safe Policy Improvement for Factored Multi-Agent MDPs"
source: "https://proceedings.mlr.press/v235/bianchi24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bianchi24b/bianchi24b.pdf"
categories: ['multi-agent-mdp-structure-and-dependencies', 'online-learning-and-sequential-decision-making']
tags: ['safe-policy-improvement', 'multi-agent-MDP', 'factored-MDPs', 'Monte-Carlo-tree-search']
venue: "ICML 2024"
tldr: "This paper proposes scalable safe policy improvement methods for factored multi-agent MDPs using Monte Carlo Tree Search with baseline bootstrapping."
---

# Scalable Safe Policy Improvement for Factored Multi-Agent MDPs

**Source**: [https://proceedings.mlr.press/v235/bianchi24b.html](https://proceedings.mlr.press/v235/bianchi24b.html)

**TLDR**: This paper proposes scalable safe policy improvement methods for factored multi-agent MDPs using Monte Carlo Tree Search with baseline bootstrapping.

## Abstract

In this work, we focus on safe policy improvement in multi-agent domains where current state-of-the-art methods cannot be effectively applied because of large state and action spaces. We consider recent results using Monte Carlo Tree Search for Safe Policy Improvement with Baseline Bootstrapping and propose a novel algorithm that scales this approach to multi-agent domains, exploiting the factorization of the transition model and value function. Given a centralized behavior policy and a dataset of trajectories, our algorithm generates an improved policy by selecting joint actions using a novel extension of Max-Plus (or Variable Elimination) that constrains local actions to guarantee safety criteria. An empirical evaluation on multi-agent SysAdmin and multi-UAV Delivery shows that the approach scales to very large domains where state-of-the-art methods cannot work.