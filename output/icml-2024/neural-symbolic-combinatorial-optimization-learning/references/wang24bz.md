---
title: "A Hierarchical Adaptive Multi-Task Reinforcement Learning Framework for Multiplier Circuit Design"
source: "https://proceedings.mlr.press/v235/wang24bz.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24bz/wang24bz.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'multi-agent-mdp-structure-and-dependencies']
tags: ['multiplier-circuit-design', 'multi-task-reinforcement-learning', 'combinatorial-optimization', 'circuit-design']
venue: "ICML 2024"
tldr: "Presents a hierarchical adaptive multi-task RL framework for optimizing multiplier circuit designs across multiple conflicting objectives."
---

# A Hierarchical Adaptive Multi-Task Reinforcement Learning Framework for Multiplier Circuit Design

**Source**: [https://proceedings.mlr.press/v235/wang24bz.html](https://proceedings.mlr.press/v235/wang24bz.html)

**TLDR**: Presents a hierarchical adaptive multi-task RL framework for optimizing multiplier circuit designs across multiple conflicting objectives.

## Abstract

Multiplier design—which aims to explore a large combinatorial design space to simultaneously optimize multiple conflicting objectives—is a fundamental problem in the integrated circuits industry. Although traditional approaches tackle the multi-objective multiplier optimization problem by manually designed heuristics, reinforcement learning (RL) offers a promising approach to discover high-speed and area-efficient multipliers. However, the existing RL-based methods struggle to find Pareto-optimal circuit designs for all possible preferences, i.e., weights over objectives, in a sample-efficient manner. To address this challenge, we propose a novel hierarchical adaptive (HAVE) multi-task reinforcement learning framework. The hierarchical framework consists of a meta-agent to generate diverse multiplier preferences, and an adaptive multi-task agent to collaboratively optimize multipliers conditioned on the dynamic preferences given by the meta-agent. To the best of our knowledge, HAVE is the first to well approximate Pareto-optimal circuit designs for the entire preference space with high sample efficiency. Experiments on multipliers across a wide range of input widths demonstrate that HAVE significantly Pareto-dominates state-of-the-art approaches, achieving up to 28% larger hypervolume. Moreover, experiments demonstrate that multipliers designed by HAVE can well generalize to large-scale computation-intensive circuits.