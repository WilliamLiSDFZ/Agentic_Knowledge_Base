---
title: "JaxMARL: Multi-Agent RL Environments and Algorithms in JAX"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/5aee125f052c90e326dcf6f380df94f6-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['reinforcement-learning-optimization-and-decision-making', 'ai-benchmarking-and-evaluation-methodology']
tags: ['multi-agent-reinforcement-learning', 'JAX', 'benchmarking']
venue: "NeurIPS 2024"
tldr: "Introduces JaxMARL, a suite of multi-agent RL environments and algorithms implemented in JAX for scalable GPU-accelerated benchmarking."
---

# JaxMARL: Multi-Agent RL Environments and Algorithms in JAX

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/5aee125f052c90e326dcf6f380df94f6-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/5aee125f052c90e326dcf6f380df94f6-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces JaxMARL, a suite of multi-agent RL environments and algorithms implemented in JAX for scalable GPU-accelerated benchmarking.

## Abstract

Benchmarks are crucial in the development of machine learning algorithms, significantly influencing reinforcement learning (RL) research through the available environments. Traditionally, RL environments run on the CPU, which limits their scalability with the computational resources typically available in academia. However, recent advancements in JAX have enabled the wider use of hardware acceleration, enabling massively parallel RL training pipelines and environments. While this has been successfully applied to single-agent RL, it has not yet been widely adopted for multi-agent scenarios. In this paper, we present JaxMARL, the first open-source, easy-to-use code base that combines GPU-enabled efficiency with support for a large number of commonly used MARL environments and popular baseline algorithms. Our experiments show that, in terms of wall clock time, our JAX-based training pipeline is up to 12,500 times faster than existing approaches. This enables efficient and thorough evaluations, potentially alleviating the evaluation crisis in the field. We also introduce and benchmark SMAX, a vectorised, simplified version of the popular StarCraft Multi-Agent Challenge, which removes the need to run the StarCraft II game engine. This not only enables GPU acceleration, but also provides a more flexible MARL environment, unlocking the potential for self-play, meta-learning, and other future applications in MARL. The code is available at https://github.com/flairox/jaxmarl.