---
title: "4DBInfer:  A 4D Benchmarking Toolbox for Graph-Centric Predictive Modeling on RDBs"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/2fd67447702c8eff5683dda507a1b0a2-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['graph-neural-networks-and-representation-learning']
tags: ['relational-databases', 'graph-neural-networks', 'benchmarking', 'predictive-modeling', 'multi-table']
venue: "NeurIPS 2024"
tldr: "Introduces a 4D benchmarking toolbox for evaluating graph-centric predictive models on relational databases with interconnected tables."
---

# 4DBInfer:  A 4D Benchmarking Toolbox for Graph-Centric Predictive Modeling on RDBs

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/2fd67447702c8eff5683dda507a1b0a2-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/2fd67447702c8eff5683dda507a1b0a2-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces a 4D benchmarking toolbox for evaluating graph-centric predictive models on relational databases with interconnected tables.

## Abstract

Given a relational database (RDB), how can we predict  missing column values in some target table of interest? Although RDBs store vast amounts of rich, informative data spread across interconnected tables, the progress of predictive machine learning models as applied to such tasks arguably falls well behind advances in other domains such as computer vision or natural language processing.  This deficit stems, at least in part, from the lack of established/public RDB benchmarks as needed for training and evaluation purposes.  As a result, related model development thus far often defaults to tabular approaches trained on ubiquitous single-table benchmarks, or on the relational side, graph-based alternatives such as GNNs applied to a completely different set of graph datasets devoid of tabular characteristics.  To more precisely target RDBs lying at the nexus of these two complementary regimes, we explore a broad class of baseline models predicated on: (i) converting multi-table datasets into graphs using various strategies equipped with efficient subsampling, while preserving tabular characteristics; and (ii) trainable models with well-matched inductive biases that output predictions based on these input subgraphs.  Then, to address the dearth of suitable public benchmarks and reduce siloed comparisons, we assemble a diverse collection of (i) large-scale RDB datasets and (ii) coincident predictive tasks.  From a delivery standpoint, we  operationalize the above four dimensions (4D) of exploration within a unified, scalable open-source toolbox called 4DBInfer; please see https://github.com/awslabs/multi-table-benchmark .