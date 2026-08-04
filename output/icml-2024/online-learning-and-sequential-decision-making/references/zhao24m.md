---
title: "Is Inverse Reinforcement Learning Harder than Standard Reinforcement Learning? A Theoretical Perspective"
source: "https://proceedings.mlr.press/v235/zhao24m.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhao24m/zhao24m.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['inverse-reinforcement-learning', 'theoretical-analysis', 'sample-complexity']
venue: "ICML 2024"
tldr: "This paper provides a theoretical comparison of the computational and statistical hardness of inverse reinforcement learning versus standard reinforcement learning."
---

# Is Inverse Reinforcement Learning Harder than Standard Reinforcement Learning? A Theoretical Perspective

**Source**: [https://proceedings.mlr.press/v235/zhao24m.html](https://proceedings.mlr.press/v235/zhao24m.html)

**TLDR**: This paper provides a theoretical comparison of the computational and statistical hardness of inverse reinforcement learning versus standard reinforcement learning.

## Abstract

Inverse Reinforcement Learning (IRL)—the problem of learning reward functions from demonstrations of an expert policy—plays a critical role in developing intelligent systems. While widely used in applications, theoretical understandings of IRL present unique challenges and remain less developed compared with standard RL. For example, it remains open how to do IRL efficiently in standard offline settings with pre-collected data, where states are obtained from a behavior policy (which could be the expert policy itself), and actions are sampled from the expert policy. This paper provides the first line of results for efficient IRL in vanilla offline and online settings using polynomial samples and runtime. Our algorithms and analyses seamlessly adapt the pessimism principle commonly used in offline RL, and achieve IRL guarantees in stronger metrics than considered in existing work. We provide lower bounds showing that our sample complexities are nearly optimal. As an application, we also show that the learned rewards can transfer to another target MDP with suitable guarantees when the target MDP satisfies certain similarity assumptions with the original (source) MDP.