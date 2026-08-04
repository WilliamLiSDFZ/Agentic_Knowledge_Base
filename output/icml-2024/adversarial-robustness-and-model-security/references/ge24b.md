---
title: "Safe and Robust Subgame Exploitation in Imperfect Information Games"
source: "https://proceedings.mlr.press/v235/ge24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ge24b/ge24b.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'adversarial-robustness-and-model-security']
tags: ['opponent-exploitation', 'imperfect-information-games', 'subgame-solving']
venue: "ICML 2024"
tldr: "Introduces a safe and robust subgame exploitation framework resilient to modeling errors and deceptive adversaries in imperfect information games."
---

# Safe and Robust Subgame Exploitation in Imperfect Information Games

**Source**: [https://proceedings.mlr.press/v235/ge24b.html](https://proceedings.mlr.press/v235/ge24b.html)

**TLDR**: Introduces a safe and robust subgame exploitation framework resilient to modeling errors and deceptive adversaries in imperfect information games.

## Abstract

Opponent exploitation is an important task for players to exploit the weaknesses of others in games. Existing approaches mainly focus on balancing between exploitation and exploitability but are often vulnerable to modeling errors and deceptive adversaries. To address this problem, our paper offers a novel perspective on the safety of opponent exploitation, named Adaptation Safety. This concept leverages the insight that strategies, even those not explicitly aimed at opponent exploitation, may inherently be exploitable due to computational complexities, rendering traditional safety overly rigorous. In contrast, adaptation safety requires that the strategy should not be more exploitable than it would be in scenarios where opponent exploitation is not considered. Building on such adaptation safety, we further propose an Opponent eXploitation Search (OX-Search) framework by incorporating real-time search techniques for efficient online opponent exploitation. Moreover, we provide theoretical analyses to show the adaptation safety and robust exploitation of OX-Search, even with inaccurate opponent models. Empirical evaluations in popular poker games demonstrate OX-Search’s superiority in both exploitability and exploitation compared to previous methods.