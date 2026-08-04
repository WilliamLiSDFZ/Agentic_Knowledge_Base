---
title: "Target Networks and Over-parameterization Stabilize Off-policy Bootstrapping with Function Approximation"
source: "https://proceedings.mlr.press/v235/che24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/che24a/che24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'online-learning-and-sequential-decision-making']
tags: ['target-networks', 'over-parameterization', 'off-policy-learning', 'TD-convergence']
venue: "ICML 2024"
tldr: "Combining target networks with over-parameterized linear function approximation provably stabilizes off-policy bootstrapped value estimation."
---

# Target Networks and Over-parameterization Stabilize Off-policy Bootstrapping with Function Approximation

**Source**: [https://proceedings.mlr.press/v235/che24a.html](https://proceedings.mlr.press/v235/che24a.html)

**TLDR**: Combining target networks with over-parameterized linear function approximation provably stabilizes off-policy bootstrapped value estimation.

## Abstract

We prove that the combination of a target network and over-parameterized linear function approximation establishes a weaker convergence condition for bootstrapped value estimation in certain cases, even with off-policy data. Our condition is naturally satisfied for expected updates over the entire state-action space or learning with a batch of complete trajectories from episodic Markov decision processes. Notably, using only a target network or an over-parameterized model does not provide such a convergence guarantee. Additionally, we extend our results to learning with truncated trajectories, showing that convergence is achievable for all tasks with minor modifications, akin to value truncation for the final states in trajectories. Our primary result focuses on temporal difference estimation for prediction, providing high-probability value estimation error bounds and empirical analysis on Baird’s counterexample and a Four-room task. Furthermore, we explore the control setting, demonstrating that similar convergence conditions apply to Q-learning.