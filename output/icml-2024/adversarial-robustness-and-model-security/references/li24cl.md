---
title: "Towards Optimal Adversarial Robust Q-learning with Bellman Infinity-error"
source: "https://proceedings.mlr.press/v235/li24cl.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24cl/li24cl.pdf"
categories: ['adversarial-robustness-and-model-security']
tags: ['adversarial-robustness', 'Q-learning', 'Bellman-error']
venue: "ICML 2024"
tldr: "This paper proposes an adversarially robust Q-learning approach using Bellman infinity-error to handle state-adversarial attacks in deep RL."
---

# Towards Optimal Adversarial Robust Q-learning with Bellman Infinity-error

**Source**: [https://proceedings.mlr.press/v235/li24cl.html](https://proceedings.mlr.press/v235/li24cl.html)

**TLDR**: This paper proposes an adversarially robust Q-learning approach using Bellman infinity-error to handle state-adversarial attacks in deep RL.

## Abstract

Establishing robust policies is essential to counter attacks or disturbances affecting deep reinforcement learning (DRL) agents. Recent studies explore state-adversarial robustness and suggest the potential lack of an optimal robust policy (ORP), posing challenges in setting strict robustness constraints. This work further investigates ORP: At first, we introduce a consistency assumption of policy (CAP) stating that optimal actions in the Markov decision process remain consistent with minor perturbations, supported by empirical and theoretical evidence. Building upon CAP, we crucially prove the existence of a deterministic and stationary ORP that aligns with the Bellman optimal policy. Furthermore, we illustrate the necessity of $L^{\infty}$-norm when minimizing Bellman error to attain ORP. This finding clarifies the vulnerability of prior DRL algorithms that target the Bellman optimal policy with $L^{1}$-norm and motivates us to train a Consistent Adversarial Robust Deep Q-Network (CAR-DQN) by minimizing a surrogate of Bellman Infinity-error. The top-tier performance of CAR-DQN across various benchmarks validates its practical effectiveness and reinforces the soundness of our theoretical analysis.