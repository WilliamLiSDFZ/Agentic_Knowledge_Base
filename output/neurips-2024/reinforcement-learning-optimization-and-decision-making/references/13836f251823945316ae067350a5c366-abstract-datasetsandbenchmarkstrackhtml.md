---
title: "DiscoveryWorld: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/13836f251823945316ae067350a5c366-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'reinforcement-learning-optimization-and-decision-making']
tags: ['scientific-discovery', 'virtual-environment', 'agent-evaluation']
venue: "NeurIPS 2024"
tldr: "DiscoveryWorld is a virtual environment benchmark for developing and evaluating AI agents capable of end-to-end automated scientific discovery."
---

# DiscoveryWorld: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/13836f251823945316ae067350a5c366-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/13836f251823945316ae067350a5c366-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: DiscoveryWorld is a virtual environment benchmark for developing and evaluating AI agents capable of end-to-end automated scientific discovery.

## Abstract

Automated scientific discovery promises to accelerate progress across scientific domains, but evaluating an agent's capacity for end-to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. In this work we introduce DiscoveryWorld, a virtual environment that enables benchmarking an agent's ability to perform complete cycles of novel scientific discovery in an inexpensive, simulated, multi-modal, long-horizon, and fictional setting.DiscoveryWorld consists of 24 scientific tasks across three levels of difficulty, each with parametric variations that provide new discoveries for agents to make across runs. Tasks require an agent to form hypotheses, design and run experiments, analyze results, and act on conclusions. Task difficulties are normed to range from straightforward to challenging for human scientists with advanced degrees. DiscoveryWorld further provides three automatic metrics for evaluating performance, including: (1) binary task completion, (2) fine-grained report cards detailing procedural scoring of task-relevant actions, and (3) the accuracy of discovered explanatory knowledge.While simulated environments such as DiscoveryWorld are low-fidelity compared to the real world, we find that strong baseline agents struggle on most DiscoveryWorld tasks, highlighting the utility of using simulated environments as proxy tasks for near-term development of scientific discovery competency in agents.