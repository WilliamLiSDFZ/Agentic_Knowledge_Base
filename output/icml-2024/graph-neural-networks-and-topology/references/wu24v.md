---
title: "Learning Divergence Fields for Shift-Robust Graph Representations"
source: "https://proceedings.mlr.press/v235/wu24v.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wu24v/wu24v.pdf"
categories: ['graph-neural-networks-and-topology', 'learning-with-imperfect-data-and-bias']
tags: ['graph-neural-networks', 'distribution-shift', 'divergence-fields', 'graph-representations', 'robustness']
venue: "ICML 2024"
tldr: "Proposes learning divergence fields to achieve shift-robust graph representations by accounting for instance-level interdependence in real-world data generation."
---

# Learning Divergence Fields for Shift-Robust Graph Representations

**Source**: [https://proceedings.mlr.press/v235/wu24v.html](https://proceedings.mlr.press/v235/wu24v.html)

**TLDR**: Proposes learning divergence fields to achieve shift-robust graph representations by accounting for instance-level interdependence in real-world data generation.

## Abstract

Real-world data generation often involves certain geometries (e.g., graphs) that induce instance-level interdependence. This characteristic makes the generalization of learning models more difficult due to the intricate interdependent patterns that impact data-generative distributions and can vary from training to testing. In this work, we propose a geometric diffusion model with learnable divergence fields for the challenging generalization problem with interdependent data. We generalize the diffusion equation with stochastic diffusivity at each time step, which aims to capture the multi-faceted information flows among interdependent data. Furthermore, we derive a new learning objective through causal inference, which can guide the model to learn generalizable patterns of interdependence that are insensitive across domains. Regarding practical implementation, we introduce three model instantiations that can be considered as the generalized versions of GCN, GAT, and Transformers, respectively, which possess advanced robustness against distribution shifts. We demonstrate their promising efficacy for out-of-distribution generalization on diverse real-world datasets. Source codes are available at https://github.com/fannie1208/GLIND.