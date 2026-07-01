---
title: "Using Time-Aware Graph Neural Networks to Predict Temporal Centralities in Dynamic Graphs"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/3514dbacaebf0f38b25adfe59ed81a8a-Abstract-Conference.html"
categories: ['graph-neural-networks-and-representation-learning', 'time-series-forecasting-and-analysis']
tags: ['temporal-graphs', 'node-centrality', 'graph-neural-networks']
venue: "NeurIPS 2024"
tldr: "Uses time-aware GNNs to predict temporal node centralities in dynamic graphs more accurately than static methods."
---

# Using Time-Aware Graph Neural Networks to Predict Temporal Centralities in Dynamic Graphs

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/3514dbacaebf0f38b25adfe59ed81a8a-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/3514dbacaebf0f38b25adfe59ed81a8a-Abstract-Conference.html)

**TLDR**: Uses time-aware GNNs to predict temporal node centralities in dynamic graphs more accurately than static methods.

## Abstract

Node centralities play a pivotal role in network science, social network analysis, and recommender systems.In temporal data, static path-based centralities like closeness or betweenness can give misleading results about the true importance of nodes in a temporal graph. To address this issue, temporal generalizations of betweenness and closeness have been defined that are based on the shortest time-respecting paths between pairs of nodes. However, a major issue of those generalizations is that the calculation of such paths is computationally expensive.Addressing this issue, we study the application of De Bruijn Graph Neural Networks (DBGNN), a time-aware graph neural network architecture, to predict temporal path-based centralities in time series data. We experimentally evaluate our approach in 13 temporal graphs from biological and social systems and show that it considerably improves the prediction of betweenness and closeness centrality compared to (i) a static Graph Convolutional Neural Network, (ii) an efficient sampling-based approximation technique for temporal betweenness, and (iii) two state-of-the-art time-aware graph learning techniques for dynamic graphs.