---
title: "Uncertainty-Aware Reward-Free Exploration with General Function Approximation"
source: "https://proceedings.mlr.press/v235/zhang24ci.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24ci/zhang24ci.pdf"
categories: ['online-learning-and-sequential-decision-making', 'difference-in-differences-based-policy-evaluation']
tags: ['unsupervised-RL', 'exploration', 'uncertainty-estimation']
venue: "ICML 2024"
tldr: "Proposes an uncertainty-aware reward-free exploration method for reinforcement learning with general function approximation."
---

# Uncertainty-Aware Reward-Free Exploration with General Function Approximation

**Source**: [https://proceedings.mlr.press/v235/zhang24ci.html](https://proceedings.mlr.press/v235/zhang24ci.html)

**TLDR**: Proposes an uncertainty-aware reward-free exploration method for reinforcement learning with general function approximation.

## Abstract

Mastering multiple tasks through exploration and learning in an environment poses a significant challenge in reinforcement learning (RL). Unsupervised RL has been introduced to address this challenge by training policies with intrinsic rewards rather than extrinsic rewards. However, current intrinsic reward designs and unsupervised RL algorithms often overlook the heterogeneous nature of collected samples, thereby diminishing their sample efficiency. To overcome this limitation, in this paper, we proposed a reward-free RL algorithm called GFA-RFE. The key idea behind our algorithm is an uncertainty-aware intrinsic reward for exploring the environment and an uncertainty-weighted learning process to handle heterogeneous uncertainty in different samples. Theoretically, we show that in order to find an $\epsilon$-optimal policy, GFA-RFE needs to collect $\tilde{O} (H^2 \log N_{\mathcal{F}} (\epsilon) \text{dim} (\mathcal{F}) / \epsilon^2 )$ number of episodes, where $\mathcal{F}$ is the value function class with covering number $N_{\mathcal{F}} (\epsilon)$ and generalized eluder dimension $\text{dim} (\mathcal{F})$. Such a result outperforms all existing reward-free RL algorithms. We further implement and evaluate GFA-RFE across various domains and tasks in the DeepMind Control Suite. Experiment results show that GFA-RFE outperforms or is comparable to the performance of state-of-the-art unsupervised RL algorithms.