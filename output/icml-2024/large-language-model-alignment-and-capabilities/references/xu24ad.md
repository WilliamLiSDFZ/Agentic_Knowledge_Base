---
title: "Language Agents with Reinforcement Learning for Strategic Play in the Werewolf Game"
source: "https://proceedings.mlr.press/v235/xu24ad.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xu24ad/xu24ad.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['language-agents', 'reinforcement-learning', 'social-deduction-games']
venue: "ICML 2024"
tldr: "Combines LLMs with reinforcement learning to reduce action bias in language agents playing the strategic Werewolf game."
---

# Language Agents with Reinforcement Learning for Strategic Play in the Werewolf Game

**Source**: [https://proceedings.mlr.press/v235/xu24ad.html](https://proceedings.mlr.press/v235/xu24ad.html)

**TLDR**: Combines LLMs with reinforcement learning to reduce action bias in language agents playing the strategic Werewolf game.

## Abstract

Agents built with large language models (LLMs) have shown great potential across a wide range of domains. However, in complex decision-making tasks, pure LLM-based agents tend to exhibit intrinsic bias in their choice of actions, which is inherited from the model’s training data and results in suboptimal performance. To develop strategic language agents, i.e., agents that generate flexible language actions and possess strong decision-making abilities, we propose a novel framework that powers LLM-based agents with reinforcement learning (RL). We consider Werewolf, a popular social deduction game, as a challenging testbed that emphasizes versatile communication and strategic gameplay. To mitigate the intrinsic bias in language actions, our agents use an LLM to perform deductive reasoning and generate a diverse set of action candidates. Then an RL policy trained to optimize the decision-making ability chooses an action from the candidates to play in the game. Extensive experiments show that our agents overcome the intrinsic bias and outperform existing LLM-based agents in the Werewolf game. We also conduct human-agent experiments and find that our agents achieve human-level performance and demonstrate strong strategic play.