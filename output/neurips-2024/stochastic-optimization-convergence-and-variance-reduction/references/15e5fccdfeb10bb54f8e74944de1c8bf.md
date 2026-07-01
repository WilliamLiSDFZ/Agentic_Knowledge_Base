---
title: "HyperPrism: An Adaptive Non-linear Aggregation Framework for Distributed Machine Learning over Non-IID Data and Time-varying Communication Links"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/15e5fccdfeb10bb54f8e74944de1c8bf-Abstract-Conference.html"
categories: ['privacy-preserving-federated-distributed-learning', 'stochastic-optimization-convergence-and-variance-reduction']
tags: ['distributed-machine-learning', 'non-IID-data', 'non-linear-aggregation']
venue: "NeurIPS 2024"
tldr: "Introduces HyperPrism, an adaptive non-linear aggregation framework for distributed learning over non-IID data and time-varying communication links."
---

# HyperPrism: An Adaptive Non-linear Aggregation Framework for Distributed Machine Learning over Non-IID Data and Time-varying Communication Links

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/15e5fccdfeb10bb54f8e74944de1c8bf-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/15e5fccdfeb10bb54f8e74944de1c8bf-Abstract-Conference.html)

**TLDR**: Introduces HyperPrism, an adaptive non-linear aggregation framework for distributed learning over non-IID data and time-varying communication links.

## Abstract

While Distributed Machine Learning (DML) has been widely used to achieve decent performance, it is still challenging to take full advantage of data and devices distributed at multiple vantage points to adapt and learn, especially it is non-trivial to address dynamic and divergence challenges based on the linear aggregation framework as follows: (1) heterogeneous learning data at different devices (i.e., non-IID data) resulting in model divergence and (2) in the case of time-varying communication links, the limited ability for devices to reconcile model divergence. In this paper, we contribute a non-linear class aggregation framework HyperPrism that leverages distributed mirror descent with averaging done in the mirror descent dual space and adapts the degree of Weighted Power Mean (WPM) used in each round. Moreover, HyperPrism could adaptively choose different mapping for different layers of the local model with a dedicated hypernetwork per device, achieving automatic optimization of DML in high divergence settings. We perform rigorous analysis and experimental evaluations to demonstrate the effectiveness of adaptive, mirror-mapping DML. In particular, we extend the generalizability of existing related works and position them as special cases within HyperPrism. Our experimental results show that HyperPrism can improve the convergence speed up to 98.63% and scale well to more devices compared with the state-of-the-art, all with little additional computation overhead compared to traditional linear aggregation.