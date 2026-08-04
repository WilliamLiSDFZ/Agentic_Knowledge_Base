---
title: "Locality-Sensitive Hashing-Based Efficient Point Transformer with Applications in High-Energy Physics"
source: "https://proceedings.mlr.press/v235/miao24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/miao24b/miao24b.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'graph-neural-networks-and-topology']
tags: ['locality-sensitive-hashing', 'point-cloud', 'high-energy-physics']
venue: "ICML 2024"
tldr: "Proposes an LSH-based efficient transformer for large-scale point cloud processing with applications in high-energy physics."
---

# Locality-Sensitive Hashing-Based Efficient Point Transformer with Applications in High-Energy Physics

**Source**: [https://proceedings.mlr.press/v235/miao24b.html](https://proceedings.mlr.press/v235/miao24b.html)

**TLDR**: Proposes an LSH-based efficient transformer for large-scale point cloud processing with applications in high-energy physics.

## Abstract

This study introduces a novel transformer model optimized for large-scale point cloud processing in scientific domains such as high-energy physics (HEP) and astrophysics. Addressing the limitations of graph neural networks and standard transformers, our model integrates local inductive bias and achieves near-linear complexity with hardware-friendly regular operations. One contribution of this work is the quantitative analysis of the error-complexity tradeoff of various sparsification techniques for building efficient transformers. Our findings highlight the superiority of using locality-sensitive hashing (LSH), especially OR & AND-construction LSH, in kernel approximation for large-scale point cloud data with local inductive bias. Based on this finding, we propose LSH-based Efficient Point Transformer (HEPT), which combines E$^2$LSH with OR & AND constructions and is built upon regular computations. HEPT demonstrates remarkable performance on two critical yet time-consuming HEP tasks, significantly outperforming existing GNNs and transformers in accuracy and computational speed, marking a significant advancement in geometric deep learning and large-scale scientific data processing. Our code is available at https://github.com/Graph-COM/HEPT.