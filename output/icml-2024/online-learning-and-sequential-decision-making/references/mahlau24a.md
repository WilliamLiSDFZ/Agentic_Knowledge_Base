---
title: "Mastering Zero-Shot Interactions in Cooperative and Competitive Simultaneous Games"
source: "https://proceedings.mlr.press/v235/mahlau24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mahlau24a/mahlau24a.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'online-learning-and-sequential-decision-making']
tags: ['zero-shot-coordination', 'simultaneous-games', 'self-play-planning']
venue: "ICML 2024"
tldr: "An algorithm mastering zero-shot interactions in cooperative and competitive simultaneous games by extending self-play and planning to handle missing concurrent action information."
---

# Mastering Zero-Shot Interactions in Cooperative and Competitive Simultaneous Games

**Source**: [https://proceedings.mlr.press/v235/mahlau24a.html](https://proceedings.mlr.press/v235/mahlau24a.html)

**TLDR**: An algorithm mastering zero-shot interactions in cooperative and competitive simultaneous games by extending self-play and planning to handle missing concurrent action information.

## Abstract

The combination of self-play and planning has achieved great successes in sequential games, for instance in Chess and Go. However, adapting algorithms such as AlphaZero to simultaneous games poses a new challenge. In these games, missing information about concurrent actions of other agents is a limiting factor as they may select different Nash equilibria or do not play optimally at all. Thus, it is vital to model the behavior of the other agents when interacting with them in simultaneous games. To this end, we propose Albatross: AlphaZero for Learning Bounded-rational Agents and Temperature-based Response Optimization using Simulated Self-play. Albatross learns to play the novel equilibrium concept of a Smooth Best Response Logit Equilibrium (SBRLE), which enables cooperation and competition with agents of any playing strength. We perform an extensive evaluation of Albatross on a set of cooperative and competitive simultaneous perfect-information games. In contrast to AlphaZero, Albatross is able to exploit weak agents in the competitive game of Battlesnake. Additionally, it yields an improvement of 37.6% compared to previous state of the art in the cooperative Overcooked benchmark.