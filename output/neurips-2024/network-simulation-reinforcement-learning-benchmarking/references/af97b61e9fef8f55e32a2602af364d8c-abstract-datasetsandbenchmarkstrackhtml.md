---
title: "NeuralPlane: An Efficiently Parallelizable Platform for Fixed-wing Aircraft Control with Reinforcement Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/af97b61e9fef8f55e32a2602af364d8c-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'network-simulation-reinforcement-learning-benchmarking']
tags: ['reinforcement-learning', 'fixed-wing-aircraft', 'flight-control']
venue: "NeurIPS 2024"
tldr: "Introduces a parallelizable RL simulation platform for efficient training of fixed-wing aircraft control policies."
---

# NeuralPlane: An Efficiently Parallelizable Platform for Fixed-wing Aircraft Control with Reinforcement Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/af97b61e9fef8f55e32a2602af364d8c-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/af97b61e9fef8f55e32a2602af364d8c-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces a parallelizable RL simulation platform for efficient training of fixed-wing aircraft control policies.

## Abstract

Reinforcement learning (RL) demonstrates superior potential over traditional flight control methods for fixed-wing aircraft, particularly under extreme operational conditions. However, the high demand for training samples and the lack of efficient computation in existing simulators hinder its further application. In this paper, we introduce NeuralPlane, the first benchmark platform for large-scale parallel simulations of fixed-wing aircraft. NeuralPlane significantly boosts high-fidelity simulation via GPU-accelerated Flight Dynamics Model (FDM) computation, achieving a single-step simulation time of just 0.2 seconds at a parallel scale of $10^{6}$, far exceeding current platforms. We also provide clear code templates, comprehensive evaluation/visualization tools and hierarchical frameworks for integrating RL and traditional control methods. We believe that NeuralPlane can accelerate the development of RL-based fixed-wing flight control and serve as a new challenging benchmark for the RL community. Our NeuralPlane is open-source and accessible at https://github.com/xuecy22/NeuralPlane.