---
title: "Open Ad Hoc Teamwork with Cooperative Game Theory"
source: "https://proceedings.mlr.press/v235/wang24an.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24an/wang24an.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'multi-agent-mdp-structure-and-dependencies']
tags: ['ad-hoc-teamwork', 'cooperative-game-theory', 'multi-agent', 'open-team']
venue: "ICML 2024"
tldr: "Cooperative game theory is applied to enable agents to collaborate in open ad hoc teamwork with a variable number of teammates."
---

# Open Ad Hoc Teamwork with Cooperative Game Theory

**Source**: [https://proceedings.mlr.press/v235/wang24an.html](https://proceedings.mlr.press/v235/wang24an.html)

**TLDR**: Cooperative game theory is applied to enable agents to collaborate in open ad hoc teamwork with a variable number of teammates.

## Abstract

Ad hoc teamwork poses a challenging problem, requiring the design of an agent to collaborate with teammates without prior coordination or joint training. Open ad hoc teamwork (OAHT) further complicates this challenge by considering environments with a changing number of teammates, referred to as open teams. One promising solution in practice to this problem is leveraging the generalizability of graph neural networks to handle an unrestricted number of agents with various agent-types, named graph-based policy learning (GPL). However, its joint Q-value representation over a coordination graph lacks convincing explanations. In this paper, we establish a new theory to understand the representation of the joint Q-value for OAHT and its learning paradigm, through the lens of cooperative game theory. Building on our theory, we propose a novel algorithm named CIAO, based on GPL’s framework, with additional provable implementation tricks that can facilitate learning. The demos of experimental results are available on https://sites.google.com/view/ciao2024, and the code of experiments is published on https://github.com/hsvgbkhgbv/CIAO.