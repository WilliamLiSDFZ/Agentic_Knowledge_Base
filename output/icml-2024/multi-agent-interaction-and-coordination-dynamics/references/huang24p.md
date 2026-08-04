---
title: "Efficient Adaptation in Mixed-Motive Environments via Hierarchical Opponent Modeling and Planning"
source: "https://proceedings.mlr.press/v235/huang24p.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24p/huang24p.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'multi-agent-mdp-structure-and-dependencies']
tags: ['multi-agent-reinforcement-learning', 'opponent-modeling', 'hierarchical-planning']
venue: "ICML 2024"
tldr: "Proposes hierarchical opponent modeling and planning for efficient adaptation to co-players in mixed-motive multi-agent environments."
---

# Efficient Adaptation in Mixed-Motive Environments via Hierarchical Opponent Modeling and Planning

**Source**: [https://proceedings.mlr.press/v235/huang24p.html](https://proceedings.mlr.press/v235/huang24p.html)

**TLDR**: Proposes hierarchical opponent modeling and planning for efficient adaptation to co-players in mixed-motive multi-agent environments.

## Abstract

Despite the recent successes of multi-agent reinforcement learning (MARL) algorithms, efficiently adapting to co-players in mixed-motive environments remains a significant challenge. One feasible approach is to hierarchically model co-players’ behavior based on inferring their characteristics. However, these methods often encounter difficulties in efficient reasoning and utilization of inferred information. To address these issues, we propose Hierarchical Opponent modeling and Planning (HOP), a novel multi-agent decision-making algorithm that enables few-shot adaptation to unseen policies in mixed-motive environments. HOP is hierarchically composed of two modules: an opponent modeling module that infers others’ goals and learns corresponding goal-conditioned policies, and a planning module that employs Monte Carlo Tree Search (MCTS) to identify the best response. Our approach improves efficiency by updating beliefs about others’ goals both across and within episodes and by using information from the opponent modeling module to guide planning. Experimental results demonstrate that in mixed-motive environments, HOP exhibits superior few-shot adaptation capabilities when interacting with various unseen agents, and excels in self-play scenarios. Furthermore, the emergence of social intelligence during our experiments underscores the potential of our approach in complex multi-agent environments.