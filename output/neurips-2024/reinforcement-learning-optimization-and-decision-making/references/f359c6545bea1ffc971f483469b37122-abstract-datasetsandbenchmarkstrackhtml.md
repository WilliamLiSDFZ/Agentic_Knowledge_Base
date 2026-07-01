---
title: "CALE: Continuous Arcade Learning Environment"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f359c6545bea1ffc971f483469b37122-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'ai-benchmarking-and-evaluation-methodology']
tags: ['arcade-learning-environment', 'continuous-actions', 'reinforcement-learning-benchmark']
venue: "NeurIPS 2024"
tldr: "Extends the Arcade Learning Environment to support continuous action spaces for reinforcement learning research."
---

# CALE: Continuous Arcade Learning Environment

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f359c6545bea1ffc971f483469b37122-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/f359c6545bea1ffc971f483469b37122-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Extends the Arcade Learning Environment to support continuous action spaces for reinforcement learning research.

## Abstract

We introduce the Continuous Arcade Learning Environment (CALE), an extension of the well-known Arcade Learning Environment (ALE) [Bellemare et al., 2013]. The CALE uses the same underlying emulator of the Atari 2600 gaming system (Stella), but adds support for continuous actions. This enables the benchmarking and evaluation of continuous-control agents (such as PPO [Schulman et al., 2017] and SAC [Haarnoja et al., 2018]) and value-based agents (such as DQN [Mnih et al., 2015] and Rainbow [Hessel et al., 2018]) on the same environment suite. We provide a series of open questions and research directions that CALE enables, as well as initial baseline results using Soft Actor-Critic. CALE is available as part of the ALE athttps://github.com/Farama-Foundation/Arcade-Learning-Environment.