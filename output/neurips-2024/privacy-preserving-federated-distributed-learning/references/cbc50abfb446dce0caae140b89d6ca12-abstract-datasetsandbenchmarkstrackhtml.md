---
title: "DECO-Bench: Unified Benchmark for Decoupled Task-Agnostic Synthetic Data Release"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/cbc50abfb446dce0caae140b89d6ca12-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['privacy-preserving-federated-distributed-learning']
tags: ['synthetic-data', 'privacy-preserving', 'benchmarking']
venue: "NeurIPS 2024"
tldr: "Introduces DECO-Bench, a unified benchmark for evaluating task-agnostic decoupling methods for privacy-preserving dataset sharing."
---

# DECO-Bench: Unified Benchmark for Decoupled Task-Agnostic Synthetic Data Release

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/cbc50abfb446dce0caae140b89d6ca12-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/cbc50abfb446dce0caae140b89d6ca12-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces DECO-Bench, a unified benchmark for evaluating task-agnostic decoupling methods for privacy-preserving dataset sharing.

## Abstract

In this work, we tackle the question of how to systematically benchmark task-agnostic decoupling methods for privacy-preserving machine learning (ML). Sharing datasets that include sensitive information often triggers privacy concerns, necessitating robust decoupling methods to separate sensitive and non-sensitive attributes. Despite the development of numerous decoupling techniques, a standard benchmark for systematically comparing these methods remains absent. Our framework integrates various decoupling techniques along with synthetic datageneration and evaluation protocols within a unified system. Using our framework, we benchmark various decoupling techniques and evaluate their privacy-utility trade-offs. Finally, we release our source code, pre-trained models, datasets of decoupled representations to foster research in this area.