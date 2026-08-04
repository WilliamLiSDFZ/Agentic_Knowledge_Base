---
title: "An Empirical Study of Realized GNN Expressiveness"
source: "https://proceedings.mlr.press/v235/wang24cl.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24cl/wang24cl.pdf"
categories: ['graph-neural-networks-and-topology']
tags: ['gnn-expressiveness', 'weisfeiler-leman', 'empirical-evaluation']
venue: "ICML 2024"
tldr: "This paper empirically evaluates the realized expressiveness of GNNs using a unified measure based on the Weisfeiler-Leman hierarchy."
---

# An Empirical Study of Realized GNN Expressiveness

**Source**: [https://proceedings.mlr.press/v235/wang24cl.html](https://proceedings.mlr.press/v235/wang24cl.html)

**TLDR**: This paper empirically evaluates the realized expressiveness of GNNs using a unified measure based on the Weisfeiler-Leman hierarchy.

## Abstract

Research on the theoretical expressiveness of Graph Neural Networks (GNNs) has developed rapidly, and many methods have been proposed to enhance the expressiveness. However, most methods do not have a uniform expressiveness measure except for a few that strictly follow the $k$-dimensional Weisfeiler-Lehman ($k$-WL) test hierarchy, leading to difficulties in quantitatively comparing their expressiveness. Previous research has attempted to use datasets for measurement, but facing problems with difficulty (any model surpassing 1-WL has nearly 100% accuracy), granularity (models tend to be either 100% correct or near random guess), and scale (only several essentially different graphs involved). To address these limitations, we study the realized expressive power that a practical model instance can achieve using a novel expressiveness dataset, BREC, which poses greater difficulty (with up to 4-WL-indistinguishable graphs), finer granularity (enabling comparison of models between 1-WL and 3-WL), a larger scale (consisting of 800 1-WL-indistinguishable graphs that are non-isomorphic to each other). We synthetically test 23 models with higher-than-1-WL expressiveness on BREC. Our experiment gives the first thorough measurement of the realized expressiveness of those state-of-the-art beyond-1-WL GNN models and reveals the gap between theoretical and realized expressiveness. Dataset and evaluation codes are released at: https://github.com/GraphPKU/BREC.