---
title: "Optimal Recurrent Network Topologies for Dynamical Systems Reconstruction"
source: "https://proceedings.mlr.press/v235/hemmer24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hemmer24a/hemmer24a.pdf"
categories: ['bayesian-filtering-and-dynamical-systems-learning', 'neuromorphic-computing-and-neural-dynamics-modeling']
tags: ['recurrent-networks', 'dynamical-systems', 'topology', 'reconstruction']
venue: "ICML 2024"
tldr: "Identifies optimal recurrent network topologies for parsimonious and accurate dynamical systems reconstruction from time series."
---

# Optimal Recurrent Network Topologies for Dynamical Systems Reconstruction

**Source**: [https://proceedings.mlr.press/v235/hemmer24a.html](https://proceedings.mlr.press/v235/hemmer24a.html)

**TLDR**: Identifies optimal recurrent network topologies for parsimonious and accurate dynamical systems reconstruction from time series.

## Abstract

In dynamical systems reconstruction (DSR) we seek to infer from time series measurements a generative model of the underlying dynamical process. This is a prime objective in any scientific discipline, where we are particularly interested in parsimonious models with a low parameter load. A common strategy here is parameter pruning, removing all parameters with small weights. However, here we find this strategy does not work for DSR, where even low magnitude parameters can contribute considerably to the system dynamics. On the other hand, it is well known that many natural systems which generate complex dynamics, like the brain or ecological networks, have a sparse topology with comparatively few links. Inspired by this, we show that geometric pruning, where in contrast to magnitude-based pruning weights with a low contribution to an attractor’s geometrical structure are removed, indeed manages to reduce parameter load substantially without significantly hampering DSR quality. We further find that the networks resulting from geometric pruning have a specific type of topology, and that this topology, and not the magnitude of weights, is what is most crucial to performance. We provide an algorithm that automatically generates such topologies which can be used as priors for generative modeling of dynamical systems by RNNs, and compare it to other well studied topologies like small-world or scale-free networks.