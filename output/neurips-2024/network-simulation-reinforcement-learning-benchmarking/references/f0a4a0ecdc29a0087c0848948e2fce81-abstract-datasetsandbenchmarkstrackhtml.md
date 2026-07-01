---
title: "WFCRL: A Multi-Agent Reinforcement Learning Benchmark for Wind Farm Control"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f0a4a0ecdc29a0087c0848948e2fce81-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['network-simulation-reinforcement-learning-benchmarking']
tags: ['wind-farm-control', 'multi-agent-reinforcement-learning', 'benchmark']
venue: "NeurIPS 2024"
tldr: "WFCRL is a multi-agent reinforcement learning benchmark for wind farm control that captures complex aerodynamic turbine interactions."
---

# WFCRL: A Multi-Agent Reinforcement Learning Benchmark for Wind Farm Control

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f0a4a0ecdc29a0087c0848948e2fce81-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/f0a4a0ecdc29a0087c0848948e2fce81-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: WFCRL is a multi-agent reinforcement learning benchmark for wind farm control that captures complex aerodynamic turbine interactions.

## Abstract

The wind farm control problem is challenging, since conventional model-based control strategies require tractable models of complex aerodynamical interactions between the turbines and suffer from the curse of dimension when the number of turbines increases. Recently, model-free and multi-agent reinforcement learning approaches have been used to address this challenge. In this article, we introduce WFCRL (Wind Farm Control with Reinforcement Learning), the first suite of multi-agent reinforcement learning environments for the wind farm control problem. WFCRL frames a cooperative Multi-Agent Reinforcement Learning (MARL) problem: each turbine is an agent and can learn to adjust its yaw, pitch or torque to maximize the common objective (e.g. the total power production of the farm). WFCRL also offers turbine load observations that will allow to optimize the farm performance while limiting turbine structural damages. Interfaces with two state-of-the-art farm simulators are implemented in WFCRL: a static simulator (Floris) and a dynamic simulator (FAST.farm). For each simulator, $10$ wind layouts are provided, including $5$ real wind farms. Two state-of-the-art online MARL algorithms are implemented to illustrate the scaling challenges. As learning online on FAST.Farm is highly time-consuming, WFCRL offers the possibility of designing transfer learning strategies from Floris to FAST.Farm.