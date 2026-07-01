---
title: "A Simulation Benchmark for Autonomous Racing with Large-Scale Human Data"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/b91ea2ba1b6521940e204b7b81d5ef47-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['autonomous-driving-and-trajectory-prediction', 'reinforcement-learning-optimization-and-decision-making']
tags: ['autonomous-racing', 'simulation-benchmark', 'human-driving-data']
venue: "NeurIPS 2024"
tldr: "A simulation benchmark for autonomous racing featuring large-scale human driving data to support research on near-limit vehicle control."
---

# A Simulation Benchmark for Autonomous Racing with Large-Scale Human Data

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/b91ea2ba1b6521940e204b7b81d5ef47-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/b91ea2ba1b6521940e204b7b81d5ef47-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A simulation benchmark for autonomous racing featuring large-scale human driving data to support research on near-limit vehicle control.

## Abstract

Despite the availability of international prize-money competitions, scaled vehicles, and simulation environments, research on autonomous racing and the control of sports cars operating close to the limit of handling has been limited by the high costs of vehicle acquisition and management, as well as the limited physics accuracy of open-source simulators. In this paper, we propose a racing simulation platform based on the simulator Assetto Corsa to test, validate, and benchmark autonomous driving algorithms, including reinforcement learning (RL) and classical Model Predictive Control (MPC), in realistic and challenging scenarios. Our contributions include the development of this simulation platform, several state-of-the-art algorithms tailored to the racing environment, and a comprehensive dataset collected from human drivers. Additionally, we evaluate algorithms in the offline RL setting. All the necessary code (including environment and benchmarks), working examples, and datasets are publicly released and can be found at: https://github.com/dasGringuen/assettocorsagym.