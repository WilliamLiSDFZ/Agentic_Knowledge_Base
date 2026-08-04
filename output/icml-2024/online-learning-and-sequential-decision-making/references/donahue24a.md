---
title: "Impact of Decentralized Learning on Player Utilities in Stackelberg Games"
source: "https://proceedings.mlr.press/v235/donahue24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/donahue24a/donahue24a.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'online-learning-and-sequential-decision-making']
tags: ['Stackelberg-games', 'decentralized-learning', 'multi-agent', 'recommender-systems', 'utility']
venue: "ICML 2024"
tldr: "Analyzes the impact of decentralized learning by two non-aligned agents in Stackelberg games on their long-run utilities and equilibrium behavior."
---

# Impact of Decentralized Learning on Player Utilities in Stackelberg Games

**Source**: [https://proceedings.mlr.press/v235/donahue24a.html](https://proceedings.mlr.press/v235/donahue24a.html)

**TLDR**: Analyzes the impact of decentralized learning by two non-aligned agents in Stackelberg games on their long-run utilities and equilibrium behavior.

## Abstract

When deployed in the world, a learning agent such as a recommender system or a chatbot often repeatedly interacts with another learning agent (such as a user) over time. In many such two-agent systems, each agent learns separately and the rewards of the two agents are not perfectly aligned. To better understand such cases, we examine the learning dynamics of the two-agent system and the implications for each agent’s objective. We model these systems as Stackelberg games with decentralized learning and show that standard regret benchmarks (such as Stackelberg equilibrium payoffs) result in worst-case linear regret for at least one player. To better capture these systems, we construct a relaxed regret benchmark that is tolerant to small learning errors by agents. We show that standard learning algorithms fail to provide sublinear regret, and we develop algorithms to achieve near-optimal $\mathcal{O}(T^{2/3})$ regret for both players with respect to these benchmarks. We further design relaxed environments under which faster learning ($\mathcal{O}(\sqrt{T})$) is possible. Altogether, our results take a step towards assessing how two-agent interactions in sequential and decentralized learning environments affect the utility of both agents.