---
title: "Graph Neural Stochastic Diffusion for Estimating Uncertainty in Node Classification"
source: "https://proceedings.mlr.press/v235/lin24x.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24x/lin24x.pdf"
categories: ['graph-neural-networks-and-topology', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['graph-neural-networks', 'uncertainty-estimation', 'node-classification']
venue: "ICML 2024"
tldr: "A graph neural stochastic diffusion method for principled uncertainty estimation in GNN-based node classification."
---

# Graph Neural Stochastic Diffusion for Estimating Uncertainty in Node Classification

**Source**: [https://proceedings.mlr.press/v235/lin24x.html](https://proceedings.mlr.press/v235/lin24x.html)

**TLDR**: A graph neural stochastic diffusion method for principled uncertainty estimation in GNN-based node classification.

## Abstract

Graph neural networks (GNNs) have advanced the state of the art in various domains. Despite their remarkable success, the uncertainty estimation of GNN predictions remains under-explored, which limits their practical applications especially in risk-sensitive areas. Current works suffer from either intractable posteriors or inflexible prior specifications, leading to sub-optimal empirical results. In this paper, we present graph neural stochastic diffusion (GNSD), a novel framework for estimating predictive uncertainty on graphs by establishing theoretical connections between GNNs and stochastic partial differential equation. GNSD represents a GNN-based parameterization of the proposed graph stochastic diffusion equation which includes a $Q$-Wiener process to model the stochastic evolution of node representations. GNSD introduces a drift network to guarantee accurate prediction and a stochastic forcing network to model the propagation of epistemic uncertainty among nodes. Extensive experiments are conducted on multiple detection tasks, demonstrating that GNSD yields the superior performance over existing strong approaches.