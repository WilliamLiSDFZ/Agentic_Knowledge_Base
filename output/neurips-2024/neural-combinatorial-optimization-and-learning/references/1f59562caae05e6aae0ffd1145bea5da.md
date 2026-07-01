---
title: "The Map Equation Goes Neural: Mapping Network Flows with Graph Neural Networks"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/1f59562caae05e6aae0ffd1145bea5da-Abstract-Conference.html"
categories: ['graph-neural-networks-and-representation-learning', 'neural-combinatorial-optimization-and-learning']
tags: ['community-detection', 'map-equation', 'graph-neural-networks']
venue: "NeurIPS 2024"
tldr: "Integrates the map equation objective into a graph neural network framework for differentiable and scalable community detection."
---

# The Map Equation Goes Neural: Mapping Network Flows with Graph Neural Networks

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/1f59562caae05e6aae0ffd1145bea5da-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/1f59562caae05e6aae0ffd1145bea5da-Abstract-Conference.html)

**TLDR**: Integrates the map equation objective into a graph neural network framework for differentiable and scalable community detection.

## Abstract

Community detection is an essential tool for unsupervised data exploration and revealing the organisational structure of networked systems. With a long history in network science, community detection typically relies on objective functions, optimised with custom-tailored search algorithms, but often without leveraging recent advances in deep learning. Recently, first works have started incorporating such objectives into loss functions for deep graph clustering and pooling. We consider the map equation, a popular information-theoretic objective function for unsupervised community detection, and express it in differentiable tensor form for optimisation through gradient descent. Our formulation turns the map equation compatible with any neural network architecture, enables end-to-end learning, incorporates node features, and chooses the optimal number of clusters automatically, all without requiring explicit regularisation. Applied to unsupervised graph clustering tasks, we achieve competitive performance against state-of-the-art deep graph clustering baselines in synthetic and real-world datasets.