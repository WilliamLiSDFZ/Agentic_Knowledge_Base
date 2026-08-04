---
title: "Making Old Things New: A Unified Algorithm for Differentially Private Clustering"
source: "https://proceedings.mlr.press/v235/dupre-la-tour24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dupre-la-tour24a/dupre-la-tour24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'graph-clustering-and-matching-algorithms']
tags: ['differential-privacy', 'clustering', 'unified-algorithm', 'local-shuffle-central']
venue: "ICML 2024"
tldr: "A unified differentially private clustering algorithm is presented that achieves near-optimal guarantees across centralized, local, and shuffle privacy models."
---

# Making Old Things New: A Unified Algorithm for Differentially Private Clustering

**Source**: [https://proceedings.mlr.press/v235/dupre-la-tour24a.html](https://proceedings.mlr.press/v235/dupre-la-tour24a.html)

**TLDR**: A unified differentially private clustering algorithm is presented that achieves near-optimal guarantees across centralized, local, and shuffle privacy models.

## Abstract

As a staple of data analysis and unsupervised learning, the problem of private clustering has been widely studied, under various privacy models. Centralized differential privacy is the first of them, and the problem has also been studied for the local and the shuffle variation. In each case, the goal is to design an algorithm that computes privately a clustering, with the smallest possible error. The study of each variation gave rise to new algorithm: the landscape of private clustering algorithm is therefore quite intricate. In this paper, we show that a 20 year-old algorithm can be slightly modified to work for any of those models. This provides a unified picture: while matching almost all previously known results, it allows us to improve some of them, and extend to a new privacy model, the continual observation setting, where the input is changing over time and the algorithm must output a new solution at each time step.