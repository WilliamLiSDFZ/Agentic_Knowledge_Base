---
title: "Position: Automatic Environment Shaping is the Next Frontier in RL"
source: "https://proceedings.mlr.press/v235/park24i.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/park24i/park24i.pdf"
categories: ['position-papers-on-ml-research-directions', 'simulation-scaling-limits-for-robot-manipulation']
tags: ['reinforcement-learning', 'sim-to-real', 'environment-shaping', 'robotics']
venue: "ICML 2024"
tldr: "Argues that automatic environment shaping is the next frontier in RL for robotics, enabling agents to autonomously adapt simulation environments for efficient skill acquisition."
---

# Position: Automatic Environment Shaping is the Next Frontier in RL

**Source**: [https://proceedings.mlr.press/v235/park24i.html](https://proceedings.mlr.press/v235/park24i.html)

**TLDR**: Argues that automatic environment shaping is the next frontier in RL for robotics, enabling agents to autonomously adapt simulation environments for efficient skill acquisition.

## Abstract

Many roboticists dream of presenting a robot with a task in the evening and returning the next morning to find the robot capable of solving the task. What is preventing us from achieving this? Sim-to-real reinforcement learning (RL) has achieved impressive performance on challenging robotics tasks, but requires substantial human effort to set up the task in a way that is amenable to RL. It’s our position that algorithmic improvements in policy optimization and other ideas should be guided towards resolving the primary bottleneck of shaping the training environment, i.e., designing observations, actions, rewards and simulation dynamics. Most practitioners don’t tune the RL algorithm, but other environment parameters to obtain a desirable controller. We posit that scaling RL to diverse robotic tasks will only be achieved if the community focuses on automating environment shaping procedures.