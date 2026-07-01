---
title: "NetworkGym: Reinforcement Learning Environments for Multi-Access Traffic Management in Network Simulation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/c112271dab20d38b43a1c0669f86b4f6-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['network-simulation-reinforcement-learning-benchmarking', 'reinforcement-learning-optimization-and-decision-making']
tags: ['reinforcement-learning', 'network-simulation', 'multi-access', 'traffic-management', 'benchmark']
venue: "NeurIPS 2024"
tldr: "Presents NetworkGym, an RL environment for benchmarking multi-access traffic management in network simulation."
---

# NetworkGym: Reinforcement Learning Environments for Multi-Access Traffic Management in Network Simulation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/c112271dab20d38b43a1c0669f86b4f6-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/c112271dab20d38b43a1c0669f86b4f6-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Presents NetworkGym, an RL environment for benchmarking multi-access traffic management in network simulation.

## Abstract

Mobile devices such as smartphones, laptops, and tablets can often connect to multiple access networks (e.g., Wi-Fi, LTE, and 5G) simultaneously.Recent advancements facilitate seamless integration of these connections below the transport layer, enhancing the experience for apps that lack inherent multi-path support.This optimization hinges on dynamically determining the traffic distribution across networks for each device, a process referred to as multi-access traffic splitting.This paper introduces NetworkGym, a high-fidelity network environment simulator that facilitates generating multiple network traffic flows and multi-access traffic splitting.This simulator facilitates training and evaluating different RL-based solutions for the multi-access traffic splitting problem.Our initial explorations demonstrate that the majority of existing state-of-the-art offline RL algorithms (e.g. CQL) fail to outperform certain hand-crafted heuristic policies on average.This illustrates the urgent need to evaluate offline RL algorithms against a broader range of benchmarks, rather than relying solely on popular ones such as D4RL.We also propose an extension to the TD3+BC algorithm, named Pessimistic TD3 (PTD3), and demonstrate that it outperforms many state-of-the-art offline RL algorithms.PTD3's behavioral constraint mechanism, which relies on value-function pessimism, is theoretically motivated and relatively simple to implement.We open source our code and offline datasets at github.com/hmomin/networkgym.