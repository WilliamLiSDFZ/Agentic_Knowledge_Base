---
title: "Revisiting, Benchmarking and Understanding Unsupervised Graph Domain Adaptation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a2c548b2ed3141400d86a235eaa6fad0-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['graph-neural-networks-and-representation-learning']
tags: ['graph-domain-adaptation', 'benchmarking', 'unsupervised-transfer']
venue: "NeurIPS 2024"
tldr: "Revisits and benchmarks unsupervised graph domain adaptation methods under standardized experimental settings to enable fair performance comparison."
---

# Revisiting, Benchmarking and Understanding Unsupervised Graph Domain Adaptation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a2c548b2ed3141400d86a235eaa6fad0-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/a2c548b2ed3141400d86a235eaa6fad0-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Revisits and benchmarks unsupervised graph domain adaptation methods under standardized experimental settings to enable fair performance comparison.

## Abstract

Unsupervised Graph Domain Adaptation (UGDA) involves the transfer of knowledge from a label-rich source graph to an unlabeled target graph under domain discrepancies. Despite the proliferation of methods designed for this emerging task, the lack of standard experimental settings and fair performance comparisons makes it challenging to understand which and when models perform well across different scenarios. To fill this gap, we present the first comprehensive benchmark for unsupervised graph domain adaptation named GDABench, which encompasses 16 algorithms across diverse adaptation tasks. Through extensive experiments, we observe that the performance of current UGDA models varies significantly across different datasets and adaptation scenarios. Specifically, we recognize that when the source and target graphs face significant distribution shifts, it is imperative to formulate strategies to effectively address and mitigate graph structural shifts. We also find that with appropriate neighbourhood aggregation mechanisms, simple GNN variants can even surpass state-of-the-art UGDA baselines. To facilitate reproducibility, we have developed an easy-to-use library PyGDA for training and evaluating existing UGDA methods, providing a standardized platform in this community. Our source codes and datasets can be found at https://github.com/pygda-team/pygda.