---
title: "Model-Free Robust $φ$-Divergence Reinforcement Learning Using Both Offline and Online Data"
source: "https://proceedings.mlr.press/v235/panaganti24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/panaganti24a/panaganti24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['robust-RL', 'phi-divergence', 'offline-online-learning', 'distributionally-robust']
venue: "ICML 2024"
tldr: "Develops a model-free robust reinforcement learning framework using phi-divergence that combines offline and online data to handle simulator-to-real-world mismatches."
---

# Model-Free Robust $φ$-Divergence Reinforcement Learning Using Both Offline and Online Data

**Source**: [https://proceedings.mlr.press/v235/panaganti24a.html](https://proceedings.mlr.press/v235/panaganti24a.html)

**TLDR**: Develops a model-free robust reinforcement learning framework using phi-divergence that combines offline and online data to handle simulator-to-real-world mismatches.

## Abstract

The robust $\phi$-regularized Markov Decision Process (RRMDP) framework focuses on designing control policies that are robust against parameter uncertainties due to mismatches between the simulator (nominal) model and real-world settings. This work makes two important contributions. First, we propose a model-free algorithm called Robust $\phi$-regularized fitted Q-iteration for learning an $\epsilon$-optimal robust policy that uses only the historical data collected by rolling out a behavior policy (with robust exploratory requirement) on the nominal model. To the best of our knowledge, we provide the first unified analysis for a class of $\phi$-divergences achieving robust optimal policies in high-dimensional systems of arbitrary large state space with general function approximation. Second, we introduce the hybrid robust $\phi$-regularized reinforcement learning framework to learn an optimal robust policy using both historical data and online sampling. Towards this framework, we propose a model-free algorithm called Hybrid robust Total-variation-regularized Q-iteration. To the best of our knowledge, we provide the first improved out-of-data-distribution assumption in large-scale problems of arbitrary large state space with general function approximation under the hybrid robust $\phi$-regularized reinforcement learning framework.