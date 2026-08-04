---
title: "Contrastive Predict-and-Search for Mixed Integer Linear Programs"
source: "https://proceedings.mlr.press/v235/huang24f.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24f/huang24f.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'optimization-algorithms-convergence-theory']
tags: ['mixed-integer-linear-programming', 'contrastive-learning', 'predict-and-search']
venue: "ICML 2024"
tldr: "Introduces ConPaS, a contrastive learning framework for predicting high-quality solutions to MILPs to guide search."
---

# Contrastive Predict-and-Search for Mixed Integer Linear Programs

**Source**: [https://proceedings.mlr.press/v235/huang24f.html](https://proceedings.mlr.press/v235/huang24f.html)

**TLDR**: Introduces ConPaS, a contrastive learning framework for predicting high-quality solutions to MILPs to guide search.

## Abstract

Mixed integer linear programs (MILP) are flexible and powerful tools for modeling and solving many difficult real-world combinatorial optimization problems. In this paper, we propose a novel machine learning (ML)-based framework ConPaS that learns to predict solutions to MILPs with contrastive learning. For training, we collect high-quality solutions as positive samples. We also collect low-quality or infeasible solutions as negative samples using novel optimization-based or sampling approaches. We then learn to make discriminative predictions by contrasting the positive and negative samples. During testing, we predict and fix the assignments for a subset of integer variables and then solve the resulting reduced MILP to find high-quality solutions. Empirically, ConPaS achieves state-of-the-art results compared to other ML-based approaches in terms of the quality of and the speed at which solutions are found.