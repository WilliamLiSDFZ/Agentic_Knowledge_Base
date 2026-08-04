---
title: "Solving Hierarchical Information-Sharing Dec-POMDPs: An Extensive-Form Game Approach"
source: "https://proceedings.mlr.press/v235/peralez24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/peralez24a/peralez24a.pdf"
categories: ['multi-agent-mdp-structure-and-dependencies', 'multi-agent-interaction-and-coordination-dynamics']
tags: ['Dec-POMDPs', 'extensive-form-games', 'hierarchical-information', 'multi-agent', 'Bellman-optimality']
venue: "ICML 2024"
tldr: "Transforms hierarchical information-sharing Dec-POMDPs into extensive-form games to enable efficient Bellman-based solution methods."
---

# Solving Hierarchical Information-Sharing Dec-POMDPs: An Extensive-Form Game Approach

**Source**: [https://proceedings.mlr.press/v235/peralez24a.html](https://proceedings.mlr.press/v235/peralez24a.html)

**TLDR**: Transforms hierarchical information-sharing Dec-POMDPs into extensive-form games to enable efficient Bellman-based solution methods.

## Abstract

A recent theory shows that a multi-player decentralized partially observable Markov decision process can be transformed into an equivalent single-player game, enabling the application of Bellman’s principle of optimality to solve the single-player game by breaking it down into single-stage subgames. However, this approach entangles the decision variables of all players at each single-stage subgame, resulting in backups with a double-exponential complexity. This paper demonstrates how to disentangle these decision variables while maintaining optimality under hierarchical information sharing, a prominent management style in our society. To achieve this, we apply the principle of optimality to solve any single-stage subgame by breaking it down further into smaller subgames, enabling us to make single-player decisions at a time. Our approach reveals that extensive-form games always exist with solutions to a single-stage subgame, significantly reducing time complexity. Our experimental results show that the algorithms leveraging these findings can scale up to much larger multi-player games without compromising optimality.