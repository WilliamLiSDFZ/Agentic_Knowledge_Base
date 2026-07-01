---
title: "What Is Missing For Graph Homophily? Disentangling Graph Homophily For Graph Neural Networks"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/7e810b2c75d69be186cadd2fe3febeab-Abstract-Conference.html"
categories: ['graph-neural-networks-and-representation-learning', 'disentangled-representation-learning-cognitive-diagnosis']
tags: ['graph-homophily', 'graph-neural-networks', 'disentanglement', 'homophily-metrics', 'node-classification']
venue: "NeurIPS 2024"
tldr: "Disentangles graph homophily into finer components to better understand and improve GNN design beyond standard homophily metrics."
---

# What Is Missing For Graph Homophily? Disentangling Graph Homophily For Graph Neural Networks

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/7e810b2c75d69be186cadd2fe3febeab-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/7e810b2c75d69be186cadd2fe3febeab-Abstract-Conference.html)

**TLDR**: Disentangles graph homophily into finer components to better understand and improve GNN design beyond standard homophily metrics.

## Abstract

Graph homophily refers to the phenomenon that connected nodes tend to share similar characteristics. Understanding this concept and its related metrics is crucial for designing effective Graph Neural Networks (GNNs). The most widely used homophily metrics, such as edge or node homophily, quantify such "similarity" as label consistency across the graph topology. These metrics are believed to be able to reflect the performance of GNNs, especially on node-level tasks. However, many recent studies have empirically demonstrated that the performance of GNNs does not always align with homophily metrics, and how homophily influences GNNs still remains unclear and controversial. Then, a crucial question arises: What is missing in our current understanding of homophily? To figure out the missing part, in this paper, we disentangle the graph homophily into three aspects: label, structural, and feature homophily, which are derived from the three basic elements of graph data. We argue that the synergy of the three homophily can provide a more comprehensive understanding of GNN performance. Our new proposed structural and feature homophily consider the neighborhood consistency and feature dependencies among nodes, addressing the previously overlooked structural and feature aspects in graph homophily. To investigate their synergy, we propose a Contextual Stochastic Block Model with three types of Homophily (CSBM-3H), where the topology and feature generation are controlled by the three metrics. Based on the theoretical analysis of CSBM-3H, we derive a new composite metric, named Tri-Hom, that considers all three aspects and overcomes the limitations of conventional homophily metrics. The theoretical conclusions and the effectiveness of Tri-Hom have been verified through synthetic experiments on CSBM-3H. In addition, we conduct experiments on $31$ real-world benchmark datasets and calculate the correlations between homophily metrics and model performance. Tri-Hom has significantly higher correlation values than $17$ existing metrics that only focus on a single homophily aspect, demonstrating its superiority and the importance of homophily synergy. Our code is available at https://github.com/zylMozart/Disentangle_GraphHom.