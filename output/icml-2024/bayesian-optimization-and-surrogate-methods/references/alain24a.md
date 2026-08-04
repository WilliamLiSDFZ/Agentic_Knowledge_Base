---
title: "Gaussian Processes on Cellular Complexes"
source: "https://proceedings.mlr.press/v235/alain24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/alain24a/alain24a.pdf"
categories: ['graph-neural-networks-and-topology', 'bayesian-optimization-and-surrogate-methods']
tags: ['Gaussian-processes', 'cellular-complexes', 'topological-learning']
venue: "ICML 2024"
tldr: "This paper extends Gaussian processes to cellular complexes to incorporate topological inductive biases with uncertainty quantification."
---

# Gaussian Processes on Cellular Complexes

**Source**: [https://proceedings.mlr.press/v235/alain24a.html](https://proceedings.mlr.press/v235/alain24a.html)

**TLDR**: This paper extends Gaussian processes to cellular complexes to incorporate topological inductive biases with uncertainty quantification.

## Abstract

In recent years, there has been considerable interest in developing machine learning models on graphs to account for topological inductive biases. In particular, recent attention has been given to Gaussian processes on such structures since they can additionally account for uncertainty. However, graphs are limited to modelling relations between two vertices. In this paper, we go beyond this dyadic setting and consider polyadic relations that include interactions between vertices, edges and one of their generalisations, known as cells. Specifically, we propose Gaussian processes on cellular complexes, a generalisation of graphs that captures interactions between these higher-order cells. One of our key contributions is the derivation of two novel kernels, one that generalises the graph Matérn kernel and one that additionally mixes information of different cell types.