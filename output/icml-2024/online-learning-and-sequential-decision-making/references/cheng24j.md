---
title: "RICE: Breaking Through the Training Bottlenecks of Reinforcement Learning with Explanation"
source: "https://proceedings.mlr.press/v235/cheng24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cheng24j/cheng24j.pdf"
categories: ['online-learning-and-sequential-decision-making', 'ai-explainability-uncertainty-human-decision-making']
tags: ['deep-reinforcement-learning', 'explanation-guided-exploration', 'sparse-rewards']
venue: "ICML 2024"
tldr: "RICE leverages explanations to break training bottlenecks in deep reinforcement learning under sparse reward settings."
---

# RICE: Breaking Through the Training Bottlenecks of Reinforcement Learning with Explanation

**Source**: [https://proceedings.mlr.press/v235/cheng24j.html](https://proceedings.mlr.press/v235/cheng24j.html)

**TLDR**: RICE leverages explanations to break training bottlenecks in deep reinforcement learning under sparse reward settings.

## Abstract

Deep reinforcement learning (DRL) is playing an increasingly important role in real-world applications. However, obtaining an optimally performing DRL agent for complex tasks, especially with sparse rewards, remains a significant challenge. The training of a DRL agent can be often trapped in a bottleneck without further progress. In this paper, we propose RICE, an innovative refining scheme for reinforcement learning that incorporates explanation methods to break through the training bottlenecks. The high-level idea of RICE is to construct a new initial state distribution that combines both the default initial states and critical states identified through explanation methods, thereby encouraging the agent to explore from the mixed initial states. Through careful design, we can theoretically guarantee that our refining scheme has a tighter sub-optimality bound. We evaluate RICE in various popular RL environments and real-world applications. The results demonstrate that RICE significantly outperforms existing refining schemes in enhancing agent performance.