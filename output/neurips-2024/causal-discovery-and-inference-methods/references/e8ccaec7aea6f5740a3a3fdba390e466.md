---
title: "Graph Structure Inference with BAM: Neural Dependency Processing via Bilinear Attention"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/e8ccaec7aea6f5740a3a3fdba390e466-Abstract-Conference.html"
categories: ['graph-neural-networks-and-representation-learning', 'causal-discovery-and-inference-methods']
tags: ['graph-structure-inference', 'bilinear-attention', 'dependency-detection']
venue: "NeurIPS 2024"
tldr: "A neural network model using bilinear attention to infer graph dependency structures from observational data."
---

# Graph Structure Inference with BAM: Neural Dependency Processing via Bilinear Attention

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/e8ccaec7aea6f5740a3a3fdba390e466-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/e8ccaec7aea6f5740a3a3fdba390e466-Abstract-Conference.html)

**TLDR**: A neural network model using bilinear attention to infer graph dependency structures from observational data.

## Abstract

Detecting dependencies among variables is a fundamental task across scientific disciplines. We propose a novel neural network model for graph structure inference, which aims to learn a mapping from observational data to the corresponding underlying dependence structures. The model is trained with variably shaped and coupled simulated input data and requires only a single forward pass through the trained network for inference. Central to our approach is a novel bilinear attention mechanism (BAM) operating on covariance matrices of transformed data while respecting the geometry of the manifold of symmetric positive definite (SPD) matrices. Inspired by graphical lasso methods, our model optimizes over continuous graph representations in the SPD space, where inverse covariance matrices encode conditional independence relations. Empirical evaluations demonstrate the robustness of our method in detecting diverse dependencies, excelling in undirected graph estimation and showing competitive performance in completed partially directed acyclic graph estimation via a novel two-step approach. The trained model effectively detects causal relationships and generalizes well across different functional forms of nonlinear dependencies.