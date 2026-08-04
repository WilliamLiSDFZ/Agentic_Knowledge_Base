---
title: "Collective Certified Robustness against Graph Injection Attacks"
source: "https://proceedings.mlr.press/v235/lai24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lai24a/lai24a.pdf"
categories: ['adversarial-robustness-and-model-security', 'graph-neural-networks-and-topology']
tags: ['certified-robustness', 'graph-injection-attacks', 'GNN', 'collective-certificate']
venue: "ICML 2024"
tldr: "The first collective certificate for GNN robustness under graph injection attacks, jointly certifying sets of nodes rather than individual samples."
---

# Collective Certified Robustness against Graph Injection Attacks

**Source**: [https://proceedings.mlr.press/v235/lai24a.html](https://proceedings.mlr.press/v235/lai24a.html)

**TLDR**: The first collective certificate for GNN robustness under graph injection attacks, jointly certifying sets of nodes rather than individual samples.

## Abstract

We investigate certified robustness for GNNs under graph injection attacks. Existing research only provides sample-wise certificates by verifying each node independently, leading to very limited certifying performance. In this paper, we present the first collective certificate, which certifies a set of target nodes simultaneously. To achieve it, we formulate the problem as a binary integer quadratic constrained linear programming (BQCLP). We further develop a customized linearization technique that allows us to relax the BQCLP into linear programming (LP) that can be efficiently solved. Through comprehensive experiments, we demonstrate that our collective certification scheme significantly improves certification performance with minimal computational overhead. For instance, by solving the LP within 1 minute on the Citeseer dataset, we achieve a significant increase in the certified ratio from 0.0% to 81.2% when the injected node number is 5% of the graph size. Our paper marks a crucial step towards making provable defense more practical. Our source code is available at https://github.com/Yuni-Lai/CollectiveLPCert.