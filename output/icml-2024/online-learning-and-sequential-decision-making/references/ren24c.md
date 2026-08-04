---
title: "Hybrid Inverse Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/ren24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ren24c/ren24c.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['inverse-reinforcement-learning', 'imitation-learning', 'hybrid-IRL', 'expert-demonstrations', 'reward-learning']
venue: "ICML 2024"
tldr: "A hybrid inverse reinforcement learning framework is proposed that reduces the number of required expert demonstrations while mitigating error compounding."
---

# Hybrid Inverse Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/ren24c.html](https://proceedings.mlr.press/v235/ren24c.html)

**TLDR**: A hybrid inverse reinforcement learning framework is proposed that reduces the number of required expert demonstrations while mitigating error compounding.

## Abstract

The inverse reinforcement learning approach to imitation learning is a double-edged sword. On the one hand, it can enable learning from a smaller number of expert demonstrations with more robustness to error compounding than behavioral cloning approaches. On the other hand, it requires that the learner repeatedly solve a computationally expensive reinforcement learning (RL) problem. Often, much of this computation is wasted searching over policies very dissimilar to the expert’s. In this work, we propose using hybrid RL – training on a mixture of online and expert data – to curtail unnecessary exploration. Intuitively, the expert data focuses the learner on good states during training, which reduces the amount of exploration required to compute a strong policy. Notably, such an approach doesn’t need the ability to reset the learner to arbitrary states in the environment, a requirement of prior work in efficient inverse RL. More formally, we derive a reduction from inverse RL to expert-competitive RL (rather than globally optimal RL) that allows us to dramatically reduce interaction during the inner policy search loop while maintaining the benefits of the IRL approach. This allows us to derive both model-free and model-based hybrid inverse RL algorithms with strong policy performance guarantees. Empirically, we find that our approaches are significantly more sample efficient than standard inverse RL and several other baselines on a suite of continuous control tasks.