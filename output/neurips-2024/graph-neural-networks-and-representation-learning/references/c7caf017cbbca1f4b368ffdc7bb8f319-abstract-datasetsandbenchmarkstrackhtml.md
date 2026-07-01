---
title: "PowerGraph: A power grid benchmark dataset for graph neural networks"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/c7caf017cbbca1f4b368ffdc7bb8f319-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['graph-neural-networks-and-representation-learning']
tags: ['power-grid', 'graph-neural-networks', 'benchmark', 'energy-systems']
venue: "NeurIPS 2024"
tldr: "PowerGraph introduces a benchmark dataset for evaluating graph neural networks on power grid analysis under diverse operating conditions."
---

# PowerGraph: A power grid benchmark dataset for graph neural networks

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/c7caf017cbbca1f4b368ffdc7bb8f319-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/c7caf017cbbca1f4b368ffdc7bb8f319-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: PowerGraph introduces a benchmark dataset for evaluating graph neural networks on power grid analysis under diverse operating conditions.

## Abstract

Power grids are critical infrastructures of paramount importance to modern society and, therefore, engineered to operate under diverse conditions and failures. The ongoing energy transition poses new challenges for the decision-makers and system operators. Therefore, we must develop grid analysis algorithms to ensure reliable operations. These key tools include power flow analysis and system security analysis, both needed for effective operational and strategic planning. The literature review shows a growing trend of machine learning (ML) models that perform these analyses effectively. In particular, Graph Neural Networks (GNNs) stand out in such applications because of the graph-based structure of power grids. However, there is a lack of publicly available graph datasets for training and benchmarking ML models in electrical power grid applications. First, we present PowerGraph, which comprises GNN-tailored datasets for i) power flows, ii) optimal power flows, and iii) cascading failure analyses of power grids. Second, we provide ground-truth explanations for the cascading failure analysis. Finally, we perform a complete benchmarking of GNN methods for node-level and graph-level tasks and explainability. Overall, PowerGraph is a multifaceted GNN dataset for diverse tasks that includes power flow and fault scenarios with real-world explanations, providing a valuable resource for developing improved GNN models for node-level, graph-level tasks and explainability methods in power system modeling. The dataset is available at https://figshare.com/articles/dataset/PowerGraph/22820534 and the code at https://github.com/PowerGraph-Datasets.