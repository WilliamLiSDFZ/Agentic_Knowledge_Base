---
title: "ACPO: A Policy Optimization Algorithm for Average MDPs with Constraints"
source: "https://proceedings.mlr.press/v235/agnihotri24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/agnihotri24a/agnihotri24a.pdf"
categories: ['multi-agent-mdp-structure-and-dependencies']
tags: ['constrained-mdp', 'average-reward', 'policy-optimization', 'reinforcement-learning']
venue: "ICML 2024"
tldr: "Proposes ACPO, a policy optimization algorithm for average-reward constrained MDPs with provable guarantees."
---

# ACPO: A Policy Optimization Algorithm for Average MDPs with Constraints

**Source**: [https://proceedings.mlr.press/v235/agnihotri24a.html](https://proceedings.mlr.press/v235/agnihotri24a.html)

**TLDR**: Proposes ACPO, a policy optimization algorithm for average-reward constrained MDPs with provable guarantees.

## Abstract

Reinforcement Learning (RL) for constrained MDPs (CMDPs) is an increasingly important problem for various applications. Often, the average criterion is more suitable than the discounted criterion. Yet, RL for average-CMDPs (ACMDPs) remains a challenging problem. Algorithms designed for discounted constrained RL problems often do not perform well for the average CMDP setting. In this paper, we introduce a new policy optimization with function approximation algorithm for constrained MDPs with the average criterion. The Average-Constrained Policy Optimization (ACPO) algorithm is inspired by trust region-based policy optimization algorithms. We develop basic sensitivity theory for average CMDPs, and then use the corresponding bounds in the design of the algorithm. We provide theoretical guarantees on its performance, and through extensive experimental work in various challenging OpenAI Gym environments, show its superior empirical performance when compared to other state-of-the-art algorithms adapted for the ACMDPs.