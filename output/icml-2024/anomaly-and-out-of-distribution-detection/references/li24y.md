---
title: "Graph Structure Extrapolation for Out-of-Distribution Generalization"
source: "https://proceedings.mlr.press/v235/li24y.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24y/li24y.pdf"
categories: ['graph-neural-networks-and-topology', 'anomaly-and-out-of-distribution-detection']
tags: ['graph-OOD', 'generalization', 'data-augmentation', 'distribution-shift', 'graph-neural-networks']
venue: "ICML 2024"
tldr: "A graph structure extrapolation method improves out-of-distribution generalization for graph learning tasks."
---

# Graph Structure Extrapolation for Out-of-Distribution Generalization

**Source**: [https://proceedings.mlr.press/v235/li24y.html](https://proceedings.mlr.press/v235/li24y.html)

**TLDR**: A graph structure extrapolation method improves out-of-distribution generalization for graph learning tasks.

## Abstract

Out-of-distribution (OOD) generalization deals with the prevalent learning scenario where test distribution shifts from training distribution. With rising application demands and inherent complexity, graph OOD problems call for specialized solutions. While data-centric methods exhibit performance enhancements on many generic machine learning tasks, there is a notable absence of data augmentation methods tailored for graph OOD generalization. In this work, we propose to achieve graph OOD generalization with the novel design of non-Euclidean-space linear extrapolation. The proposed augmentation strategy extrapolates structure spaces to generate OOD graph data. Our design tailors OOD samples for specific shifts without corrupting underlying causal mechanisms. Theoretical analysis and empirical results evidence the effectiveness of our method in solving target shifts, showing substantial and constant improvements across various graph OOD tasks.