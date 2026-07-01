---
title: "WikiDBs: A Large-Scale Corpus Of Relational Databases From Wikidata"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/4847447cae911dde321ca19afe7d8707-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['graph-neural-networks-and-representation-learning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['relational-databases', 'tabular-data', 'representation-learning', 'Wikidata', 'benchmark']
venue: "NeurIPS 2024"
tldr: "Introduces WikiDBs, a large-scale corpus of relational databases derived from Wikidata to support multi-table representation learning research."
---

# WikiDBs: A Large-Scale Corpus Of Relational Databases From Wikidata

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/4847447cae911dde321ca19afe7d8707-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/4847447cae911dde321ca19afe7d8707-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces WikiDBs, a large-scale corpus of relational databases derived from Wikidata to support multi-table representation learning research.

## Abstract

Deep learning on tabular data, and particularly tabular representation learning, has recently gained growing interest. However, representation learning for relational databases with multiple tables is still an underexplored area, which may be attributed to the lack of openly available resources. To support the development of foundation models for tabular data and relational databases, we introduce WikiDBs, a novel open-source corpus of 100,000 relational databases. Each database consists of multiple tables connected by foreign keys. The corpus is based on Wikidata and aims to follow certain characteristics of real-world databases. In this paper, we describe the dataset and our method for creating it. By making our code publicly available, we enable others to create tailored versions of the dataset, for example, by creating databases in different languages. Finally, we conduct a set of initial experiments to showcase how WikiDBs can be used to train for data engineering tasks, such as missing value imputation and column type annotation.