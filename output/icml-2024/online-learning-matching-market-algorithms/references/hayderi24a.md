---
title: "MAGNOLIA: Matching Algorithms via GNNs for Online Value-to-go Approximation"
source: "https://proceedings.mlr.press/v235/hayderi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hayderi24a/hayderi24a.pdf"
categories: ['online-learning-matching-market-algorithms', 'graph-neural-networks-and-topology']
tags: ['bipartite-matching', 'gnn', 'online-algorithms']
venue: "ICML 2024"
tldr: "MAGNOLIA uses GNNs to approximate the optimal online algorithm for Bayesian bipartite matching in digital marketplace applications."
---

# MAGNOLIA: Matching Algorithms via GNNs for Online Value-to-go Approximation

**Source**: [https://proceedings.mlr.press/v235/hayderi24a.html](https://proceedings.mlr.press/v235/hayderi24a.html)

**TLDR**: MAGNOLIA uses GNNs to approximate the optimal online algorithm for Bayesian bipartite matching in digital marketplace applications.

## Abstract

Online Bayesian bipartite matching is a central problem in digital marketplaces and exchanges, including advertising, crowdsourcing, ridesharing, and kidney exchange. We introduce a graph neural network (GNN) approach that emulates the problem’s combinatorially-complex optimal online algorithm, which selects actions (e.g., which nodes to match) by computing each action’s value-to-go (VTG)—the expected weight of the final matching if the algorithm takes that action, then acts optimally in the future. We train a GNN to estimate VTG and show empirically that this GNN returns high-weight matchings across a variety of tasks. Moreover, we identify a common family of graph distributions in spatial crowdsourcing applications, such as rideshare, under which VTG can be efficiently approximated by aggregating information within local neighborhoods in the graphs. This structure matches the local behavior of GNNs, providing theoretical justification for our approach.