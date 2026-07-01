---
title: "QGym: Scalable Simulation and Benchmarking of Queuing Network Controllers"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a7f67788f7b4d77fa7cd6887de3dcbe7-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'ai-benchmarking-and-evaluation-methodology']
tags: ['queuing-networks', 'reinforcement-learning', 'simulation-benchmarking']
venue: "NeurIPS 2024"
tldr: "QGym is a scalable simulation and benchmarking platform for reinforcement learning-based queuing network controllers."
---

# QGym: Scalable Simulation and Benchmarking of Queuing Network Controllers

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a7f67788f7b4d77fa7cd6887de3dcbe7-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/a7f67788f7b4d77fa7cd6887de3dcbe7-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: QGym is a scalable simulation and benchmarking platform for reinforcement learning-based queuing network controllers.

## Abstract

Queuing network control allows allocation of  scarce resources to manage congestion, a fundamental problem in manufacturing, communications, and healthcare. Compared to standard RL problems, queueing problems  are distinguished by unique challenges: i) a system operating in continuous time, ii) high stochasticity, and iii) long horizons over which the system can become unstable (exploding delays). To provide the empirical foundations for methodological development tackling these challenges, we present an open-sourced  queueing simulation framework, QGym, that benchmark queueing policies across realistic problem instances. Our modular framework allows the researchers to build on our initial instances, which provide a wide range of environments including parallel servers, criss-cross, tandem, and re-entrant networks, as well as a realistically calibrated hospital queuing system.  From these, various policies can be easily tested, including both model-free RL methods and classical queuing policies. Our testbed significantly expands the scope of empirical benchmarking in prior work, and complements thetraditional focus on evaluating algorithms based on mathematical guarantees in idealized settings. QGym code is open-sourced at https://github.com/namkoong-lab/QGym.