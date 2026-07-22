---
title: "CACL: Community-Aware Heterogeneous Graph Contrastive Learning for Social Media Bot Detection"
source: "https://aclanthology.org/2024.findings-acl.617/"
categories: ['graph-based-social-bot-detection', 'llm-reasoning-and-knowledge-graph-benchmarks']
tags: ['bot-detection', 'heterogeneous-graph', 'community-aware']
venue: "ACL 2024"
tldr: "Proposes CACL, a community-aware heterogeneous graph contrastive learning method for social media bot detection."
---

# CACL: Community-Aware Heterogeneous Graph Contrastive Learning for Social Media Bot Detection

**Source**: [https://aclanthology.org/2024.findings-acl.617/](https://aclanthology.org/2024.findings-acl.617/)

**TLDR**: Proposes CACL, a community-aware heterogeneous graph contrastive learning method for social media bot detection.

## Abstract

AbstractSocial media bot detection is increasingly crucial with the rise of social media platforms. Existing methods predominantly construct social networks as graph and utilize graph neural networks (GNNs) for bot detection. However, most of these methods focus on how to improve the performance of GNNs while neglecting the community structure within social networks. Moreover, GNNs based methods still face problems such as poor model generalization due to the relatively small scale of the dataset and over-smoothness caused by information propagation mechanism. To address these problems, we propose the Community-Aware Heterogeneous Graph Contrastive Learning framework (i.e., CACL), which constructs social network as heterogeneous graph with multiple node types and edge types, and then utilizes community-aware module to mine both hard positive samples and hard negative samples for supervised graph contrastive learning with adaptive graph enhancement algorithms. Extensive experiments demonstrate that our framework addresses the previously mentioned challenges and outperforms competitive baselines on three social media bot benchmarks.