---
title: "Discovering Environments with XRM"
source: "https://proceedings.mlr.press/v235/pezeshki24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/pezeshki24a/pezeshki24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'causal-inference-and-discovery-methods']
tags: ['environment-discovery', 'OOD-generalization', 'automatic-annotation', 'spurious-correlations', 'distribution-shift']
venue: "ICML 2024"
tldr: "Proposes XRM, an algorithm for automatically discovering environment annotations to enable robust out-of-distribution generalization."
---

# Discovering Environments with XRM

**Source**: [https://proceedings.mlr.press/v235/pezeshki24a.html](https://proceedings.mlr.press/v235/pezeshki24a.html)

**TLDR**: Proposes XRM, an algorithm for automatically discovering environment annotations to enable robust out-of-distribution generalization.

## Abstract

Environment annotations are essential for the success of many out-of-distribution (OOD) generalization methods. Unfortunately, these are costly to obtain and often limited by human annotators’ biases. To achieve robust generalization, it is essential to develop algorithms for automatic environment discovery within datasets. Current proposals, which divide examples based on their training error, suffer from one fundamental problem. These methods introduce hyper-parameters and early-stopping criteria, which require a validation set with human-annotated environments, the very information subject to discovery. In this paper, we propose Cross-Risk Minimization (XRM) to address this issue. XRM trains twin networks, each learning from one random half of the training data, while imitating confident held-out mistakes made by its sibling. XRM provides a recipe for hyper-parameter tuning, does not require early-stopping, and can discover environments for all training and validation data. Algorithms built on top of XRM environments achieve oracle worst-group-accuracy, addressing a long-standing challenge in OOD generalization.