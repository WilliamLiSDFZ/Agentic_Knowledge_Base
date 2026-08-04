---
title: "Individual Contributions as Intrinsic Exploration Scaffolds for Multi-agent Reinforcement Learning"
source: "https://proceedings.mlr.press/v235/li24aw.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24aw/li24aw.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'online-learning-and-sequential-decision-making']
tags: ['multi-agent-RL', 'exploration', 'intrinsic-reward', 'credit-assignment', 'sparse-reward']
venue: "ICML 2024"
tldr: "Individual contribution-based intrinsic exploration scaffolds improve multi-agent reinforcement learning in sparse reward settings."
---

# Individual Contributions as Intrinsic Exploration Scaffolds for Multi-agent Reinforcement Learning

**Source**: [https://proceedings.mlr.press/v235/li24aw.html](https://proceedings.mlr.press/v235/li24aw.html)

**TLDR**: Individual contribution-based intrinsic exploration scaffolds improve multi-agent reinforcement learning in sparse reward settings.

## Abstract

In multi-agent reinforcement learning (MARL), effective exploration is critical, especially in sparse reward environments. Although introducing global intrinsic rewards can foster exploration in such settings, it often complicates credit assignment among agents. To address this difficulty, we propose Individual Contributions as intrinsic Exploration Scaffolds (ICES), a novel approach to motivate exploration by assessing each agent’s contribution from a global view. In particular, ICES constructs exploration scaffolds with Bayesian surprise, leveraging global transition information during centralized training. These scaffolds, used only in training, help to guide individual agents towards actions that significantly impact the global latent state transitions. Additionally, ICES separates exploration policies from exploitation policies, enabling the former to utilize privileged global information during training. Extensive experiments on cooperative benchmark tasks with sparse rewards, including Google Research Football (GRF) and StarCraft Multi-agent Challenge (SMAC), demonstrate that ICES exhibits superior exploration capabilities compared with baselines. The code is publicly available at https://github.com/LXXXXR/ICES.