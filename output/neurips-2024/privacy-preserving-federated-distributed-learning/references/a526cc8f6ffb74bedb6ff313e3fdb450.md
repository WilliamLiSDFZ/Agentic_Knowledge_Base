---
title: "On provable privacy vulnerabilities of graph representations"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/a526cc8f6ffb74bedb6ff313e3fdb450-Abstract-Conference.html"
categories: ['graph-neural-networks-and-representation-learning', 'privacy-preserving-federated-distributed-learning']
tags: ['graph-neural-networks', 'privacy-attacks', 'structural-vulnerability']
venue: "NeurIPS 2024"
tldr: "Investigates structural privacy vulnerabilities in graph neural network representations, demonstrating provable risks of sensitive information leakage from learned graph embeddings."
---

# On provable privacy vulnerabilities of graph representations

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/a526cc8f6ffb74bedb6ff313e3fdb450-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/a526cc8f6ffb74bedb6ff313e3fdb450-Abstract-Conference.html)

**TLDR**: Investigates structural privacy vulnerabilities in graph neural network representations, demonstrating provable risks of sensitive information leakage from learned graph embeddings.

## Abstract

Graph representation learning (GRL) is critical for extracting insights from complex network structures, but it also raises security concerns due to potential privacy vulnerabilities in these representations. This paper investigates the structural vulnerabilities in graph neural models where sensitive topological information can be inferred through edge reconstruction attacks. Our research primarily addresses the theoretical underpinnings of similarity-based edge reconstruction attacks (SERA), furnishing a non-asymptotic analysis of their reconstruction capacities. Moreover, we present empirical corroboration indicating that such attacks can perfectly reconstruct sparse graphs as graph size increases. Conversely, we establish that sparsity is a critical factor for SERA's effectiveness, as demonstrated through analysis and experiments on (dense) stochastic block models. Finally, we explore the resilience of private graph representations produced via noisy aggregation (NAG) mechanism against SERA. Through theoretical analysis and empirical assessments, we affirm the mitigation of SERA using NAG . In parallel, we also empirically delineate instances wherein SERA demonstrates both efficacy and deficiency in its capacity to function as an instrument for elucidating the trade-off between privacy and utility.