---
title: "Learning Coverage Paths in Unknown Environments with Deep Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/jonnarth24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jonnarth24a/jonnarth24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['coverage-path-planning', 'deep-reinforcement-learning', 'robotics', 'unknown-environments']
venue: "ICML 2024"
tldr: "Deep reinforcement learning is applied to online coverage path planning in unknown environments for robotic applications."
---

# Learning Coverage Paths in Unknown Environments with Deep Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/jonnarth24a.html](https://proceedings.mlr.press/v235/jonnarth24a.html)

**TLDR**: Deep reinforcement learning is applied to online coverage path planning in unknown environments for robotic applications.

## Abstract

Coverage path planning (CPP) is the problem of finding a path that covers the entire free space of a confined area, with applications ranging from robotic lawn mowing to search-and-rescue. When the environment is unknown, the path needs to be planned online while mapping the environment, which cannot be addressed by offline planning methods that do not allow for a flexible path space. We investigate how suitable reinforcement learning is for this challenging problem, and analyze the involved components required to efficiently learn coverage paths, such as action space, input feature representation, neural network architecture, and reward function. We propose a computationally feasible egocentric map representation based on frontiers, and a novel reward term based on total variation to promote complete coverage. Through extensive experiments, we show that our approach surpasses the performance of both previous RL-based approaches and highly specialized methods across multiple CPP variations.