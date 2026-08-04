---
title: "RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation"
source: "https://proceedings.mlr.press/v235/wang24cc.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24cc/wang24cc.pdf"
categories: ['simulation-scaling-limits-for-robot-manipulation', 'llm-driven-automated-system-optimization']
tags: ['robot-learning', 'generative-simulation', 'foundation-models', 'skill-generation']
venue: "ICML 2024"
tldr: "Presents RoboGen, a generative robotic agent that uses foundation and generative models to automatically synthesize diverse robot skills at scale via generative simulation."
---

# RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation

**Source**: [https://proceedings.mlr.press/v235/wang24cc.html](https://proceedings.mlr.press/v235/wang24cc.html)

**TLDR**: Presents RoboGen, a generative robotic agent that uses foundation and generative models to automatically synthesize diverse robot skills at scale via generative simulation.

## Abstract

We present RoboGen, a generative robotic agent that automatically learns diverse robotic skills at scale via generative simulation. RoboGen leverages the latest advancements in foundation and generative models. Instead of directly adapting these models to produce policies or low-level actions, we advocate for a generative scheme, which uses these models to automatically generate diversified tasks, scenes, and training supervisions, thereby scaling up robotic skill learning with minimal human supervision. Our approach equips a robotic agent with a self-guided propose-generate-learn cycle: the agent first proposes interesting tasks and skills to develop, and then generates simulation environments by populating pertinent assets with proper spatial configurations. Afterwards, the agent decomposes the proposed task into sub-tasks, selects the optimal learning approach (reinforcement learning, motion planning, or trajectory optimization), generates required training supervision, and then learns policies to acquire the proposed skill. Our fully generative pipeline can be queried repeatedly, producing an endless stream of skill demonstrations associated with diverse tasks and environments.