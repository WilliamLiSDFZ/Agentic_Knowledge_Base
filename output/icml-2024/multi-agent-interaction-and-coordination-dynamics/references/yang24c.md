---
title: "Sample-Efficient Multiagent Reinforcement Learning with Reset Replay"
source: "https://proceedings.mlr.press/v235/yang24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yang24c/yang24c.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'online-learning-and-sequential-decision-making']
tags: ['multi-agent-RL', 'sample-efficiency', 'reset-replay']
venue: "ICML 2024"
tldr: "Improves sample efficiency in multi-agent reinforcement learning by introducing reset replay to better leverage past experience."
---

# Sample-Efficient Multiagent Reinforcement Learning with Reset Replay

**Source**: [https://proceedings.mlr.press/v235/yang24c.html](https://proceedings.mlr.press/v235/yang24c.html)

**TLDR**: Improves sample efficiency in multi-agent reinforcement learning by introducing reset replay to better leverage past experience.

## Abstract

The popularity of multiagent reinforcement learning (MARL) is growing rapidly with the demand for real-world tasks that require swarm intelligence. However, a noticeable drawback of MARL is its low sample efficiency, which leads to a huge amount of interactions with the environment. Surprisingly, few MARL works focus on this practical problem especially in the parallel environment setting, which greatly hampers the application of MARL into the real world. In response to this gap, in this paper, we propose Multiagent Reinforcement Learning with Reset Replay (MARR) to greatly improve the sample efficiency of MARL by enabling MARL training at a high replay ratio in the parallel environment setting for the first time. To achieve this, first, a reset strategy is introduced for maintaining the network plasticity to ensure that MARL continually learns with a high replay ratio. Second, MARR incorporates a data augmentation technique to boost the sample efficiency further. Extensive experiments in SMAC and MPE show that MARR significantly improves the performance of various MARL approaches with much fewer environment interactions.