---
title: "Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/b10ed15ff1aa864f1be3a75f1ffc021b-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['graph-neural-networks-and-representation-learning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['graph-neural-networks', 'node-classification', 'graph-transformers', 'benchmarking', 'baselines']
venue: "NeurIPS 2024"
tldr: "Classic GNNs with proper tuning remain strong baselines for node classification, challenging claims of Graph Transformer superiority."
---

# Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/b10ed15ff1aa864f1be3a75f1ffc021b-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/b10ed15ff1aa864f1be3a75f1ffc021b-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Classic GNNs with proper tuning remain strong baselines for node classification, challenging claims of Graph Transformer superiority.

## Abstract

Graph Transformers (GTs) have recently emerged as popular alternatives to traditional message-passing Graph Neural Networks (GNNs), due to their theoretically superior expressiveness and impressive performance reported on standard node classification benchmarks, often significantly outperforming GNNs. In this paper, we conduct a thorough empirical analysis to reevaluate the performance of three classic GNN models (GCN, GAT, and GraphSAGE) against GTs. Our findings suggest that the previously reported superiority of GTs may have been overstated due to suboptimal hyperparameter configurations in GNNs. Remarkably, with slight hyperparameter tuning, these classic GNN models achieve state-of-the-art performance, matching or even exceeding that of recent GTs across 17 out of the 18 diverse datasets examined. Additionally, we conduct detailed ablation studies to investigate the influence of various GNN configurations—such as normalization, dropout, residual connections, and network depth—on node classification performance. Our study aims to promote a higher standard of empirical rigor in the field of graph machine learning, encouraging more accurate comparisons and evaluations of model capabilities. Our implementation is available at https://github.com/LUOyk1999/tunedGNN.