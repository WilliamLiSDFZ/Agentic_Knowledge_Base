---
title: "Reason for Future, Act for Now: A Principled Architecture for Autonomous LLM Agents"
source: "https://proceedings.mlr.press/v235/liu24ab.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24ab/liu24ab.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-driven-automated-system-optimization']
tags: ['llm-agents', 'autonomous-decision-making', 'task-planning']
venue: "ICML 2024"
tldr: "A principled architecture for autonomous LLM agents that provably minimizes environment interactions by reasoning about future goals while acting optimally in the present."
---

# Reason for Future, Act for Now: A Principled Architecture for Autonomous LLM Agents

**Source**: [https://proceedings.mlr.press/v235/liu24ab.html](https://proceedings.mlr.press/v235/liu24ab.html)

**TLDR**: A principled architecture for autonomous LLM agents that provably minimizes environment interactions by reasoning about future goals while acting optimally in the present.

## Abstract

Large language models (LLMs) demonstrate impressive reasoning abilities, but translating reasoning into actions in the real world remains challenging. In particular, it is unclear how to complete a given task provably within a minimum number of interactions with the external environment, e.g., through an internal mechanism of reasoning. To this end, we propose the first framework with provable regret guarantees to orchestrate reasoning and acting, which we call reason for future, act for now (RAFA). Specifically, we design a prompt template for reasoning that learns from the memory buffer and plans a future trajectory over a long horizon (reason for future). At each step, the LLM agent takes the initial action of the planned trajectory (act for now), stores the collected feedback in the memory buffer, and reinvokes the reasoning routine to replan the future trajectory from the new state. The key idea is to cast reasoning in LLMs as learning and planning in Bayesian adaptive Markov decision processes (MDPs). Correspondingly, we prompt LLMs with the memory buffer to estimate the unknown environment (learning) and generate an optimal trajectory for multiple future steps that maximize a value function (planning). The learning and planning subroutines are performed in an in-context manner to emulate the actor-critic update for MDPs. Our theoretical analysis establishes a $\sqrt{T}$ regret, while our experimental validation demonstrates superior empirical performance.