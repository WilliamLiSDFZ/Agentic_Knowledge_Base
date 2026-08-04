---
title: "Random Latent Exploration for Deep Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/mahankali24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mahankali24a/mahankali24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'neural-network-learning-dynamics-theory']
tags: ['exploration', 'deep-reinforcement-learning', 'random-latent-space']
venue: "ICML 2024"
tldr: "Random Latent Exploration combines exploration bonuses and randomized value functions in latent space for efficient deep RL exploration."
---

# Random Latent Exploration for Deep Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/mahankali24a.html](https://proceedings.mlr.press/v235/mahankali24a.html)

**TLDR**: Random Latent Exploration combines exploration bonuses and randomized value functions in latent space for efficient deep RL exploration.

## Abstract

The ability to efficiently explore high-dimensional state spaces is essential for the practical success of deep Reinforcement Learning (RL). This paper introduces a new exploration technique called Random Latent Exploration (RLE), that combines the strengths of exploration bonuses and randomized value functions (two popular approaches for effective exploration in deep RL). RLE leverages the idea of perturbing rewards by adding structured random rewards to the original task rewards in certain (random) states of the environment, to encourage the agent to explore the environment during training. RLE is straightforward to implement and performs well in practice. To demonstrate the practical effectiveness of RLE, we evaluate it on the challenging Atari and IsaacGym benchmarks and show that RLE exhibits higher overall scores across all the tasks than other approaches, including action-noise and randomized value function exploration.