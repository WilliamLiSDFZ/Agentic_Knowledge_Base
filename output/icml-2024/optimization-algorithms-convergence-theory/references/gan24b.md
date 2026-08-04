---
title: "Reflective Policy Optimization"
source: "https://proceedings.mlr.press/v235/gan24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gan24b/gan24b.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['reinforcement-learning', 'policy-optimization', 'on-policy', 'sample-efficiency']
venue: "ICML 2024"
tldr: "Reflective Policy Optimization combines on-policy and off-policy data to improve sample efficiency over standard methods like PPO."
---

# Reflective Policy Optimization

**Source**: [https://proceedings.mlr.press/v235/gan24b.html](https://proceedings.mlr.press/v235/gan24b.html)

**TLDR**: Reflective Policy Optimization combines on-policy and off-policy data to improve sample efficiency over standard methods like PPO.

## Abstract

On-policy reinforcement learning methods, like Trust Region Policy Optimization (TRPO) and Proximal Policy Optimization (PPO), often demand extensive data per update, leading to sample inefficiency. This paper introduces Reflective Policy Optimization (RPO), a novel on-policy extension that amalgamates past and future state-action information for policy optimization. This approach empowers the agent for introspection, allowing modifications to its actions within the current state. Theoretical analysis confirms that policy performance is monotonically improved and contracts the solution space, consequently expediting the convergence procedure. Empirical results demonstrate RPO’s feasibility and efficacy in two reinforcement learning benchmarks, culminating in superior sample efficiency. The source code of this work is available at https://github.com/Edgargan/RPO.