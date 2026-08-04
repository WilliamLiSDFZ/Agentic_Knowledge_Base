---
title: "CHEMREASONER: Heuristic Search over a Large Language Model’s Knowledge Space using Quantum-Chemical Feedback"
source: "https://proceedings.mlr.press/v235/sprueill24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sprueill24a/sprueill24a.pdf"
categories: ['llm-driven-automated-system-optimization', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['catalyst-discovery', 'LLMs', 'quantum-chemistry', 'heuristic-search']
venue: "ICML 2024"
tldr: "CHEMREASONER combines LLM linguistic reasoning with quantum-chemical feedback to guide heuristic search for novel catalyst discovery."
---

# CHEMREASONER: Heuristic Search over a Large Language Model’s Knowledge Space using Quantum-Chemical Feedback

**Source**: [https://proceedings.mlr.press/v235/sprueill24a.html](https://proceedings.mlr.press/v235/sprueill24a.html)

**TLDR**: CHEMREASONER combines LLM linguistic reasoning with quantum-chemical feedback to guide heuristic search for novel catalyst discovery.

## Abstract

The discovery of new catalysts is essential for the design of new and more efficient chemical processes in order to transition to a sustainable future. We introduce an AI-guided computational screening framework unifying linguistic reasoning with quantum-chemistry based feedback from 3D atomistic representations. Our approach formulates catalyst discovery as an uncertain environment where an agent actively searches for highly effective catalysts via the iterative combination of large language model (LLM)-derived hypotheses and atomistic graph neural network (GNN)-derived feedback. Identified catalysts in intermediate search steps undergo structural evaluation based on spatial orientation, reaction pathways, and stability. Scoring functions based on adsorption energies and reaction energy barriers steer the exploration in the LLM’s knowledge space toward energetically favorable, high-efficiency catalysts. We introduce planning methods that automatically guide the exploration without human input, providing competitive performance against expert-enumerated chemical descriptor-based implementations. By integrating language-guided reasoning with computational chemistry feedback, our work pioneers AI-accelerated, trustworthy catalyst discovery.