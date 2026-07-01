---
title: "Benchmarking Structural Inference Methods for Interacting Dynamical Systems with Synthetic Data"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f3c812da38d1bc796cb2e8235eee96bf-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'graph-neural-networks-and-representation-learning']
tags: ['structural-inference', 'dynamical-systems', 'benchmark']
venue: "NeurIPS 2024"
tldr: "Provides a synthetic benchmark for evaluating structural inference methods on interacting dynamical systems across domains."
---

# Benchmarking Structural Inference Methods for Interacting Dynamical Systems with Synthetic Data

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f3c812da38d1bc796cb2e8235eee96bf-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/f3c812da38d1bc796cb2e8235eee96bf-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Provides a synthetic benchmark for evaluating structural inference methods on interacting dynamical systems across domains.

## Abstract

Understanding complex dynamical systems begins with identifying their topological structures, which expose the organization of the systems. This requires robust structural inference methods that can deduce structure from observed behavior. However, existing methods are often domain-specific and lack a standardized, objective comparison framework. We address this gap by benchmarking 13 structural inference methods from various disciplines on simulations representing two types of dynamics and 11 interaction graph models, supplemented by a biological experimental dataset to mirror real-world application. We evaluated the methods for accuracy, scalability, robustness, and sensitivity to graph properties. Our findings indicate that deep learning methods excel with multi-dimensional data, while classical statistics and information theory based approaches are notably accurate and robust. Additionally, performance correlates positively with the graph's average shortest path length. This benchmark should aid researchers in selecting suitable methods for their specific needs and stimulate further methodological innovation.