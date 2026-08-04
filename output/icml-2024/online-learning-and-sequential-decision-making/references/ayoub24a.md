---
title: "Switching the Loss Reduces the Cost in Batch Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/ayoub24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ayoub24a/ayoub24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['fitted-Q-iteration', 'log-loss', 'batch-RL', 'cost-sensitive-learning', 'sample-efficiency']
venue: "ICML 2024"
tldr: "Shows that using log-loss in fitted Q-iteration yields sample complexity scaling with optimal policy cost, improving efficiency in batch RL."
---

# Switching the Loss Reduces the Cost in Batch Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/ayoub24a.html](https://proceedings.mlr.press/v235/ayoub24a.html)

**TLDR**: Shows that using log-loss in fitted Q-iteration yields sample complexity scaling with optimal policy cost, improving efficiency in batch RL.

## Abstract

We propose training fitted Q-iteration with log-loss (FQI-LOG) for batch reinforcement learning (RL). We show that the number of samples needed to learn a near-optimal policy with FQI-LOG scales with the accumulated cost of the optimal policy, which is zero in problems where acting optimally achieves the goal and incurs no cost. In doing so, we provide a general framework for proving small-cost bounds, i.e. bounds that scale with the optimal achievable cost, in batch RL. Moreover, we empirically verify that FQI-LOG uses fewer samples than FQI trained with squared loss on problems where the optimal policy reliably achieves the goal.