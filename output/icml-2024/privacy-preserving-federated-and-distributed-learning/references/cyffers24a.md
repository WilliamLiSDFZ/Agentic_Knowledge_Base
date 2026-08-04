---
title: "Differentially Private Decentralized Learning with Random Walks"
source: "https://proceedings.mlr.press/v235/cyffers24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cyffers24a/cyffers24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'online-learning-and-sequential-decision-making']
tags: ['differential-privacy', 'decentralized-learning', 'random-walks']
venue: "ICML 2024"
tldr: "Analyzes differentially private decentralized learning with random walk gossip protocols, characterizing privacy-utility tradeoffs."
---

# Differentially Private Decentralized Learning with Random Walks

**Source**: [https://proceedings.mlr.press/v235/cyffers24a.html](https://proceedings.mlr.press/v235/cyffers24a.html)

**TLDR**: Analyzes differentially private decentralized learning with random walk gossip protocols, characterizing privacy-utility tradeoffs.

## Abstract

The popularity of federated learning comes from the possibility of better scalability and the ability for participants to keep control of their data, improving data security and sovereignty. Unfortunately, sharing model updates also creates a new privacy attack surface. In this work, we characterize the privacy guarantees of decentralized learning with random walk algorithms, where a model is updated by traveling from one node to another along the edges of a communication graph. Using a recent variant of differential privacy tailored to the study of decentralized algorithms, namely Pairwise Network Differential Privacy, we derive closed-form expressions for the privacy loss between each pair of nodes where the impact of the communication topology is captured by graph theoretic quantities. Our results further reveal that random walk algorithms tends to yield better privacy guarantees than gossip algorithms for nodes close from each other. We supplement our theoretical results with empirical evaluation on synthetic and real-world graphs and datasets.