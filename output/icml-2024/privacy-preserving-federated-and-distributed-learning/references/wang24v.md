---
title: "Momentum for the Win: Collaborative Federated Reinforcement Learning across Heterogeneous Environments"
source: "https://proceedings.mlr.press/v235/wang24v.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24v/wang24v.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'multi-agent-mdp-structure-and-dependencies']
tags: ['federated-reinforcement-learning', 'momentum', 'heterogeneous-environments', 'collaborative-learning', 'policy-gradient']
venue: "ICML 2024"
tldr: "A momentum-based federated reinforcement learning algorithm enables collaborative policy learning across agents in heterogeneous environments."
---

# Momentum for the Win: Collaborative Federated Reinforcement Learning across Heterogeneous Environments

**Source**: [https://proceedings.mlr.press/v235/wang24v.html](https://proceedings.mlr.press/v235/wang24v.html)

**TLDR**: A momentum-based federated reinforcement learning algorithm enables collaborative policy learning across agents in heterogeneous environments.

## Abstract

We explore a Federated Reinforcement Learning (FRL) problem where $N$ agents collaboratively learn a common policy without sharing their trajectory data. To date, existing FRL work has primarily focused on agents operating in the same or “similar" environments. In contrast, our problem setup allows for arbitrarily large levels of environment heterogeneity. To obtain the optimal policy which maximizes the average performance across all potentially completely different environments, we propose two algorithms: FedSVRPG-M and FedHAPG-M. In contrast to existing results, we demonstrate that both FedSVRPG-M and FedHAPG-M, both of which leverage momentum mechanisms, can exactly converge to a stationary point of the average performance function, regardless of the magnitude of environment heterogeneity. Furthermore, by incorporating the benefits of variance-reduction techniques or Hessian approximation, both algorithms achieve state-of-the-art convergence results, characterized by a sample complexity of $\mathcal{O}\left(\epsilon^{-\frac{3}{2}}/N\right)$. Notably, our algorithms enjoy linear convergence speedups with respect to the number of agents, highlighting the benefit of collaboration among agents in finding a common policy.