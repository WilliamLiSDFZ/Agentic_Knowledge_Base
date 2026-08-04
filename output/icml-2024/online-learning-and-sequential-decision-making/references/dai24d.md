---
title: "Safe Reinforcement Learning using Finite-Horizon Gradient-based Estimation"
source: "https://proceedings.mlr.press/v235/dai24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dai24d/dai24d.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['safe-reinforcement-learning', 'finite-horizon', 'gradient-estimation', 'policy-optimization', 'constraint-satisfaction']
venue: "ICML 2024"
tldr: "Proposes a finite-horizon gradient-based estimation method for constraint conditions in Safe RL to improve safe policy updates over the existing infinite-horizon advantage-based approach."
---

# Safe Reinforcement Learning using Finite-Horizon Gradient-based Estimation

**Source**: [https://proceedings.mlr.press/v235/dai24d.html](https://proceedings.mlr.press/v235/dai24d.html)

**TLDR**: Proposes a finite-horizon gradient-based estimation method for constraint conditions in Safe RL to improve safe policy updates over the existing infinite-horizon advantage-based approach.

## Abstract

A key aspect of Safe Reinforcement Learning (Safe RL) involves estimating the constraint condition for the next policy, which is crucial for guiding the optimization of safe policy updates. However, the existing Advantage-based Estimation (ABE) method relies on the infinite-horizon discounted advantage function. This dependence leads to catastrophic errors in finite-horizon scenarios with non-discounted constraints, resulting in safety-violation updates. In response, we propose the first estimation method for finite-horizon non-discounted constraints in deep Safe RL, termed Gradient-based Estimation (GBE), which relies on the analytic gradient derived along trajectories. Our theoretical and empirical analyses demonstrate that GBE can effectively estimate constraint changes over a finite horizon. Constructing a surrogate optimization problem with GBE, we developed a novel Safe RL algorithm called Constrained Gradient-based Policy Optimization (CGPO). CGPO identifies feasible optimal policies by iteratively resolving sub-problems within trust regions. Our empirical results reveal that CGPO, unlike baseline algorithms, successfully estimates the constraint functions of subsequent policies, thereby ensuring the efficiency and feasibility of each update.