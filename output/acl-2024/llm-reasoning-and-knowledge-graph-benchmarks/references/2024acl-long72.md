---
title: "Advancing Abductive Reasoning in Knowledge Graphs through Complex Logical Hypothesis Generation"
source: "https://aclanthology.org/2024.acl-long.72/"
categories: ['llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['abductive-reasoning', 'knowledge-graphs', 'logical-hypothesis-generation']
venue: "ACL 2024"
tldr: "Advances abductive reasoning over knowledge graphs by generating complex logical hypotheses to explain observations."
---

# Advancing Abductive Reasoning in Knowledge Graphs through Complex Logical Hypothesis Generation

**Source**: [https://aclanthology.org/2024.acl-long.72/](https://aclanthology.org/2024.acl-long.72/)

**TLDR**: Advances abductive reasoning over knowledge graphs by generating complex logical hypotheses to explain observations.

## Abstract

AbstractAbductive reasoning is the process of making educated guesses to provide explanations for observations. Although many applications require the use of knowledge for explanations, the utilization of abductive reasoning in conjunction with structured knowledge, such as a knowledge graph, remains largely unexplored. To fill this gap, this paper introduces the task of complex logical hypothesis generation, as an initial step towards abductive logical reasoning with KG. In this task, we aim to generate a complex logical hypothesis so that it can explain a set of observations. We find that the supervised trained generative model can generate logical hypotheses that are structurally closer to the reference hypothesis. However, when generalized to unseen observations, this training objective does not guarantee better hypothesis generation. To address this, we introduce the Reinforcement Learning from Knowledge Graph (RLF-KG) method, which minimizes differences between observations and conclusions drawn from generated hypotheses according to the KG. Experiments show that, with RLF-KG’s assistance, the generated hypotheses provide better explanations, and achieve state-of-the-art results on three widely used KGs.