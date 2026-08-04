---
title: "GNNs Also Deserve Editing, and They Need It More Than Once"
source: "https://proceedings.mlr.press/v235/zhong24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhong24d/zhong24d.pdf"
categories: ['graph-neural-networks-and-topology', 'continual-learning-memory-plasticity']
tags: ['model-editing', 'graph-neural-networks', 'continual-editing']
venue: "ICML 2024"
tldr: "Proposes a framework for sequentially editing GNNs to efficiently correct multiple errors without retraining from scratch."
---

# GNNs Also Deserve Editing, and They Need It More Than Once

**Source**: [https://proceedings.mlr.press/v235/zhong24d.html](https://proceedings.mlr.press/v235/zhong24d.html)

**TLDR**: Proposes a framework for sequentially editing GNNs to efficiently correct multiple errors without retraining from scratch.

## Abstract

Suppose a self-driving car is crashing into pedestrians, or a chatbot is instructing its users to conduct criminal wrongdoing; the stakeholders of such products will undoubtedly want to patch these catastrophic errors as soon as possible. To address such concerns, Model Editing: the study of efficiently patching model behaviors without significantly altering their general performance, has seen considerable activity, with hundreds of editing techniques developed in various domains such as CV and NLP. However, the graph learning community has objectively fallen behind with only a few Graph Neural Network-compatible — and just one GNN-specific — model editing methods available, where all of which are limited in their practical scope. We argue that the impracticality of these methods lies in their lack of Sequential Editing Robustness: the ability to edit multiple errors sequentially, and therefore fall short in effectiveness, as this approach mirrors how errors are discovered and addressed in the real world. In this paper, we delve into the specific reasons behind the difficulty of editing GNNs in succession and observe the root cause to be model overfitting. We subsequently propose a simple yet effective solution — SEED-GNN — by leveraging overfit-prevention techniques in a GNN-specific context to derive the first and only GNN model editing method that scales practically. Additionally, we formally frame the task paradigm of GNN editing and hope to inspire future research in this crucial but currently overlooked field. Please refer to our GitHub repository for code and checkpoints.