---
title: "Hard Tasks First: Multi-Task Reinforcement Learning Through Task Scheduling"
source: "https://proceedings.mlr.press/v235/cho24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cho24d/cho24d.pdf"
categories: ['multi-agent-mdp-structure-and-dependencies', 'optimization-algorithms-convergence-theory']
tags: ['multi-task-reinforcement-learning', 'task-scheduling', 'curriculum-learning']
venue: "ICML 2024"
tldr: "Scheduled Multi-Task Training dynamically prioritizes harder tasks to mitigate negative transfer in multi-task RL."
---

# Hard Tasks First: Multi-Task Reinforcement Learning Through Task Scheduling

**Source**: [https://proceedings.mlr.press/v235/cho24d.html](https://proceedings.mlr.press/v235/cho24d.html)

**TLDR**: Scheduled Multi-Task Training dynamically prioritizes harder tasks to mitigate negative transfer in multi-task RL.

## Abstract

Multi-task reinforcement learning (RL) faces the significant challenge of varying task difficulties, often leading to negative transfer when simpler tasks overshadow the learning of more complex ones. To overcome this challenge, we propose a novel algorithm, Scheduled Multi-Task Training (SMT), that strategically prioritizes more challenging tasks, thereby enhancing overall learning efficiency. SMT introduces a dynamic task prioritization strategy, underpinned by an effective metric for assessing task difficulty. This metric ensures an efficient and targeted allocation of training resources, significantly improving learning outcomes. Additionally, SMT incorporates a reset mechanism that periodically reinitializes key network parameters to mitigate the simplicity bias, further enhancing the adaptability and robustness of the learning process across diverse tasks. The efficacy of SMT’s scheduling method is validated by significantly improving performance on challenging Meta-World benchmarks.