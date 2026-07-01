---
title: "RelBench: A Benchmark for Deep Learning on Relational Databases"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/25cd345233c65fac1fec0ce61d0f7836-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['ai-benchmarking-and-evaluation-methodology', 'graph-neural-networks-and-representation-learning']
tags: ['relational-databases', 'benchmark', 'graph-neural-networks']
venue: "NeurIPS 2024"
tldr: "RelBench is a public benchmark for deep learning on relational databases spanning diverse domains and predictive tasks."
---

# RelBench: A Benchmark for Deep Learning on Relational Databases

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/25cd345233c65fac1fec0ce61d0f7836-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/25cd345233c65fac1fec0ce61d0f7836-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: RelBench is a public benchmark for deep learning on relational databases spanning diverse domains and predictive tasks.

## Abstract

We present RelBench, a public benchmark for solving predictive tasks in relational databases with deep learning.  RelBench provides databases and tasks spanning diverse domains, scales, and database dimensions, and is intended to be a foundational infrastructure for future research in this direction. We use RelBench to conduct the first comprehensive empirical study of graph neural network (GNN) based predictive models on relational data, as recently proposed by Fey et al. 2024.  End-to-end learned GNNs are capable fully exploiting the predictive signal encoded in links between entities, marking a significant shift away from the dominant paradigm of manual feature engineering combined with tabular machine learning. To thoroughly evaluate GNNs against the prior gold-standard we conduct a user study, where an experienced data scientist manually engineers features for each task. In this study, GNNs learn better models whilst reducing human work needed by more than an order of magnitude. This result demonstrates the power of GNNs for solving predictive tasks in relational databases, opening up new research opportunities.