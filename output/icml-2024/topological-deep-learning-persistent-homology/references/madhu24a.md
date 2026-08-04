---
title: "Unsupervised Parameter-free Simplicial Representation Learning with Scattering Transforms"
source: "https://proceedings.mlr.press/v235/madhu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/madhu24a/madhu24a.pdf"
categories: ['graph-neural-networks-and-topology', 'topological-deep-learning-persistent-homology']
tags: ['simplicial-neural-networks', 'scattering-transforms', 'unsupervised-learning']
venue: "ICML 2024"
tldr: "A parameter-free simplicial scattering network for unsupervised higher-order graph representation learning without task-specific labels."
---

# Unsupervised Parameter-free Simplicial Representation Learning with Scattering Transforms

**Source**: [https://proceedings.mlr.press/v235/madhu24a.html](https://proceedings.mlr.press/v235/madhu24a.html)

**TLDR**: A parameter-free simplicial scattering network for unsupervised higher-order graph representation learning without task-specific labels.

## Abstract

Simplicial neural network models are becoming popular for processing and analyzing higher-order graph data, but they suffer from high training complexity and dependence on task-specific labels. To address these challenges, we propose simplicial scattering networks (SSNs), a parameter-free model inspired by scattering transforms designed to extract task-agnostic features from simplicial complex data without labels in a principled manner. Specifically, we propose a simplicial scattering transform based on random walk matrices for various adjacencies underlying a simplicial complex. We then use the simplicial scattering transform to construct a deep filter bank network that captures high-frequency information at multiple scales. The proposed simplicial scattering transform possesses properties such as permutation invariance, robustness to perturbations, and expressivity. We theoretically prove that including higher-order information improves the robustness of SSNs to perturbations. Empirical evaluations demonstrate that SSNs outperform existing simplicial or graph neural models in many tasks like node classification, simplicial closure, graph classification, trajectory prediction, and simplex prediction while being computationally efficient.