---
title: "ScaLearn: Simple and Highly Parameter-Efficient Task Transfer by Learning to Scale"
source: "https://aclanthology.org/2024.findings-acl.699/"
categories: ['llm-training-alignment-and-evaluation', 'bias-and-fairness-in-llms']
tags: ['multi-task-learning', 'parameter-efficient', 'adapter', 'task-transfer', 'scaling']
venue: "ACL 2024"
tldr: "Proposes ScaLearn, a simple parameter-efficient multi-task transfer method that learns to scale adapter representations across tasks."
---

# ScaLearn: Simple and Highly Parameter-Efficient Task Transfer by Learning to Scale

**Source**: [https://aclanthology.org/2024.findings-acl.699/](https://aclanthology.org/2024.findings-acl.699/)

**TLDR**: Proposes ScaLearn, a simple parameter-efficient multi-task transfer method that learns to scale adapter representations across tasks.

## Abstract

AbstractMulti-task learning (MTL) has shown considerable practical benefits, particularly when using language models (LMs). While this is commonly achieved by learning tasks under a joint optimization procedure, some methods, such as AdapterFusion, divide the problem into two stages: (i) task learning, where knowledge specific to a task is encapsulated within sets of parameters (e.g., adapters), and (ii) transfer, where this already learned knowledge is leveraged for a target task. This separation of concerns provides numerous benefits (e.g., promoting reusability). However, current two stage MTL introduces a substantial number of additional parameters. We address this issue by leveraging the usefulness of linearly scaling the output representations of source adapters for transfer learning. We introduce ScaLearn, a simple and highly parameter-efficient two-stage MTL method that capitalizes on the knowledge of the source tasks by learning a minimal set of scaling parameters that enable effective transfer to a target task. Our experiments on three benchmarks (GLUE, SuperGLUE, and HumSet) and two encoder LMs show that ScaLearn consistently outperforms strong baselines with a small number of transfer parameters (~0.35% of those of AdapterFusion). Remarkably, we observe that ScaLearn maintains its strong abilities even when further reducing parameters, achieving competitive results with only 8 transfer parameters per target task. Our proposed approach thus demonstrates the power of simple scaling as a promise for more efficient task transfer. Our code is available at https://github.com/CPJKU/ScaLearn.