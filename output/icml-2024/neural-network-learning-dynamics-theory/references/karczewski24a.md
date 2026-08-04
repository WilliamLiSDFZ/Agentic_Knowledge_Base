---
title: "On the Generalization of Equivariant Graph Neural Networks"
source: "https://proceedings.mlr.press/v235/karczewski24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/karczewski24a/karczewski24a.pdf"
categories: ['graph-neural-networks-and-topology', 'neural-network-learning-dynamics-theory']
tags: ['equivariant-GNNs', 'generalization-theory', 'geometric-graphs']
venue: "ICML 2024"
tldr: "Analyzes the generalization properties of E(n)-equivariant graph neural networks beyond expressivity on geometric graphs like 3D molecules."
---

# On the Generalization of Equivariant Graph Neural Networks

**Source**: [https://proceedings.mlr.press/v235/karczewski24a.html](https://proceedings.mlr.press/v235/karczewski24a.html)

**TLDR**: Analyzes the generalization properties of E(n)-equivariant graph neural networks beyond expressivity on geometric graphs like 3D molecules.

## Abstract

$E(n)$-Equivariant Graph Neural Networks (EGNNs) are among the most widely used and successful models for representation learning on geometric graphs (e.g., 3D molecules). However, while the expressivity of EGNNs has been explored in terms of geometric variants of the Weisfeiler-Leman isomorphism test, characterizing their generalization capability remains open. In this work, we establish the first generalization bound for EGNNs. Our bound depicts a dependence on the weighted sum of logarithms of the spectral norms of the weight matrices (EGNN parameters). In addition, our main result reveals interesting novel insights: $i$) the spectral norms of the initial layers may impact generalization more than the final ones; $ii$) $\varepsilon$-normalization is beneficial to generalization — confirming prior empirical evidence. We leverage these insights to introduce a spectral norm regularizer tailored to EGNNs. Experiments on real-world datasets substantiate our analysis, demonstrating a high correlation between theoretical and empirical generalization gaps and the effectiveness of the proposed regularization scheme.