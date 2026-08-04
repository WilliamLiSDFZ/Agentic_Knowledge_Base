---
title: "Stable Differentiable Causal Discovery"
source: "https://proceedings.mlr.press/v235/nazaret24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nazaret24a/nazaret24a.pdf"
categories: ['causal-inference-and-discovery-methods']
tags: ['causal-discovery', 'differentiable-dag-learning', 'numerical-stability']
venue: "ICML 2024"
tldr: "Stable differentiable causal discovery improves existing DCD methods by addressing numerical instability in continuous DAG optimization."
---

# Stable Differentiable Causal Discovery

**Source**: [https://proceedings.mlr.press/v235/nazaret24a.html](https://proceedings.mlr.press/v235/nazaret24a.html)

**TLDR**: Stable differentiable causal discovery improves existing DCD methods by addressing numerical instability in continuous DAG optimization.

## Abstract

Inferring causal relationships as directed acyclic graphs (DAGs) is an important but challenging problem. Differentiable Causal Discovery (DCD) is a promising approach to this problem, framing the search as a continuous optimization. But existing DCD methods are numerically unstable, with poor performance beyond tens of variables. In this paper, we propose Stable Differentiable Causal Discovery (SDCD), a new method that improves previous DCD methods in two ways: (1) It employs an alternative constraint for acyclicity; this constraint is more stable, both theoretically and empirically, and fast to compute. (2) It uses a training procedure tailored for sparse causal graphs, which are common in real-world scenarios. We first derive SDCD and prove its stability and correctness. We then evaluate it with both observational and interventional data and in both small-scale and large-scale settings. We find that SDCD outperforms existing methods in convergence speed and accuracy, and can scale to thousands of variables.