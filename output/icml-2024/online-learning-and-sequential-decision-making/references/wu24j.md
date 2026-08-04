---
title: "Planning, Fast and Slow: Online Reinforcement Learning with Action-Free Offline Data via Multiscale Planners"
source: "https://proceedings.mlr.press/v235/wu24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24j/wu24j.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['reinforcement-learning', 'offline-data', 'video-learning', 'passive-rl', 'multiscale-planning']
venue: "ICML 2024"
tldr: "Explores how passive video observations can be converted into actionable reinforcement learning insights using multiscale planners combining fast and slow planning."
---

# Planning, Fast and Slow: Online Reinforcement Learning with Action-Free Offline Data via Multiscale Planners

**Source**: [https://proceedings.mlr.press/v235/wu24j.html](https://proceedings.mlr.press/v235/wu24j.html)

**TLDR**: Explores how passive video observations can be converted into actionable reinforcement learning insights using multiscale planners combining fast and slow planning.

## Abstract

The surge in volumes of video data offers unprecedented opportunities for advancing reinforcement learning (RL). This growth has motivated the development of passive RL, seeking to convert passive observations into actionable insights. This paper explores the prerequisites and mechanisms through which passive data can be utilized to improve online RL. We show that, in identifiable dynamics, where action impact can be distinguished from stochasticity, learning on passive data is statistically beneficial. Building upon the theoretical insights, we propose a novel algorithm named Multiscale State-Centric Planners (MSCP) that leverages two planners at distinct scales to offer guidance across varying levels of abstraction. The algorithm’s fast planner targets immediate objectives, while the slow planner focuses on achieving longer-term goals. Notably, the fast planner incorporates pessimistic regularization to address the distributional shift between offline and online data. MSCP effectively handles the practical challenges involving imperfect pretraining and limited dataset coverage. Our empirical evaluations across multiple benchmarks demonstrate that MSCP significantly outperforms existing approaches, underscoring its proficiency in addressing complex, long-horizon tasks through the strategic use of passive data.