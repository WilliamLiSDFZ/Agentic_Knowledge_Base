---
title: "Graph Neural Network Explanations are Fragile"
source: "https://proceedings.mlr.press/v235/li24bd.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bd/li24bd.pdf"
categories: ['adversarial-robustness-and-model-security', 'graph-neural-networks-and-topology']
tags: ['GNN-explainability', 'adversarial-attack', 'fragility']
venue: "ICML 2024"
tldr: "Demonstrates that GNN explanations are fragile and can be manipulated by adversaries with small perturbations."
---

# Graph Neural Network Explanations are Fragile

**Source**: [https://proceedings.mlr.press/v235/li24bd.html](https://proceedings.mlr.press/v235/li24bd.html)

**TLDR**: Demonstrates that GNN explanations are fragile and can be manipulated by adversaries with small perturbations.

## Abstract

Explainable Graph Neural Network (GNN) has emerged recently to foster the trust of using GNNs. Existing GNN explainers are developed from various perspectives to enhance the explanation performance. We take the first step to study GNN explainers under adversarial attack—We found that an adversary slightly perturbing graph structure can ensure GNN model makes correct predictions, but the GNN explainer yields a drastically different explanation on the perturbed graph. Specifically, we first formulate the attack problem under a practical threat model (i.e., the adversary has limited knowledge about the GNN explainer and a restricted perturbation budget). We then design two methods (i.e., one is loss-based and the other is deduction-based) to realize the attack. We evaluate our attacks on various GNN explainers and the results show these explainers are fragile.