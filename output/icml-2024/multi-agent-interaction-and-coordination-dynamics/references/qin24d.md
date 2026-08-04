---
title: "Feasible Reachable Policy Iteration"
source: "https://proceedings.mlr.press/v235/qin24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/qin24d/qin24d.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['safe-RL', 'goal-reaching', 'policy-iteration', 'safety-constraints', 'sparse-rewards']
venue: "ICML 2024"
tldr: "A feasible reachable policy iteration method addressing safety constraints and sparse rewards in goal-reaching control tasks."
---

# Feasible Reachable Policy Iteration

**Source**: [https://proceedings.mlr.press/v235/qin24d.html](https://proceedings.mlr.press/v235/qin24d.html)

**TLDR**: A feasible reachable policy iteration method addressing safety constraints and sparse rewards in goal-reaching control tasks.

## Abstract

The goal-reaching tasks with safety constraints are common control problems in real world, such as intelligent driving and robot manipulation. The difficulty of this kind of problem comes from the exploration termination caused by safety constraints and the sparse rewards caused by goals. The existing safe RL avoids unsafe exploration by restricting the search space to a feasible region, the essence of which is the pruning of the search space. However, there are still many ineffective explorations in the feasible region because of the ignorance of the goals. Our approach considers both safety and goals; the policy space pruning is achieved by a function called feasible reachable function, which describes whether there is a policy to make the agent safely reach the goals in the finite time domain. This function naturally satisfies the self-consistent condition and the risky Bellman equation, which can be solved by the fixed point iteration method. On this basis, we propose feasible reachable policy iteration (FRPI), which is divided into three steps: policy evaluation, region expansion, and policy improvement. In the region expansion step, by using the information of agent to reach the goals, the convergence of the feasible region is accelerated, and simultaneously a smaller feasible reachable region is identified. The experimental results verify the effectiveness of the proposed FR function in both improving the convergence speed of better or comparable performance without sacrificing safety and identifying a smaller policy space with higher sample efficiency.