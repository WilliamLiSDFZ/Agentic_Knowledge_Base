---
title: "TEG-DB: A Comprehensive Dataset and Benchmark of Textual-Edge Graphs"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/7054d2c49863c1c41be1d53f4377b82a-Abstract-Datasets_and_Benchmarks_Track.html"
categories: ['graph-neural-networks-and-representation-learning', 'ai-benchmarking-and-evaluation-methodology']
tags: ['textual-edge-graphs', 'graph-benchmarks', 'text-attributed-graphs']
venue: "NeurIPS 2024"
tldr: "Introduces TEG-DB, a dataset and benchmark for text-attributed graphs that includes rich textual information on edges as well as nodes."
---

# TEG-DB: A Comprehensive Dataset and Benchmark of Textual-Edge Graphs

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/7054d2c49863c1c41be1d53f4377b82a-Abstract-Datasets_and_Benchmarks_Track.html](https://papers.nips.cc/paper_files/paper/2024/hash/7054d2c49863c1c41be1d53f4377b82a-Abstract-Datasets_and_Benchmarks_Track.html)

**TLDR**: Introduces TEG-DB, a dataset and benchmark for text-attributed graphs that includes rich textual information on edges as well as nodes.

## Abstract

Text-Attributed Graphs (TAGs) augment graph structures with natural language descriptions, facilitating detailed depictions of data and their interconnections across various real-world settings. However, existing TAG datasets predominantly feature textual information only at the nodes, with edges typically represented by mere binary or categorical attributes. This lack of rich textual edge annotations significantly limits the exploration of contextual relationships between entities, hindering deeper insights into graph-structured data. To address this gap, we introduce Textual-Edge Graphs Datasets and Benchmark (TEG-DB), a comprehensive and diverse collection of benchmark textual-edge datasets featuring rich textual descriptions on nodes and edges. The TEG-DB datasets are large-scale and encompass a wide range of domains, from citation networks to social networks. In addition, we conduct extensive benchmark experiments on TEG-DB to assess the extent to which current techniques, including pre-trained language models, graph neural networks, and their combinations, can utilize textual node and edge information. Our goal is to elicit advancements in   textual-edge graph research, specifically in developing methodologies that exploit rich textual node and edge descriptions to enhance graph analysis and provide deeper insights into complex real-world networks. The entire TEG-DB project is publicly accessible as an open-source repository on Github, accessible at https://github.com/Zhuofeng-Li/TEG-Benchmark.