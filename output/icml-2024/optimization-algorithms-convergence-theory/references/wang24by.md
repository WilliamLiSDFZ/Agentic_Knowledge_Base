---
title: "Non-Asymptotic Analysis for Single-Loop (Natural) Actor-Critic with Compatible Function Approximation"
source: "https://proceedings.mlr.press/v235/wang24by.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24by/wang24by.pdf"
categories: ['online-learning-and-sequential-decision-making', 'optimization-algorithms-convergence-theory']
tags: ['actor-critic', 'natural-policy-gradient', 'function-approximation', 'non-asymptotic-analysis']
venue: "ICML 2024"
tldr: "Provides non-asymptotic convergence analysis for single-loop actor-critic with compatible function approximation in reinforcement learning."
---

# Non-Asymptotic Analysis for Single-Loop (Natural) Actor-Critic with Compatible Function Approximation

**Source**: [https://proceedings.mlr.press/v235/wang24by.html](https://proceedings.mlr.press/v235/wang24by.html)

**TLDR**: Provides non-asymptotic convergence analysis for single-loop actor-critic with compatible function approximation in reinforcement learning.

## Abstract

Actor-critic (AC) is a powerful method for learning an optimal policy in reinforcement learning, where the critic uses algorithms, e.g., temporal difference (TD) learning with function approximation, to evaluate the current policy and the actor updates the policy along an approximate gradient direction using information from the critic. This paper provides the tightest non-asymptotic convergence bounds for both the AC and natural AC (NAC) algorithms. Specifically, existing studies show that AC converges to an $\epsilon+\varepsilon_{\text{critic}}$ neighborhood of stationary points with the best known sample complexity of $\mathcal{O}(\epsilon^{-2})$ (up to a log factor), and NAC converges to an $\epsilon+\varepsilon_{\text{critic}}+\sqrt{\varepsilon_{\text{actor}}}$ neighborhood of the global optimum with the best known sample complexity of $\mathcal{O}(\epsilon^{-3})$, where $\varepsilon_{\text{critic}}$ is the approximation error of the critic and $\varepsilon_{\text{actor}}$ is the approximation error induced by the insufficient expressive power of the parameterized policy class. This paper analyzes the convergence of both AC and NAC algorithms with compatible function approximation. Our analysis eliminates the term $\varepsilon_{\text{critic}}$ from the error bounds while still achieving the best known sample complexities. Moreover, we focus on the challenging single-loop setting with a single Markovian sample trajectory. Our major technical novelty lies in analyzing the stochastic bias due to policy-dependent and time-varying compatible function approximation in the critic, and handling the non-ergodicity of the MDP due to the single Markovian sample trajectory. Numerical results are also provided in the appendix.