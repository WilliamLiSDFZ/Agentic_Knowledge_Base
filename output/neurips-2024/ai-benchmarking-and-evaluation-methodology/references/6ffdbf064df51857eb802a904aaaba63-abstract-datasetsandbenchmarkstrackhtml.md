---
title: "HW-GPT-Bench: Hardware-Aware Architecture Benchmark for Language Models"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/6ffdbf064df51857eb802a904aaaba63-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'llm-training-and-optimization-techniques']
tags: ['hardware-aware-nas', 'language-model-benchmarking', 'latency-energy-tradeoffs']
venue: "NeurIPS 2024"
tldr: "A benchmark for evaluating language model architectures across hardware metrics including latency, energy, and GPU memory under specific constraints."
---

# HW-GPT-Bench: Hardware-Aware Architecture Benchmark for Language Models

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/6ffdbf064df51857eb802a904aaaba63-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/6ffdbf064df51857eb802a904aaaba63-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A benchmark for evaluating language model architectures across hardware metrics including latency, energy, and GPU memory under specific constraints.

## Abstract

The increasing size of language models necessitates a thorough analysis across multiple dimensions to assess trade-offs among crucial hardware metrics such as latency, energy consumption, GPU memory usage, and performance. Identifying optimal model configurations under specific hardware constraints is becoming essential but remains challenging due to the computational load of exhaustive training and evaluation on multiple devices. To address this, we introduce HW-GPT-Bench, a hardware-aware benchmark that utilizes surrogate predictions to approximate various hardware metrics across 13 devices of architectures in the GPT-2 family, with architectures containing up to 1.55B parameters. Our surrogates, via calibrated predictions and reliable uncertainty estimates, faithfully model the heteroscedastic noise inherent in the energy and latency measurements. To estimate perplexity, we employ weight-sharing techniques from Neural Architecture Search (NAS), inheriting pretrained weights from the largest GPT-2 model. Finally, we demonstrate the utility of HW-GPT-Bench by simulating optimization trajectories of various multi-objective optimization algorithms in just a few seconds.