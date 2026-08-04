---
title: "Geometric Active Exploration in Markov Decision Processes: the Benefit of Abstraction"
source: "https://proceedings.mlr.press/v235/de-santi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/de-santi24a/de-santi24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['active-exploration', 'reinforcement-learning', 'Markov-decision-processes', 'state-abstraction', 'experiment-design']
venue: "ICML 2024"
tldr: "Shows that state abstraction in Markov decision processes provides provable benefits for active exploration and experiment design via convex RL formulations."
---

# Geometric Active Exploration in Markov Decision Processes: the Benefit of Abstraction

**Source**: [https://proceedings.mlr.press/v235/de-santi24a.html](https://proceedings.mlr.press/v235/de-santi24a.html)

**TLDR**: Shows that state abstraction in Markov decision processes provides provable benefits for active exploration and experiment design via convex RL formulations.

## Abstract

How can a scientist use a Reinforcement Learning (RL) algorithm to design experiments over a dynamical system’s state space? In the case of finite and Markovian systems, an area called Active Exploration (AE) relaxes the optimization problem of experiments design into Convex RL, a generalization of RL admitting a wider notion of reward. Unfortunately, this framework is currently not scalable and the potential of AE is hindered by the vastness of experiments spaces typical of scientific discovery applications. However, these spaces are often endowed with natural geometries, e.g., permutation invariance in molecular design, that an agent could leverage to improve the statistical and computational efficiency of AE. To achieve this, we bridge AE and MDP homomorphisms, which offer a way to exploit known geometric structures via abstraction. Towards this goal, we make two fundamental contributions: we extend MDP homomorphisms formalism to Convex RL, and we present, to the best of our knowledge, the first analysis that formally captures the benefit of abstraction via homomorphisms on sample efficiency. Ultimately, we propose the Geometric Active Exploration (GAE) algorithm, which we analyse theoretically and experimentally in environments motivated by problems in scientific discovery.