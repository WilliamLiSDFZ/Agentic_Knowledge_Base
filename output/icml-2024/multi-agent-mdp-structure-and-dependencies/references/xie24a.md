---
title: "Learning to Explore in POMDPs with Informational Rewards"
source: "https://proceedings.mlr.press/v235/xie24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xie24a/xie24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'multi-agent-mdp-structure-and-dependencies']
tags: ['POMDPs', 'exploration', 'information-gathering']
venue: "ICML 2024"
tldr: "Introduces informational reward bonuses to guide exploration in POMDPs where agents must learn active information-gathering strategies."
---

# Learning to Explore in POMDPs with Informational Rewards

**Source**: [https://proceedings.mlr.press/v235/xie24a.html](https://proceedings.mlr.press/v235/xie24a.html)

**TLDR**: Introduces informational reward bonuses to guide exploration in POMDPs where agents must learn active information-gathering strategies.

## Abstract

Standard exploration methods typically rely on random coverage of the state space or coverage-promoting exploration bonuses. However, in partially observed settings, the biggest exploration challenge is often posed by the need to discover information-gathering strategies—e.g., an agent that has to navigate to a location in traffic might learn to first check traffic conditions and then choose a route. In this work, we design a POMDP agent that gathers information about the hidden state, using ideas from the meta-exploration literature. Our approach provides an exploration bonus that rewards the agent for gathering information about the state that is relevant for completing the task. While this requires the agent to know what this information is during training, it can obtained in several ways: in the most general case, off-policy algorithms can leverage knowledge about the entire trajectory to determine such information in hindsight, but the user can also provide prior knowledge (e.g., privileged information) to help inform the training process. Through experiments in several partially-observed environments, we find that our approach is competitive with prior methods when minimal exploration is needed, but substantially outperforms them when more complex strategies are required. Our algorithm also shows the ability to learn without any privileged information, by reasoning about the entire trajectory in hindsight and and effectively using any information it reveals about the hidden state.