---
title: "Feint Behaviors and Strategies: Formalization, Implementation and Evaluation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/064ae24cdbb3eaacc801ee7f4fe0e4f2-Abstract-Conference.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'llm-agent-communication-and-cooperation']
tags: ['feint-behavior', 'deception-strategies', 'competitive-games']
venue: "NeurIPS 2024"
tldr: "This paper formalizes, implements, and evaluates feint deceptive behaviors and strategies for competitive multi-player games."
---

# Feint Behaviors and Strategies: Formalization, Implementation and Evaluation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/064ae24cdbb3eaacc801ee7f4fe0e4f2-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/064ae24cdbb3eaacc801ee7f4fe0e4f2-Abstract-Conference.html)

**TLDR**: This paper formalizes, implements, and evaluates feint deceptive behaviors and strategies for competitive multi-player games.

## Abstract

Feint behaviors refer to a set of deceptive behaviors in a nuanced manner, which enable players to obtain temporal and spatial advantages over opponents in competitive games. Such behaviors are crucial tactics in most competitive multi-player games (e.g., boxing, fencing, basketball, motor racing, etc.). However, existing literature does not provide a comprehensive (and/or concrete) formalization for Feint behaviors, and their implications on game strategies. In this work, we introduce the first comprehensive formalization of Feint behaviors at both action-level and strategy-level, and provide concrete implementation and quantitative evaluation of them in multi-player games. The key idea of our work is to (1) allow automatic generation of Feint behaviors via Palindrome-directed templates, combine them into meaningful behavior sequences via a Dual-Behavior Model; (2) concertize the implications from our formalization of Feint on game strategies, in terms of temporal, spatial, and their collective impacts respectively; and (3) provide a unified implementation scheme of Feint behaviors in existing MARL frameworks. The experimental results show that our design of Feint behaviors can (1) greatly improve the game reward gains; (2) significantly improve the diversity of Multi-Player Games; and (3) only incur negligible overheads in terms of time consumption.