---
title: "Differentiable Weightless Neural Networks"
source: "https://proceedings.mlr.press/v235/bacellar24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bacellar24a/bacellar24a.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling', 'decision-tree-learning-algorithms-optimization']
tags: ['weightless-neural-networks', 'lookup-tables', 'differentiable-training', 'finite-difference', 'binary-networks']
venue: "ICML 2024"
tldr: "Introduces Differentiable Weightless Neural Networks based on lookup tables trained via a novel Extended Finite Difference approximation."
---

# Differentiable Weightless Neural Networks

**Source**: [https://proceedings.mlr.press/v235/bacellar24a.html](https://proceedings.mlr.press/v235/bacellar24a.html)

**TLDR**: Introduces Differentiable Weightless Neural Networks based on lookup tables trained via a novel Extended Finite Difference approximation.

## Abstract

We introduce the Differentiable Weightless Neural Network (DWN), a model based on interconnected lookup tables. Training of DWNs is enabled by a novel Extended Finite Difference technique for approximate differentiation of binary values. We propose Learnable Mapping, Learnable Reduction, and Spectral Regularization to further improve the accuracy and efficiency of these models. We evaluate DWNs in three edge computing contexts: (1) an FPGA-based hardware accelerator, where they demonstrate superior latency, throughput, energy efficiency, and model area compared to state-of-the-art solutions, (2) a low-power microcontroller, where they achieve preferable accuracy to XGBoost while subject to stringent memory constraints, and (3) ultra-low-cost chips, where they consistently outperform small models in both accuracy and projected hardware area. DWNs also compare favorably against leading approaches for tabular datasets, with higher average rank. Overall, our work positions DWNs as a pioneering solution for edge-compatible high-throughput neural networks.