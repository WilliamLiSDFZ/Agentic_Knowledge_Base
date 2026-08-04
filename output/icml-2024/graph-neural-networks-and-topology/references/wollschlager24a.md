---
title: "Expressivity and Generalization: Fragment-Biases for Molecular GNNs"
source: "https://proceedings.mlr.press/v235/wollschlager24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wollschlager24a/wollschlager24a.pdf"
categories: ['graph-neural-networks-and-topology', 'equivariant-neural-networks-and-symmetry-learning']
tags: ['molecular-GNNs', 'fragment-bias', 'expressivity', 'generalization']
venue: "ICML 2024"
tldr: "Analyzes how fragment-level inductive biases improve both expressivity and generalization of molecular graph neural networks beyond higher-order GNNs."
---

# Expressivity and Generalization: Fragment-Biases for Molecular GNNs

**Source**: [https://proceedings.mlr.press/v235/wollschlager24a.html](https://proceedings.mlr.press/v235/wollschlager24a.html)

**TLDR**: Analyzes how fragment-level inductive biases improve both expressivity and generalization of molecular graph neural networks beyond higher-order GNNs.

## Abstract

Although recent advances in higher-order Graph Neural Networks (GNNs) improve the theoretical expressiveness and molecular property predictive performance, they often fall short of the empirical performance of models that explicitly use fragment information as inductive bias. However, for these approaches, there exists no theoretic expressivity study. In this work, we propose the Fragment-WL test, an extension to the well-known Weisfeiler & Leman (WL) test, which enables the theoretic analysis of these fragment-biased GNNs. Building on the insights gained from the Fragment-WL test, we develop a new GNN architecture and a fragmentation with infinite vocabulary that significantly boosts expressiveness. We show the effectiveness of our model on synthetic and real-world data where we outperform all GNNs on Peptides and have $12$% lower error than all GNNs on ZINC and $34$% lower error than other fragment-biased models. Furthermore, we show that our model exhibits superior generalization capabilities compared to the latest transformer-based architectures, positioning it as a robust solution for a range of molecular modeling tasks.