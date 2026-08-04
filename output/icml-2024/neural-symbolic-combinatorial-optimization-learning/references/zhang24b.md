---
title: "DAG-Based Column Generation for Adversarial Team Games"
source: "https://proceedings.mlr.press/v235/zhang24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhang24b/zhang24b.pdf"
categories: ['multi-agent-interaction-and-coordination-dynamics', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['adversarial-team-games', 'column-generation', 'DAG']
venue: "ICML 2024"
tldr: "A DAG-based column generation algorithm for efficiently computing optimal ex ante coordination strategies in adversarial team games."
---

# DAG-Based Column Generation for Adversarial Team Games

**Source**: [https://proceedings.mlr.press/v235/zhang24b.html](https://proceedings.mlr.press/v235/zhang24b.html)

**TLDR**: A DAG-based column generation algorithm for efficiently computing optimal ex ante coordination strategies in adversarial team games.

## Abstract

Many works recently have focused on computing optimal solutions for the ex ante coordination of a team for solving sequential adversarial team games, where a team of players coordinate against an opponent (or a team of players) in a zero-sum extensive-form game. However, it is challenging to directly compute such an optimal solution because the team’s coordinated strategy space is exponential in the size of the game tree due to the asymmetric information of team members. Column Generation (CG) algorithms have been proposed to overcome this challenge by iteratively expanding the team’s coordinated strategy space via a Best Response Oracle (BRO). More recently, more compact representations (particularly, the Team Belief Directed Acyclic Graph (TB-DAG)) of the team’s coordinated strategy space have been proposed, but the TB-DAG-based algorithms only outperform the CG-based algorithms in games with a small TB-DAG. Unfortunately, it is inefficient to directly apply CG to the TB-DAG because the size of the TB-DAG is still exponential in the size of the game tree and then makes the BRO unscalable. To this end, we develop our novel TB-DAG CG (DCG) algorithm framework by computing a coordinated best response in the original game first and then transforming this strategy into the TB-DAG form. To further improve the scalability, we propose a more suitable BRO for DCG to reduce the cost of the transformation at each iteration. We theoretically show that our algorithm converges exponentially faster than the state-of-the-art CG algorithms, and experimental results show that our algorithm is at least two orders of magnitude faster than the state-of-the-art baselines.