---
title: "LogiCity: Advancing Neuro-Symbolic AI with Abstract Urban Simulation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/8196be81e68289d7a9ece21ed7f5750a-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['neural-networks-for-formal-reasoning-and-verification', 'ai-benchmarking-and-evaluation-methodology']
tags: ['neuro-symbolic-AI', 'urban-simulation', 'multi-agent', 'long-horizon-reasoning']
venue: "NeurIPS 2024"
tldr: "LogiCity is an abstract urban simulation benchmark designed to advance neuro-symbolic AI with complex multi-agent long-horizon reasoning tasks."
---

# LogiCity: Advancing Neuro-Symbolic AI with Abstract Urban Simulation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/8196be81e68289d7a9ece21ed7f5750a-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/8196be81e68289d7a9ece21ed7f5750a-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: LogiCity is an abstract urban simulation benchmark designed to advance neuro-symbolic AI with complex multi-agent long-horizon reasoning tasks.

## Abstract

Recent years have witnessed the rapid development of Neuro-Symbolic (NeSy) AI systems, which integrate symbolic reasoning into deep neural networks.However, most of the existing benchmarks for NeSy AI fail to provide long-horizon reasoning tasks with complex multi-agent interactions.Furthermore, they are usually constrained by fixed and simplistic logical rules over limited entities, making them far from real-world complexities.To address these crucial gaps, we introduce LogiCity, the first simulator based on customizable first-order logic (FOL) for an urban-like environment with multiple dynamic agents.LogiCity models diverse urban elements using semantic and spatial concepts, such as $\texttt{IsAmbulance}(\texttt{X})$ and $\texttt{IsClose}(\texttt{X}, \texttt{Y})$. These concepts are used to define FOL rules that govern the behavior of various agents. Since the concepts and rules are abstractions, they can be universally applied to cities with any agent compositions, facilitating the instantiation of diverse scenarios.Besides, a key feature of LogiCity is its support for user-configurable abstractions, enabling customizable simulation complexities for logical reasoning.To explore various aspects of NeSy AI, LogiCity introduces two tasks, one features long-horizon sequential decision-making, and the other focuses on one-step visual reasoning, varying in difficulty and agent behaviors.Our extensive evaluation reveals the advantage of NeSy frameworks in abstract reasoning. Moreover, we highlight the significant challenges of handling more complex abstractions in long-horizon multi-agent scenarios or under high-dimensional, imbalanced data.With its flexible design, various features, and newly raised challenges, we believe LogiCity represents a pivotal step forward in advancing the next generation of NeSy AI.All the code and data are open-sourced at our website.