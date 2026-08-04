---
title: "Reward Model Learning vs. Direct Policy Optimization: A Comparative Analysis of Learning from Human Preferences"
source: "https://proceedings.mlr.press/v235/nika24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nika24a/nika24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'learning-with-imperfect-data-and-bias']
tags: ['RLHF', 'DPO', 'human-preferences']
venue: "ICML 2024"
tldr: "Systematically compares reinforcement learning from human feedback and direct preference optimization for learning from human preferences."
---

# Reward Model Learning vs. Direct Policy Optimization: A Comparative Analysis of Learning from Human Preferences

**Source**: [https://proceedings.mlr.press/v235/nika24a.html](https://proceedings.mlr.press/v235/nika24a.html)

**TLDR**: Systematically compares reinforcement learning from human feedback and direct preference optimization for learning from human preferences.

## Abstract

In this paper, we take a step towards a deeper understanding of learning from human preferences by systematically comparing the paradigm of reinforcement learning from human feedback (RLHF) with the recently proposed paradigm of direct preference optimization (DPO). We focus our attention on the class of loglinear policy parametrization and linear reward functions. In order to compare the two paradigms, we first derive minimax statistical bounds on the suboptimality gap induced by both RLHF and DPO, assuming access to an oracle that exactly solves the optimization problems. We provide a detailed discussion on the relative comparison between the two paradigms, simultaneously taking into account the sample size, policy and reward class dimensions, and the regularization temperature. Moreover, we extend our analysis to the approximate optimization setting and derive exponentially decaying convergence rates for both RLHF and DPO. Next, we analyze the setting where the ground-truth reward is not realizable and find that, while RLHF incurs a constant additional error, DPO retains its asymptotically decaying gap by just tuning the temperature accordingly. Finally, we extend our comparison to the Markov decision process setting, where we generalize our results with exact optimization. To the best of our knowledge, we are the first to provide such a comparative analysis for RLHF and DPO.