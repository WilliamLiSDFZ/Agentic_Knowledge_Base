---
title: "Towards General Algorithm Discovery for Combinatorial Optimization: Learning Symbolic Branching Policy from Bipartite Graph"
source: "https://proceedings.mlr.press/v235/kuang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/kuang24a/kuang24a.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'decision-tree-learning-algorithms-optimization']
tags: ['combinatorial-optimization', 'symbolic-policy', 'bipartite-graph', 'branching']
venue: "ICML 2024"
tldr: "A method for learning interpretable symbolic branching policies from bipartite graphs to accelerate combinatorial optimization solvers."
---

# Towards General Algorithm Discovery for Combinatorial Optimization: Learning Symbolic Branching Policy from Bipartite Graph

**Source**: [https://proceedings.mlr.press/v235/kuang24a.html](https://proceedings.mlr.press/v235/kuang24a.html)

**TLDR**: A method for learning interpretable symbolic branching policies from bipartite graphs to accelerate combinatorial optimization solvers.

## Abstract

Machine learning (ML) approaches have been successfully applied to accelerating exact combinatorial optimization (CO) solvers. However, many of them fail to explain what patterns they have learned that accelerate the CO algorithms due to the black-box nature of ML models like neural networks, and thus they prevent researchers from further understanding the tasks they are interested in. To tackle this problem, we propose the first graph-based algorithm discovery framework—namely, graph symbolic discovery for exact combinatorial optimization solver (GS4CO)—that learns interpretable branching policies directly from the general bipartite graph representation of CO problems. Specifically, we design a unified representation for symbolic policies with graph inputs, and then we employ a Transformer with multiple tree-structural encodings to generate symbolic trees end-to-end, which effectively reduces the cumulative error from iteratively distilling graph neural networks. Experiments show that GS4CO learned interpretable and lightweight policies outperform all the baselines on CPU machines, including both the human-designed and the learning-based. GS4CO shows an encouraging step towards general algorithm discovery on modern CO solvers.