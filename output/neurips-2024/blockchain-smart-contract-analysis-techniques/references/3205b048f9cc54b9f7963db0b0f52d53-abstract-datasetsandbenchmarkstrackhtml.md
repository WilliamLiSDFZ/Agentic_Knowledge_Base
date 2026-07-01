---
title: "Multi-Chain Graphs of Graphs: A New Approach to Analyzing Blockchain Datasets"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/3205b048f9cc54b9f7963db0b0f52d53-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['blockchain-smart-contract-analysis-techniques', 'graph-neural-networks-and-representation-learning']
tags: ['blockchain', 'graph-neural-networks', 'cross-chain-dataset']
venue: "NeurIPS 2024"
tldr: "A large-scale cross-chain dataset with hierarchical graph-level data enabling machine learning analysis across multiple blockchain networks."
---

# Multi-Chain Graphs of Graphs: A New Approach to Analyzing Blockchain Datasets

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/3205b048f9cc54b9f7963db0b0f52d53-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/3205b048f9cc54b9f7963db0b0f52d53-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: A large-scale cross-chain dataset with hierarchical graph-level data enabling machine learning analysis across multiple blockchain networks.

## Abstract

Machine learning applied to blockchain graphs offers significant opportunities for enhanced data analysis and applications. However, the potential of this field is constrained by the lack of a large-scale, cross-chain dataset that includes hierarchical graph-level data. To address this issue, we present novel datasets that provide detailed label information at the token level and integrate interactions between tokens across multiple blockchain platforms. We model transactions within each token as local graphs and the relationships between tokens as global graphs, collectively forming a "Graphs of Graphs" (GoG) approach. This innovative approach facilitates a deeper understanding of systemic structures and hierarchical interactions, which are essential for applications such as link prediction, anomaly detection, and token classification. We conduct a series of experiments demonstrating that this dataset delivers new insights and challenges for exploring GoG within the blockchain domain. Our work promotes advancements and opens new avenues for research in both the blockchain and graph communities. Source code and datasets are available at https://github.com/Xtra-Computing/Cryptocurrency-Graphs-of-graphs.