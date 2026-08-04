---
title: "Improved Stability and Generalization Guarantees of the Decentralized SGD Algorithm"
source: "https://proceedings.mlr.press/v235/le-bars24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/le-bars24a/le-bars24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'optimization-algorithms-convergence-theory']
tags: ['decentralized-SGD', 'generalization', 'algorithmic-stability', 'network-topology']
venue: "ICML 2024"
tldr: "New stability-based generalization bounds for decentralized SGD that reassess the claimed detrimental effects of decentralization and network connectivity."
---

# Improved Stability and Generalization Guarantees of the Decentralized SGD Algorithm

**Source**: [https://proceedings.mlr.press/v235/le-bars24a.html](https://proceedings.mlr.press/v235/le-bars24a.html)

**TLDR**: New stability-based generalization bounds for decentralized SGD that reassess the claimed detrimental effects of decentralization and network connectivity.

## Abstract

This paper presents a new generalization error analysis for Decentralized Stochastic Gradient Descent (D-SGD) based on algorithmic stability. The obtained results overhaul a series of recent works that suggested an increased instability due to decentralization and a detrimental impact of poorly-connected communication graphs on generalization. On the contrary, we show, for convex, strongly convex and non-convex functions, that D-SGD can always recover generalization bounds analogous to those of classical SGD, suggesting that the choice of graph does not matter. We then argue that this result is coming from a worst-case analysis, and we provide a refined optimization-dependent generalization bound for general convex functions. This new bound reveals that the choice of graph can in fact improve the worst-case bound in certain regimes, and that surprisingly, a poorly-connected graph can even be beneficial for generalization.