---
title: "Predicting and Interpreting Energy Barriers of Metallic Glasses with Graph Neural Networks"
source: "https://proceedings.mlr.press/v235/li24cm.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24cm/li24cm.pdf"
categories: ['graph-neural-networks-and-topology']
tags: ['graph-neural-networks', 'metallic-glasses', 'energy-barriers']
venue: "ICML 2024"
tldr: "Graph neural networks are used to predict and interpret energy barriers of metallic glasses, revealing structure-property relationships."
---

# Predicting and Interpreting Energy Barriers of Metallic Glasses with Graph Neural Networks

**Source**: [https://proceedings.mlr.press/v235/li24cm.html](https://proceedings.mlr.press/v235/li24cm.html)

**TLDR**: Graph neural networks are used to predict and interpret energy barriers of metallic glasses, revealing structure-property relationships.

## Abstract

Metallic Glasses (MGs) are widely used materials that are stronger than steel while being shapeable as plastic. While understanding the structure-property relationship of MGs remains a challenge in materials science, studying their energy barriers (EBs) as an intermediary step shows promise. In this work, we utilize Graph Neural Networks (GNNs) to model MGs and study EBs. We contribute a new dataset for EB prediction and a novel Symmetrized GNN (SymGNN) model that is E(3)-invariant in expectation. SymGNN handles invariance by aggregating over orthogonal transformations of the graph structure. When applied to EB prediction, SymGNN are more accurate than molecular dynamics (MD) local-sampling methods and other machine-learning models. Compared to precise MD simulations, SymGNN reduces the inference time on new MGs from roughly 41 days to less than one second. We apply explanation algorithms to reveal the relationship between structures and EBs. The structures that we identify through explanations match the medium-range order (MRO) hypothesis and possess unique topological properties. Our work enables effective prediction and interpretation of MG EBs, bolstering material science research.