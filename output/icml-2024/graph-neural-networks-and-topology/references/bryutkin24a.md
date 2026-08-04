---
title: "HAMLET: Graph Transformer Neural Operator for Partial Differential Equations"
source: "https://proceedings.mlr.press/v235/bryutkin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bryutkin24a/bryutkin24a.pdf"
categories: ['neural-operators-for-pde-solving', 'graph-neural-networks-and-topology']
tags: ['graph-transformers', 'neural-operators', 'PDEs', 'modular-encoders']
venue: "ICML 2024"
tldr: "HAMLET is a graph transformer neural operator framework that incorporates differential equation structure for improved PDE solving."
---

# HAMLET: Graph Transformer Neural Operator for Partial Differential Equations

**Source**: [https://proceedings.mlr.press/v235/bryutkin24a.html](https://proceedings.mlr.press/v235/bryutkin24a.html)

**TLDR**: HAMLET is a graph transformer neural operator framework that incorporates differential equation structure for improved PDE solving.

## Abstract

We present a novel graph transformer framework, HAMLET, designed to address the challenges in solving partial differential equations (PDEs) using neural networks. The framework uses graph transformers with modular input encoders to directly incorporate differential equation information into the solution process. This modularity enhances parameter correspondence control, making HAMLET adaptable to PDEs of arbitrary geometries and varied input formats. Notably, HAMLET scales effectively with increasing data complexity and noise, showcasing its robustness. HAMLET is not just tailored to a single type of physical simulation, but can be applied across various domains. Moreover, it boosts model resilience and performance, especially in scenarios with limited data. We demonstrate, through extensive experiments, that our framework is capable of outperforming current techniques for PDEs.