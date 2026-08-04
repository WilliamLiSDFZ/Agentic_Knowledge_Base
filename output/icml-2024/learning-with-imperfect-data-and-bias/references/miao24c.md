---
title: "Rethinking Independent Cross-Entropy Loss For Graph-Structured Data"
source: "https://proceedings.mlr.press/v235/miao24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/miao24c/miao24c.pdf"
categories: ['graph-neural-networks-and-topology', 'learning-with-imperfect-data-and-bias']
tags: ['graph-neural-networks', 'node-classification', 'cross-entropy-loss']
venue: "ICML 2024"
tldr: "Rethinks the independent cross-entropy loss for graph-structured data by exploiting label correlations among connected nodes."
---

# Rethinking Independent Cross-Entropy Loss For Graph-Structured Data

**Source**: [https://proceedings.mlr.press/v235/miao24c.html](https://proceedings.mlr.press/v235/miao24c.html)

**TLDR**: Rethinks the independent cross-entropy loss for graph-structured data by exploiting label correlations among connected nodes.

## Abstract

Graph neural networks (GNNs) have exhibited prominent performance in learning graph-structured data. Considering node classification task, based on the i.i.d assumption among node labels, the traditional supervised learning simply sums up cross-entropy losses of the independent training nodes and applies the average loss to optimize GNNs’ weights. But different from other data formats, the nodes are naturally connected. It is found that the independent distribution modeling of node labels restricts GNNs’ capability to generalize over the entire graph and defend adversarial attacks. In this work, we propose a new framework, termed joint-cluster supervised learning, to model the joint distribution of each node with its corresponding cluster. We learn the joint distribution of node and cluster labels conditioned on their representations, and train GNNs with the obtained joint loss. In this way, the data-label reference signals extracted from the local cluster explicitly strengthen the discrimination ability on the target node. The extensive experiments demonstrate that our joint-cluster supervised learning can effectively bolster GNNs’ node classification accuracy. Furthermore, being benefited from the reference signals which may be free from spiteful interference, our learning paradigm significantly protects the node classification from being affected by the adversarial attack.