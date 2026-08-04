---
title: "Optimistic Multi-Agent Policy Gradient"
source: "https://proceedings.mlr.press/v235/zhao24v.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhao24v/zhao24v.pdf"
categories: ['multi-agent-mdp-structure-and-dependencies']
tags: ['multi-agent-reinforcement-learning', 'relative-overgeneralization', 'policy-gradient', 'cooperative-learning']
venue: "ICML 2024"
tldr: "This paper proposes an optimistic multi-agent policy gradient method to address relative overgeneralization in cooperative multi-agent learning."
---

# Optimistic Multi-Agent Policy Gradient

**Source**: [https://proceedings.mlr.press/v235/zhao24v.html](https://proceedings.mlr.press/v235/zhao24v.html)

**TLDR**: This paper proposes an optimistic multi-agent policy gradient method to address relative overgeneralization in cooperative multi-agent learning.

## Abstract

Relative overgeneralization (RO) occurs in cooperative multi-agent learning tasks when agents converge towards a suboptimal joint policy due to overfitting to suboptimal behaviors of other agents. No methods have been proposed for addressing RO in multi-agent policy gradient (MAPG) methods although these methods produce state-of-the-art results. To address this gap, we propose a general, yet simple, framework to enable optimistic updates in MAPG methods that alleviate the RO problem. Our approach involves clipping the advantage to eliminate negative values, thereby facilitating optimistic updates in MAPG. The optimism prevents individual agents from quickly converging to a local optimum. Additionally, we provide a formal analysis to show that the proposed method retains optimality at a fixed point. In extensive evaluations on a diverse set of tasks including the Multi-agent MuJoCo and Overcooked benchmarks, our method outperforms strong baselines on 13 out of 19 tested tasks and matches the performance on the rest.