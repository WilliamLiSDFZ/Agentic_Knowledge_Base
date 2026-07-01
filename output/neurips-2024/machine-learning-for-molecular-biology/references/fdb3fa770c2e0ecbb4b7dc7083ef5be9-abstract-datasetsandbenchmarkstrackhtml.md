---
title: "MOTIVE: A Drug-Target Interaction Graph For Inductive Link Prediction"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/fdb3fa770c2e0ecbb4b7dc7083ef5be9-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['machine-learning-for-molecular-biology', 'graph-neural-networks-and-representation-learning']
tags: ['drug-target-interaction', 'graph', 'inductive-link-prediction', 'cell-painting', 'molecular-biology']
venue: "NeurIPS 2024"
tldr: "MOTIVE is a drug-target interaction graph dataset designed for inductive link prediction leveraging both structure-based and cell-based assay features."
---

# MOTIVE: A Drug-Target Interaction Graph For Inductive Link Prediction

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/fdb3fa770c2e0ecbb4b7dc7083ef5be9-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/fdb3fa770c2e0ecbb4b7dc7083ef5be9-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: MOTIVE is a drug-target interaction graph dataset designed for inductive link prediction leveraging both structure-based and cell-based assay features.

## Abstract

Drug-target interaction (DTI) prediction is crucial for identifying new therapeutics and detecting mechanisms of action. While structure-based methods accurately model physical interactions between a drug and its protein target, cell-based assays such as Cell Painting can better capture complex DTI interactions. This paper introduces MOTIVE, a Morphological cOmpound Target Interaction Graph dataset comprising Cell Painting features for 11,000 genes and 3,600 compounds, along with their relationships extracted from seven publicly available databases. We provide random, cold-source (new drugs), and cold-target (new genes) data splits to enable rigorous evaluation under realistic use cases. Our benchmark results show that graph neural networks that use Cell Painting features consistently outperform those that learn from graph structure alone, feature-based models, and topological heuristics. MOTIVE accelerates both graph ML research and drug discovery by promoting the development of more reliable DTI prediction models. MOTIVE resources are available at https://github.com/carpenter-singh-lab/motive.