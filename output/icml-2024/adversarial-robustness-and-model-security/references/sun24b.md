---
title: "Breaking the Barrier: Enhanced Utility and Robustness in Smoothed DRL Agents"
source: "https://proceedings.mlr.press/v235/sun24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sun24b/sun24b.pdf"
categories: ['adversarial-robustness-and-model-security', 'online-learning-and-sequential-decision-making']
tags: ['deep-reinforcement-learning', 'randomized-smoothing', 'robustness', 'certified-defense', 'adversarial-robustness']
venue: "ICML 2024"
tldr: "An enhanced randomized smoothing approach for deep RL agents is proposed to simultaneously improve robustness and clean reward performance."
---

# Breaking the Barrier: Enhanced Utility and Robustness in Smoothed DRL Agents

**Source**: [https://proceedings.mlr.press/v235/sun24b.html](https://proceedings.mlr.press/v235/sun24b.html)

**TLDR**: An enhanced randomized smoothing approach for deep RL agents is proposed to simultaneously improve robustness and clean reward performance.

## Abstract

Robustness remains a paramount concern in deep reinforcement learning (DRL), with randomized smoothing emerging as a key technique for enhancing this attribute. However, a notable gap exists in the performance of current smoothed DRL agents, often characterized by significantly low clean rewards and weak robustness. In response to this challenge, our study introduces innovative algorithms aimed at training effective smoothed robust DRL agents. We propose S-DQN and S-PPO, novel approaches that demonstrate remarkable improvements in clean rewards, empirical robustness, and robustness guarantee across standard RL benchmarks. Notably, our S-DQN and S-PPO agents not only significantly outperform existing smoothed agents by an average factor of $2.16\times$ under the strongest attack, but also surpass previous robustly-trained agents by an average factor of $2.13\times$. This represents a significant leap forward in the field. Furthermore, we introduce Smoothed Attack, which is $1.89\times$ more effective in decreasing the rewards of smoothed agents than existing adversarial attacks. Our code is available at: https://github.com/Trustworthy-ML-Lab/Robust_HighUtil_Smoothed_DRL