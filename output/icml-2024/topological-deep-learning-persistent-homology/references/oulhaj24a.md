---
title: "Differentiable Mapper for Topological Optimization of Data Representation"
source: "https://proceedings.mlr.press/v235/oulhaj24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/oulhaj24a/oulhaj24a.pdf"
categories: ['topological-deep-learning-persistent-homology']
tags: ['topological-data-analysis', 'mapper-graph', 'differentiable-topology', 'data-visualization']
venue: "ICML 2024"
tldr: "Proposes a differentiable Mapper algorithm for topological optimization of data representations and visualizations."
---

# Differentiable Mapper for Topological Optimization of Data Representation

**Source**: [https://proceedings.mlr.press/v235/oulhaj24a.html](https://proceedings.mlr.press/v235/oulhaj24a.html)

**TLDR**: Proposes a differentiable Mapper algorithm for topological optimization of data representations and visualizations.

## Abstract

Unsupervised data representation and visualization using tools from topology is an active and growing field of Topological Data Analysis (TDA) and data science. Its most prominent line of work is based on the so-called Mapper graph, which is a combinatorial graph whose topological structures (connected components, branches, loops) are in correspondence with those of the data itself. While highly generic and applicable, its use has been hampered so far by the manual tuning of its many parameters—among these, a crucial one is the so-called filter: it is a continuous function whose variations on the data set are the main ingredient for both building the Mapper representation and assessing the presence and sizes of its topological structures. However, while a few parameter tuning methods have already been investigated for the other Mapper parameters (i.e., resolution, gain, clustering), there is currently no method for tuning the filter itself. In this work, we build on a recently proposed optimization framework incorporating topology to provide the first filter optimization scheme for Mapper graphs. In order to achieve this, we propose a relaxed and more general version of the Mapper graph, whose convergence properties are investigated. Finally, we demonstrate the usefulness of our approach by optimizing Mapper graph representations on several datasets, and showcasing the superiority of the optimized representation over arbitrary ones.