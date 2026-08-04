---
title: "On the Unexpected Effectiveness of Reinforcement Learning for Sequential Recommendation"
source: "https://proceedings.mlr.press/v235/silva24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/silva24b/silva24b.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'online-learning-and-sequential-decision-making']
tags: ['reinforcement-learning', 'sequential-recommendation', 'next-item-prediction']
venue: "ICML 2024"
tldr: "Investigates why reinforcement learning unexpectedly improves sequential recommendation despite next-item prediction being a myopic evaluation task."
---

# On the Unexpected Effectiveness of Reinforcement Learning for Sequential Recommendation

**Source**: [https://proceedings.mlr.press/v235/silva24b.html](https://proceedings.mlr.press/v235/silva24b.html)

**TLDR**: Investigates why reinforcement learning unexpectedly improves sequential recommendation despite next-item prediction being a myopic evaluation task.

## Abstract

In recent years, Reinforcement Learning (RL) has shown great promise in session-based recommendation. Sequential models that use RL have reached state-of-the-art performance for the Next-item Prediction (NIP) task. This result is intriguing, as the NIP task only evaluates how well the system can correctly recommend the next item to the user, while the goal of RL is to find a policy that optimizes rewards in the long term – sometimes at the expense of suboptimal short-term performance. Then, how can RL improve the system’s performance on short-term metrics? This article investigates this question by exploring proxy learning objectives, which we identify as goals RL models might be following, and thus could explain the performance boost. We found that RL – when used as an auxiliary loss – promotes the learning of embeddings that capture information about the user’s previously interacted items. Subsequently, we replaced the RL objective with a straightforward auxiliary loss designed to predict the number of items the user interacted with. This substitution results in performance gains comparable to RL. These findings pave the way to improve performance and understanding of RL methods for recommender systems.