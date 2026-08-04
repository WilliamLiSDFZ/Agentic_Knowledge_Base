---
title: "ProtoGate: Prototype-based Neural Networks with Global-to-local Feature Selection for Tabular Biomedical Data"
source: "https://proceedings.mlr.press/v235/jiang24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jiang24c/jiang24c.pdf"
categories: ['data-selection-and-active-learning-methods', 'ai-explainability-uncertainty-human-decision-making']
tags: ['prototype-networks', 'feature-selection', 'tabular-biomedical-data', 'high-dimensional']
venue: "ICML 2024"
tldr: "ProtoGate combines prototype-based neural networks with global-to-local feature selection to handle high-dimensional low-sample-size tabular biomedical data."
---

# ProtoGate: Prototype-based Neural Networks with Global-to-local Feature Selection for Tabular Biomedical Data

**Source**: [https://proceedings.mlr.press/v235/jiang24c.html](https://proceedings.mlr.press/v235/jiang24c.html)

**TLDR**: ProtoGate combines prototype-based neural networks with global-to-local feature selection to handle high-dimensional low-sample-size tabular biomedical data.

## Abstract

Tabular biomedical data poses challenges in machine learning because it is often high-dimensional and typically low-sample-size (HDLSS). Previous research has attempted to address these challenges via local feature selection, but existing approaches often fail to achieve optimal performance due to their limitation in identifying globally important features and their susceptibility to the co-adaptation problem. In this paper, we propose ProtoGate, a prototype-based neural model for feature selection on HDLSS data. ProtoGate first selects instance-wise features via adaptively balancing global and local feature selection. Furthermore, ProtoGate employs a non-parametric prototype-based prediction mechanism to tackle the co-adaptation problem, ensuring the feature selection results and predictions are consistent with underlying data clusters. We conduct comprehensive experiments to evaluate the performance and interpretability of ProtoGate on synthetic and real-world datasets. The results show that ProtoGate generally outperforms state-of-the-art methods in prediction accuracy by a clear margin while providing high-fidelity feature selection and explainable predictions. Code is available at https://github.com/SilenceX12138/ProtoGate.