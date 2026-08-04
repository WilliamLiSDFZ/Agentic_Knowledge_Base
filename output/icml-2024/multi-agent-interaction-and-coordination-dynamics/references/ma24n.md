---
title: "Fast Peer Adaptation with Context-aware Exploration"
source: "https://proceedings.mlr.press/v235/ma24n.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ma24n/ma24n.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'online-learning-and-sequential-decision-making']
tags: ['multi-agent-adaptation', 'context-aware-exploration', 'peer-strategy-identification']
venue: "ICML 2024"
tldr: "A context-aware exploration method enabling fast adaptation to unknown peers in multi-agent games by efficiently identifying their strategies."
---

# Fast Peer Adaptation with Context-aware Exploration

**Source**: [https://proceedings.mlr.press/v235/ma24n.html](https://proceedings.mlr.press/v235/ma24n.html)

**TLDR**: A context-aware exploration method enabling fast adaptation to unknown peers in multi-agent games by efficiently identifying their strategies.

## Abstract

Fast adapting to unknown peers (partners or opponents) with different strategies is a key challenge in multi-agent games. To do so, it is crucial for the agent to probe and identify the peer’s strategy efficiently, as this is the prerequisite for carrying out the best response in adaptation. However, exploring the strategies of unknown peers is difficult, especially when the games are partially observable and have a long horizon. In this paper, we propose a peer identification reward, which rewards the learning agent based on how well it can identify the behavior pattern of the peer over the historical context, such as the observation over multiple episodes. This reward motivates the agent to learn a context-aware policy for effective exploration and fast adaptation, i.e., to actively seek and collect informative feedback from peers when uncertain about their policies and to exploit the context to perform the best response when confident. We evaluate our method on diverse testbeds that involve competitive (Kuhn Poker), cooperative (PO-Overcooked), or mixed (Predator-Prey-W) games with peer agents. We demonstrate that our method induces more active exploration behavior, achieving faster adaptation and better outcomes than existing methods.