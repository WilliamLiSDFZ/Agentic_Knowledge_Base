---
title: "Bring Your Own (Non-Robust) Algorithm to Solve Robust MDPs by Estimating The Worst Kernel"
source: "https://proceedings.mlr.press/v235/gadot24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gadot24a/gadot24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['robust-MDPs', 'reinforcement-learning', 'worst-case-kernels', 'scalability']
venue: "ICML 2024"
tldr: "A framework that allows non-robust RL algorithms to solve Robust MDPs by estimating the worst-case transition kernel, enabling scaling to high-dimensional domains."
---

# Bring Your Own (Non-Robust) Algorithm to Solve Robust MDPs by Estimating The Worst Kernel

**Source**: [https://proceedings.mlr.press/v235/gadot24a.html](https://proceedings.mlr.press/v235/gadot24a.html)

**TLDR**: A framework that allows non-robust RL algorithms to solve Robust MDPs by estimating the worst-case transition kernel, enabling scaling to high-dimensional domains.

## Abstract

Robust Markov Decision Processes (RMDPs) provide a framework for sequential decision-making that is robust to perturbations on the transition kernel. However, current RMDP methods are often limited to small-scale problems, hindering their use in high-dimensional domains. To bridge this gap, we present EWoK, a novel online approach to solve RMDP that Estimates the Worst transition Kernel to learn robust policies. Unlike previous works that regularize the policy or value updates, EWoK achieves robustness by simulating the worst scenarios for the agent while retaining complete flexibility in the learning process. Notably, EWoK can be applied on top of any off-the-shelf non-robust RL algorithm, enabling easy scaling to high-dimensional domains. Our experiments, spanning from simple Cartpole to high-dimensional DeepMind Control Suite environments, demonstrate the effectiveness and applicability of the EWoK paradigm as a practical method for learning robust policies.