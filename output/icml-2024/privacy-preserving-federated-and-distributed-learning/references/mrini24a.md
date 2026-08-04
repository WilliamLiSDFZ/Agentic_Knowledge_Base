---
title: "Privacy Attacks in Decentralized Learning"
source: "https://proceedings.mlr.press/v235/mrini24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/mrini24a/mrini24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'adversarial-robustness-and-model-security']
tags: ['decentralized-learning', 'privacy-attacks', 'gradient-descent', 'network-graph']
venue: "ICML 2024"
tldr: "Privacy attacks on decentralized gradient descent are shown to be feasible even between non-neighboring nodes, challenging the assumed privacy benefits of decentralized learning."
---

# Privacy Attacks in Decentralized Learning

**Source**: [https://proceedings.mlr.press/v235/mrini24a.html](https://proceedings.mlr.press/v235/mrini24a.html)

**TLDR**: Privacy attacks on decentralized gradient descent are shown to be feasible even between non-neighboring nodes, challenging the assumed privacy benefits of decentralized learning.

## Abstract

Decentralized Gradient Descent (D-GD) allows a set of users to perform collaborative learning without sharing their data by iteratively averaging local model updates with their neighbors in a network graph. The absence of direct communication between non-neighbor nodes might lead to the belief that users cannot infer precise information about the data of others. In this work, we demonstrate the opposite, by proposing the first attack against D-GD that enables a user (or set of users) to reconstruct the private data of other users outside their immediate neighborhood. Our approach is based on a reconstruction attack against the gossip averaging protocol, which we then extend to handle the additional challenges raised by D-GD. We validate the effectiveness of our attack on real graphs and datasets, showing that the number of users compromised by a single or a handful of attackers is often surprisingly large. We empirically investigate some of the factors that affect the performance of the attack, namely the graph topology, the number of attackers, and their position in the graph.