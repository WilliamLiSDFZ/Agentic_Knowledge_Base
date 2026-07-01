---
title: "GC-Bench: An Open and Unified Benchmark for Graph Condensation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/42ed003e72eab5136e3d2fdbef4b8d7b-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology']
tags: ['graph-condensation', 'benchmark', 'evaluation']
venue: "NeurIPS 2024"
tldr: "Introduces GC-Bench, an open unified benchmark for systematically evaluating graph condensation methods across diverse settings."
---

# GC-Bench: An Open and Unified Benchmark for Graph Condensation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/42ed003e72eab5136e3d2fdbef4b8d7b-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/42ed003e72eab5136e3d2fdbef4b8d7b-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces GC-Bench, an open unified benchmark for systematically evaluating graph condensation methods across diverse settings.

## Abstract

Graph condensation (GC) has recently garnered considerable attention due to its ability to reduce large-scale graph datasets while preserving their essential properties. The core concept of GC is to create a smaller, more manageable graph that retains the characteristics of the original graph. Despite the proliferation of graph condensation methods developed in recent years, there is no comprehensive evaluation and in-depth analysis, which creates a great obstacle to understanding the progress in this field. To fill this gap, we develop a comprehensive Graph Condensation Benchmark (GC-Bench) to analyze the performance of graph condensation in different scenarios systematically. Specifically, GC-Bench systematically investigates the characteristics of graph condensation in terms of the following dimensions: effectiveness, transferability, and complexity. We comprehensively evaluate 12 state-of-the-art graph condensation algorithms in node-level and graph-level tasks and analyze their performance in 12 diverse graph datasets. Further, we have developed an easy-to-use library for training and evaluating different GC methods to facilitate reproducible research.The GC-Bench library is available at https://github.com/RingBDStack/GC-Bench.