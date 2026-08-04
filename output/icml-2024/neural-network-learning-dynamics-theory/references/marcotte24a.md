---
title: "Keep the Momentum: Conservation Laws beyond Euclidean Gradient Flows"
source: "https://proceedings.mlr.press/v235/marcotte24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/marcotte24a/marcotte24a.pdf"
categories: ['neural-network-learning-dynamics-theory']
tags: ['conservation-laws', 'non-Euclidean-geometry', 'momentum-dynamics']
venue: "ICML 2024"
tldr: "Characterizes conservation laws for non-Euclidean geometries and momentum-based optimization dynamics beyond standard gradient flows."
---

# Keep the Momentum: Conservation Laws beyond Euclidean Gradient Flows

**Source**: [https://proceedings.mlr.press/v235/marcotte24a.html](https://proceedings.mlr.press/v235/marcotte24a.html)

**TLDR**: Characterizes conservation laws for non-Euclidean geometries and momentum-based optimization dynamics beyond standard gradient flows.

## Abstract

Conservation laws are well-established in the context of Euclidean gradient flow dynamics, notably for linear or ReLU neural network training. Yet, their existence and principles for non-Euclidean geometries and momentum-based dynamics remain largely unknown. In this paper, we characterize "all" conservation laws in this general setting. In stark contrast to the case of gradient flows, we prove that the conservation laws for momentum-based dynamics exhibit temporal dependence. Additionally, we often observe a "conservation loss" when transitioning from gradient flow to momentum dynamics. Specifically, for linear networks, our framework allows us to identify all momentum conservation laws, which are less numerous than in the gradient flow case except in sufficiently over-parameterized regimes. With ReLU networks, no conservation law remains. This phenomenon also manifests in non-Euclidean metrics, used e.g. for Nonnegative Matrix Factorization (NMF): all conservation laws can be determined in the gradient flow context, yet none persists in the momentum case.