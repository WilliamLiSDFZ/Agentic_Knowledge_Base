---
title: "Chain-of-Thought Predictive Control"
source: "https://proceedings.mlr.press/v235/jia24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jia24c/jia24c.pdf"
categories: ['simulation-scaling-limits-for-robot-manipulation', 'online-learning-and-sequential-decision-making']
tags: ['hierarchical-imitation-learning', 'chain-of-thought', 'low-level-control', 'contact-rich-manipulation']
venue: "ICML 2024"
tldr: "A hierarchical imitation learning method uses chain-of-thought style predictive control to learn generalizable policies for complex low-level manipulation from sub-optimal demonstrations."
---

# Chain-of-Thought Predictive Control

**Source**: [https://proceedings.mlr.press/v235/jia24c.html](https://proceedings.mlr.press/v235/jia24c.html)

**TLDR**: A hierarchical imitation learning method uses chain-of-thought style predictive control to learn generalizable policies for complex low-level manipulation from sub-optimal demonstrations.

## Abstract

We study generalizable policy learning from demonstrations for complex low-level control (e.g., contact-rich object manipulations). We propose a novel hierarchical imitation learning method that utilizes sub-optimal demos. Firstly, we propose an observation space-agnostic approach that efficiently discovers the multi-step subskill decomposition of the demos in an unsupervised manner. By grouping temporarily close and functionally similar actions into subskill-level demo segments, the observations at the segment boundaries constitute a chain of planning steps for the task, which we refer to as the chain-of-thought (CoT). Next, we propose a Transformer-based design that effectively learns to predict the CoT as the subskill-level guidance. We couple action and subskill predictions via learnable prompt tokens and a hybrid masking strategy, which enable dynamically updated guidance at test time and improve feature representation of the trajectory for generalizable policy learning. Our method, Chain-of-Thought Predictive Control (CoTPC), consistently surpasses existing strong baselines on various challenging low-level manipulation tasks with sub-optimal demos. See project page at https://sites.google.com/view/cotpc.