---
title: "Causal Bandits: The Pareto Optimal Frontier of Adaptivity, a Reduction to Linear Bandits, and Limitations around Unknown Marginals"
source: "https://proceedings.mlr.press/v235/liu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24b/liu24b.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['causal-bandits', 'adaptivity', 'linear-bandits']
venue: "ICML 2024"
tldr: "This work characterizes the Pareto optimal frontier of adaptivity in causal bandit problems and reduces them to linear bandits while analyzing limitations around unknown marginals."
---

# Causal Bandits: The Pareto Optimal Frontier of Adaptivity, a Reduction to Linear Bandits, and Limitations around Unknown Marginals

**Source**: [https://proceedings.mlr.press/v235/liu24b.html](https://proceedings.mlr.press/v235/liu24b.html)

**TLDR**: This work characterizes the Pareto optimal frontier of adaptivity in causal bandit problems and reduces them to linear bandits while analyzing limitations around unknown marginals.

## Abstract

In this work, we investigate the problem of adapting to the presence or absence of causal structure in multi-armed bandit problems. In addition to the usual reward signal, we assume the learner has access to additional variables, observed in each round after acting. When these variables $d$-separate the action from the reward, existing work in causal bandits demonstrates that one can achieve strictly better (minimax) rates of regret (Lu et al., 2020). Our goal is to adapt to this favorable “conditionally benign” structure, if it is present in the environment, while simultaneously recovering worst-case minimax regret, if it is not. Notably, the learner has no prior knowledge of whether the favorable structure holds. In this paper, we establish the Pareto optimal frontier of adaptive rates. We prove upper and matching lower bounds on the possible trade-offs in the performance of learning in conditionally benign and arbitrary environments, resolving an open question raised by Bilodeau et al. (2022). Furthermore, we are the first to obtain instance-dependent bounds for causal bandits, by reducing the problem to the linear bandit setting. Finally, we examine the common assumption that the marginal distributions of the post-action contexts are known and show that a nontrivial estimate is necessary for better-than-worst-case minimax rates.