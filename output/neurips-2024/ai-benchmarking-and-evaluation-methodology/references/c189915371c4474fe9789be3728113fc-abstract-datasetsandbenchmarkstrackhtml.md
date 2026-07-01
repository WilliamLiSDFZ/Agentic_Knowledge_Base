---
title: "StreamBench: Towards Benchmarking Continuous Improvement of Language Agents"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/c189915371c4474fe9789be3728113fc-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'online-learning-augmented-algorithms-and-optimization']
tags: ['LLM-agent', 'continuous-improvement', 'benchmarking', 'online-learning', 'self-improvement']
venue: "NeurIPS 2024"
tldr: "Introduces StreamBench to evaluate language agents' ability to continuously improve from experience post-deployment."
---

# StreamBench: Towards Benchmarking Continuous Improvement of Language Agents

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/c189915371c4474fe9789be3728113fc-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/c189915371c4474fe9789be3728113fc-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces StreamBench to evaluate language agents' ability to continuously improve from experience post-deployment.

## Abstract

Recent works have shown that large language model (LLM) agents are able to improve themselves from experience, which is an important ability for continuous enhancement post-deployment. However, existing benchmarks primarily evaluate their innate capabilities and do not assess their ability to improve over time. To address this gap, we introduce StreamBench, a pioneering benchmark designed to evaluate the continuous improvement of LLM agents over an input-feedback sequence. StreamBench simulates an online learning environment where LLMs receive a continuous flow of feedback stream and iteratively enhance their performance. In addition, we propose several simple yet effective baselines for improving LLMs on StreamBench, and provide a comprehensive analysis to identify critical components that contribute to successful streaming strategies. Our work serves as a stepping stone towards developing effective online learning strategies for LLMs, paving the way for more adaptive AI systems in streaming scenarios.