---
title: "Quality-Diversity Actor-Critic: Learning High-Performing and Diverse Behaviors via Value and Successor Features Critics"
source: "https://proceedings.mlr.press/v235/grillotti24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/grillotti24a/grillotti24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['quality-diversity', 'reinforcement-learning', 'successor-features']
venue: "ICML 2024"
tldr: "Quality-Diversity Actor-Critic combines value and successor feature critics to learn diverse and high-performing behaviors in continuous control tasks."
---

# Quality-Diversity Actor-Critic: Learning High-Performing and Diverse Behaviors via Value and Successor Features Critics

**Source**: [https://proceedings.mlr.press/v235/grillotti24a.html](https://proceedings.mlr.press/v235/grillotti24a.html)

**TLDR**: Quality-Diversity Actor-Critic combines value and successor feature critics to learn diverse and high-performing behaviors in continuous control tasks.

## Abstract

A key aspect of intelligence is the ability to demonstrate a broad spectrum of behaviors for adapting to unexpected situations. Over the past decade, advancements in deep reinforcement learning have led to groundbreaking achievements to solve complex continuous control tasks. However, most approaches return only one solution specialized for a specific problem. We introduce Quality-Diversity Actor-Critic (QDAC), an off-policy actor-critic deep reinforcement learning algorithm that leverages a value function critic and a successor features critic to learn high-performing and diverse behaviors. In this framework, the actor optimizes an objective that seamlessly unifies both critics using constrained optimization to (1) maximize return, while (2) executing diverse skills. Compared with other Quality-Diversity methods, QDAC achieves significantly higher performance and more diverse behaviors on six challenging continuous control locomotion tasks. We also demonstrate that we can harness the learned skills to adapt better than other baselines to five perturbed environments. Finally, qualitative analyses showcase a range of remarkable behaviors: adaptive-intelligent-robotics.github.io/QDAC.