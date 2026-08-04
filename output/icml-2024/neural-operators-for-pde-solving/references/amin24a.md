---
title: "Scalable and Flexible Causal Discovery with an Efficient Test for Adjacency"
source: "https://proceedings.mlr.press/v235/amin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/amin24a/amin24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'neural-operators-for-pde-solving']
tags: ['causal-discovery', 'adjacency-testing', 'scalable-algorithms']
venue: "ICML 2024"
tldr: "This paper proposes a scalable causal discovery method using an efficient adjacency test to learn causal graphs from large-scale data."
---

# Scalable and Flexible Causal Discovery with an Efficient Test for Adjacency

**Source**: [https://proceedings.mlr.press/v235/amin24a.html](https://proceedings.mlr.press/v235/amin24a.html)

**TLDR**: This paper proposes a scalable causal discovery method using an efficient adjacency test to learn causal graphs from large-scale data.

## Abstract

To make accurate predictions, understand mechanisms, and design interventions in systems of many variables, we wish to learn causal graphs from large scale data. Unfortunately the space of all possible causal graphs is enormous so scalably and accurately searching for the best fit to the data is a challenge. In principle we could substantially decrease the search space, or learn the graph entirely, by testing the conditional independence of variables. However, deciding if two variables are adjacent in a causal graph may require an exponential number of tests. Here we build a scalable and flexible method to evaluate if two variables are adjacent in a causal graph, the Differentiable Adjacency Test (DAT). DAT replaces an exponential number of tests with a provably equivalent relaxed problem. It then solves this problem by training two neural networks. We build a graph learning method based on DAT, DAT-Graph, that can also learn from data with interventions. DAT-Graph can learn graphs of 1000 variables with state of the art accuracy. Using the graph learned by DAT-Graph, we also build models that make much more accurate predictions of the effects of interventions on large scale RNA sequencing data.