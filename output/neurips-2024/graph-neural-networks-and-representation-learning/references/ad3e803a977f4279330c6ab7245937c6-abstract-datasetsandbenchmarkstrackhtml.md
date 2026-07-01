---
title: "ProG: A Graph Prompt Learning Benchmark"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/ad3e803a977f4279330c6ab7245937c6-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['graph-neural-networks-and-representation-learning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['graph-prompts', 'benchmark', 'few-shot-learning']
venue: "NeurIPS 2024"
tldr: "Introduces ProG, a comprehensive benchmark for evaluating graph prompt learning methods across diverse tasks and settings."
---

# ProG: A Graph Prompt Learning Benchmark

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/ad3e803a977f4279330c6ab7245937c6-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/ad3e803a977f4279330c6ab7245937c6-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces ProG, a comprehensive benchmark for evaluating graph prompt learning methods across diverse tasks and settings.

## Abstract

Artificial general intelligence on graphs has shown significant advancements across various applications, yet the traditional `Pre-train &amp; Fine-tune' paradigm faces inefficiencies and negative transfer issues, particularly in complex and few-shot settings. Graph prompt learning emerges as a promising alternative, leveraging lightweight prompts to manipulate data and fill the task gap by reformulating downstream tasks to the pretext. However, several critical challenges still remain: how to unify diverse graph prompt models, how to evaluate the quality of graph prompts, and to improve their usability for practical comparisons and selection. In response to these challenges, we introduce the first comprehensive benchmark for graph prompt learning. Our benchmark integrates SIX pre-training methods and FIVE state-of-the-art graph prompt techniques, evaluated across FIFTEEN diverse datasets to assess performance, flexibility, and efficiency. We also present 'ProG', an easy-to-use open-source library that streamlines the execution of various graph prompt models, facilitating objective evaluations. Additionally, we propose a unified framework that categorizes existing graph prompt methods into two main approaches: prompts as graphs and prompts as tokens. This framework enhances the applicability and comparison of graph prompt techniques. The code is available at: https://github.com/sheldonresearch/ProG.