---
title: "Graph Neural Networks with a Distribution of Parametrized Graphs"
source: "https://proceedings.mlr.press/v235/lee24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24k/lee24k.pdf"
categories: ['graph-neural-networks-and-topology', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['graph-neural-networks', 'graph-uncertainty', 'stochastic-graphs', 'robustness']
venue: "ICML 2024"
tldr: "Trains graph neural networks over a distribution of parametrized graphs to handle uncertainty in observed graph structure."
---

# Graph Neural Networks with a Distribution of Parametrized Graphs

**Source**: [https://proceedings.mlr.press/v235/lee24k.html](https://proceedings.mlr.press/v235/lee24k.html)

**TLDR**: Trains graph neural networks over a distribution of parametrized graphs to handle uncertainty in observed graph structure.

## Abstract

Traditionally, graph neural networks have been trained using a single observed graph. However, the observed graph represents only one possible realization. In many applications, the graph may encounter uncertainties, such as having erroneous or missing edges, as well as edge weights that provide little informative value. To address these challenges and capture additional information previously absent in the observed graph, we introduce latent variables to parameterize and generate multiple graphs. The parameters follow an unknown distribution to be estimated. We propose a formulation in terms of maximum likelihood estimation of the network parameters. Therefore, it is possible to devise an algorithm based on Expectation-Maximization (EM). Specifically, we iteratively determine the distribution of the graphs using a Markov Chain Monte Carlo (MCMC) method, incorporating the principles of PAC-Bayesian theory. Numerical experiments demonstrate improvements in performance against baseline models on node classification for both heterogeneous and homogeneous graphs.