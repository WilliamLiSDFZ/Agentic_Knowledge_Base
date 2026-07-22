---
title: "AGR: Reinforced Causal Agent-Guided Self-explaining Rationalization"
source: "https://aclanthology.org/2024.acl-short.47/"
categories: ['causal-reasoning-and-explanation-in-nlp', 'llm-agents-reasoning-and-planning']
tags: ['rationalization', 'causal-reasoning', 'reinforcement-learning', 'agent']
venue: "ACL 2024"
tldr: "Introduces a reinforced causal agent-guided rationalization approach to mitigate degeneration in self-explaining models."
---

# AGR: Reinforced Causal Agent-Guided Self-explaining Rationalization

**Source**: [https://aclanthology.org/2024.acl-short.47/](https://aclanthology.org/2024.acl-short.47/)

**TLDR**: Introduces a reinforced causal agent-guided rationalization approach to mitigate degeneration in self-explaining models.

## Abstract

AbstractMost existing rationalization approaches are susceptible to degeneration accumulation due to a lack of effective control over the learning direction of the model during training. To address this issue, we propose a novel approach AGR (Agent-Guided Rationalization), guiding the next action of the model based on its current training state. Specifically, we introduce causal intervention calculus to quantify the causal effects inherent during rationale training, and utilize reinforcement learning process to refine the learning bias of them. Furthermore, we pretrain an agent within this reinforced causal environment to guide the next step of the model. We theoretically demonstrate that a good model needs the desired guidance, and empirically show the effectiveness of our approach, outperforming existing state-of-the-art methods on BeerAdvocate and HotelReview datasets.