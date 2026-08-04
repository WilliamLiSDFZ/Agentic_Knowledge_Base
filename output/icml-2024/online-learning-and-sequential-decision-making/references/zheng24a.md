---
title: "How Does Goal Relabeling Improve Sample Efficiency?"
source: "https://proceedings.mlr.press/v235/zheng24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zheng24a/zheng24a.pdf"
categories: ['online-learning-and-sequential-decision-making']
tags: ['hindsight-experience-replay', 'goal-relabeling', 'sample-efficiency', 'reinforcement-learning-theory']
venue: "ICML 2024"
tldr: "This paper provides a theoretical analysis of why hindsight experience replay and goal relabeling improve sample efficiency in reinforcement learning."
---

# How Does Goal Relabeling Improve Sample Efficiency?

**Source**: [https://proceedings.mlr.press/v235/zheng24a.html](https://proceedings.mlr.press/v235/zheng24a.html)

**TLDR**: This paper provides a theoretical analysis of why hindsight experience replay and goal relabeling improve sample efficiency in reinforcement learning.

## Abstract

Hindsight experience replay and goal relabeling are successful in reinforcement learning (RL) since they enable agents to learn from failures. Despite their successes, we lack a theoretical understanding, such as (i) why hindsight experience replay improves sample efficiency and (ii) how to design a relabeling method that achieves sample efficiency. To this end, we construct an example to show the information-theoretical improvement in sample efficiency achieved by goal relabeling. Our example reveals that goal relabeling can enhance sample efficiency and exploit the rich information in observations through better hypothesis elimination. Based on these insights, we develop an RL algorithm called GOALIVE. To analyze the sample complexity of GOALIVE, we introduce a complexity measure, the goal-conditioned Bellman-Eluder (GOAL-BE) dimension, which characterizes the sample complexity of goal-conditioned RL problems. Compared to the Bellman-Eluder dimension, the goal-conditioned version offers an exponential improvement in the best case. To the best of our knowledge, our work provides the first characterization of the theoretical improvement in sample efficiency achieved by goal relabeling.