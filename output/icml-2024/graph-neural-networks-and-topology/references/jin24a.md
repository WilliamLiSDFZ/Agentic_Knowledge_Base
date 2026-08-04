---
title: "Homomorphism Counts for Graph Neural Networks: All About That Basis"
source: "https://proceedings.mlr.press/v235/jin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jin24a/jin24a.pdf"
categories: ['graph-neural-networks-and-topology', 'algebraic-structures-in-machine-learning']
tags: ['graph-neural-networks', 'homomorphism-counts', 'expressive-power', 'basis']
venue: "ICML 2024"
tldr: "A basis-theoretic analysis of homomorphism counts reveals fundamental properties and limitations of graph neural network expressiveness."
---

# Homomorphism Counts for Graph Neural Networks: All About That Basis

**Source**: [https://proceedings.mlr.press/v235/jin24a.html](https://proceedings.mlr.press/v235/jin24a.html)

**TLDR**: A basis-theoretic analysis of homomorphism counts reveals fundamental properties and limitations of graph neural network expressiveness.

## Abstract

A large body of work has investigated the properties of graph neural networks and identified several limitations, particularly pertaining to their expressive power. Their inability to count certain patterns (e.g., cycles) in a graph lies at the heart of such limitations, since many functions to be learned rely on the ability of counting such patterns. Two prominent paradigms aim to address this limitation by enriching the graph features with subgraph or homomorphism pattern counts. In this work, we show that both of these approaches are sub-optimal in a certain sense and argue for a more fine-grained approach, which incorporates the homomorphism counts of all structures in the “basis” of the target pattern. This yields strictly more expressive architectures without incurring any additional overhead in terms of computational complexity compared to existing approaches. We prove a series of theoretical results on node-level and graph-level motif parameters and empirically validate them on standard benchmark datasets.