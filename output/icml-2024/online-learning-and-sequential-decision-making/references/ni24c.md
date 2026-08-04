---
title: "Risk-Sensitive Reward-Free Reinforcement Learning with CVaR"
source: "https://proceedings.mlr.press/v235/ni24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ni24c/ni24c.pdf"
categories: ['online-learning-and-sequential-decision-making', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['risk-sensitive-RL', 'CVaR', 'reward-free-exploration']
venue: "ICML 2024"
tldr: "Extends reward-free reinforcement learning to risk-sensitive settings using CVaR to handle safety-critical applications."
---

# Risk-Sensitive Reward-Free Reinforcement Learning with CVaR

**Source**: [https://proceedings.mlr.press/v235/ni24c.html](https://proceedings.mlr.press/v235/ni24c.html)

**TLDR**: Extends reward-free reinforcement learning to risk-sensitive settings using CVaR to handle safety-critical applications.

## Abstract

Exploration is a crucial phase in reinforcement learning (RL). The reward-free RL paradigm, as explored by (Jin et al., 2020), offers an efficient method to design exploration algorithms for risk-neutral RL across various reward functions with a single exploration phase. However, as RL applications in safety critical settings grow, there’s an increasing need for risk-sensitive RL, which considers potential risks in decision-making. Yet, efficient exploration strategies for risk-sensitive RL remain underdeveloped. This study presents a novel risk-sensitive reward-free framework based on Conditional Value-at-Risk (CVaR), designed to effectively address CVaR RL for any given reward function through a single exploration phase. We introduce the CVaR-RF-UCRL algorithm, which is shown to be $(\epsilon,p)$-PAC, with a sample complexity upper bounded by $\tilde{\mathcal{O}}\left(\frac{S^2AH^4}{\epsilon^2\tau^2}\right)$ with $\tau$ being the risk tolerance parameter. We also prove a $\Omega\left(\frac{S^2AH^2}{\epsilon^2\tau}\right)$ lower bound for any CVaR-RF exploration algorithm, demonstrating the near-optimality of our algorithm. Additionally, we propose the planning algorithms: CVaR-VI and its more practical variant, CVaR-VI-DISC. The effectiveness and practicality of our CVaR reward-free approach are further validated through numerical experiments.