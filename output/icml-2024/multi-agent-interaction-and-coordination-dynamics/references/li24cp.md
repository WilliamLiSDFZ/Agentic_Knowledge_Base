---
title: "EvoRainbow: Combining Improvements in Evolutionary Reinforcement Learning for Policy Search"
source: "https://proceedings.mlr.press/v235/li24cp.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24cp/li24cp.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics']
tags: ['evolutionary-algorithms', 'reinforcement-learning', 'policy-search']
venue: "ICML 2024"
tldr: "EvoRainbow systematically combines improvements from evolutionary algorithms and reinforcement learning for efficient policy optimization."
---

# EvoRainbow: Combining Improvements in Evolutionary Reinforcement Learning for Policy Search

**Source**: [https://proceedings.mlr.press/v235/li24cp.html](https://proceedings.mlr.press/v235/li24cp.html)

**TLDR**: EvoRainbow systematically combines improvements from evolutionary algorithms and reinforcement learning for efficient policy optimization.

## Abstract

Both Evolutionary Algorithms (EAs) and Reinforcement Learning (RL) have demonstrated powerful capabilities in policy search with different principles. A promising direction is to combine the respective strengths of both for efficient policy optimization. To this end, many works have proposed various mechanisms to integrate EAs and RL. However, it is still unclear which of these mechanisms are complementary and can be fully combined. In this paper, we revisit different mechanisms from five perspectives: 1) Interaction Mode, 2) Individual Architecture, 3) EAs and operators, 4) Impact of EA on RL, and 5) Fitness Surrogate and Usage. We evaluate the effectiveness of each mechanism and experimentally analyze the reasons for the more effective mechanisms. Using the most effective mechanisms, we develop EvoRainbow and EvoRainbow-Exp, which outperform strong baselines and provide state-of-the-art performance across various tasks with distinct characteristics. To promote community development, we release the code on https://github.com/yeshenpy/EvoRainbow.