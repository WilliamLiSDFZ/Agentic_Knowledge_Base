---
title: "Position: Relational Deep Learning - Graph Representation Learning on Relational Databases"
source: "https://proceedings.mlr.press/v235/fey24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fey24a/fey24a.pdf"
categories: ['position-papers-on-ml-research-directions', 'graph-neural-networks-and-topology']
tags: ['relational-databases', 'graph-representation', 'position-paper']
venue: "ICML 2024"
tldr: "This position paper argues for relational deep learning that applies graph representation learning directly to relational database structures."
---

# Position: Relational Deep Learning - Graph Representation Learning on Relational Databases

**Source**: [https://proceedings.mlr.press/v235/fey24a.html](https://proceedings.mlr.press/v235/fey24a.html)

**TLDR**: This position paper argues for relational deep learning that applies graph representation learning directly to relational database structures.

## Abstract

Much of the world’s most valued data is stored in relational databases and data warehouses, where the data is organized into tables connected by primary-foreign key relations. However, building machine learning models using this data is both challenging and time consuming because no ML algorithm can directly learn from multiple connected tables. Current approaches can only learn from a single table, so data must first be manually joined and aggregated into this format, the laborious process known as feature engineering. Feature engineering is slow, error prone and leads to suboptimal models. Here we introduce Relational Deep Learning (RDL), a blueprint for end-to-end learning on relational databases. The key is to represent relational databases as a temporal, heterogeneous graphs, with a node for each row in each table, and edges specified by primary-foreign key links. Graph Neural Networks then learn representations that leverage all input data, without any manual feature engineering. We also introduce RelBench, and benchmark and testing suite, demonstrating strong initial results. Overall, we define a new research area that generalizes graph machine learning and broadens its applicability.