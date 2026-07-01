---
title: "ODRL: A Benchmark for Off-Dynamics Reinforcement Learning"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/6e37ba8a27b53fccd367c648ff365b8f-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['reinforcement-learning-optimization-and-decision-making']
tags: ['off-dynamics-reinforcement-learning', 'benchmark', 'domain-transfer', 'dynamics-mismatch', 'policy-transfer']
venue: "NeurIPS 2024"
tldr: "ODRL introduces a standardized benchmark for off-dynamics reinforcement learning to evaluate algorithms under dynamics mismatch across domains."
---

# ODRL: A Benchmark for Off-Dynamics Reinforcement Learning

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/6e37ba8a27b53fccd367c648ff365b8f-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/6e37ba8a27b53fccd367c648ff365b8f-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: ODRL introduces a standardized benchmark for off-dynamics reinforcement learning to evaluate algorithms under dynamics mismatch across domains.

## Abstract

We consider off-dynamics reinforcement learning (RL) where one needs to transfer policies across different domains with dynamics mismatch. Despite the focus on developing dynamics-aware algorithms, this field is hindered due to the lack of a standard benchmark. To bridge this gap, we introduce ODRL, the first benchmark tailored for evaluating off-dynamics RL methods. ODRL contains four experimental settings where the source and target domains can be either online or offline, and provides diverse tasks and a broad spectrum of dynamics shifts, making it a reliable platform to comprehensively evaluate the agent's adaptation ability to the target domain. Furthermore, ODRL includes recent off-dynamics RL algorithms in a unified framework and introduces some extra baselines for different settings, all implemented in a single-file manner. To unpack the true adaptation capability of existing methods, we conduct extensive benchmarking experiments, which show that no method has universal advantages across varied dynamics shifts. We hope this benchmark can serve as a cornerstone for future research endeavors. Our code is publicly available at https://github.com/OffDynamicsRL/off-dynamics-rl.