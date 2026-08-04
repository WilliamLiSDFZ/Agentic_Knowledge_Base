---
title: "OMPO: A Unified Framework for RL under Policy and Dynamics Shifts"
source: "https://proceedings.mlr.press/v235/luo24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/luo24d/luo24d.pdf"
categories: ['online-learning-and-sequential-decision-making', 'large-language-model-alignment-and-capabilities']
tags: ['reinforcement-learning', 'distribution-shift', 'policy-adaptation', 'dynamics-shift']
venue: "ICML 2024"
tldr: "OMPO is a unified framework that addresses distribution discrepancies caused by policy and dynamics shifts in reinforcement learning."
---

# OMPO: A Unified Framework for RL under Policy and Dynamics Shifts

**Source**: [https://proceedings.mlr.press/v235/luo24d.html](https://proceedings.mlr.press/v235/luo24d.html)

**TLDR**: OMPO is a unified framework that addresses distribution discrepancies caused by policy and dynamics shifts in reinforcement learning.

## Abstract

Training reinforcement learning policies using environment interaction data collected from varying policies or dynamics presents a fundamental challenge. Existing works often overlook the distribution discrepancies induced by policy or dynamics shifts, or rely on specialized algorithms with task priors, thus often resulting in suboptimal policy performances and high learning variances. In this paper, we identify a unified strategy for online RL policy learning under diverse settings of policy and dynamics shifts: transition occupancy matching. In light of this, we introduce a surrogate policy learning objective by considering the transition occupancy discrepancies and then cast it into a tractable min-max optimization problem through dual reformulation. Our method, dubbed Occupancy-Matching Policy Optimization (OMPO), features a specialized actor-critic structure equipped with a distribution discriminator and a small-size local buffer. We conduct extensive experiments based on the OpenAI Gym, Meta-World, and Panda Robots environments, encompassing policy shifts under stationary and non-stationary dynamics, as well as domain adaption. The results demonstrate that OMPO outperforms the specialized baselines from different categories in all settings. We also find that OMPO exhibits particularly strong performance when combined with domain randomization, highlighting its potential in RL-based robotics applications.