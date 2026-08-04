---
title: "Environment Design for Inverse Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/kleine-buening24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kleine-buening24a/kleine-buening24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['inverse-reinforcement-learning', 'environment-design', 'reward-learning', 'sample-efficiency']
venue: "ICML 2024"
tldr: "An environment design approach to improve sample efficiency and robustness of inverse reinforcement learning from demonstrations."
---

# Environment Design for Inverse Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/kleine-buening24a.html](https://proceedings.mlr.press/v235/kleine-buening24a.html)

**TLDR**: An environment design approach to improve sample efficiency and robustness of inverse reinforcement learning from demonstrations.

## Abstract

Learning a reward function from demonstrations suffers from low sample-efficiency. Even with abundant data, current inverse reinforcement learning methods that focus on learning from a single environment can fail to handle slight changes in the environment dynamics. We tackle these challenges through adaptive environment design. In our framework, the learner repeatedly interacts with the expert, with the former selecting environments to identify the reward function as quickly as possible from the expert’s demonstrations in said environments. This results in improvements in both sample-efficiency and robustness, as we show experimentally, for both exact and approximate inference.