---
title: "Enforcing Constraints in RNA Secondary Structure Predictions: A Post-Processing Framework Based on the Assignment Problem"
source: "https://proceedings.mlr.press/v235/suh24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/suh24a/suh24a.pdf"
categories: ['neural-symbolic-combinatorial-optimization-learning', 'llm-geometry-and-interpretability-research']
tags: ['RNA-secondary-structure', 'post-processing', 'assignment-problem', 'constraints', 'bioinformatics']
venue: "ICML 2024"
tldr: "A post-processing framework based on the assignment problem is proposed to enforce structural constraints in RNA secondary structure predictions."
---

# Enforcing Constraints in RNA Secondary Structure Predictions: A Post-Processing Framework Based on the Assignment Problem

**Source**: [https://proceedings.mlr.press/v235/suh24a.html](https://proceedings.mlr.press/v235/suh24a.html)

**TLDR**: A post-processing framework based on the assignment problem is proposed to enforce structural constraints in RNA secondary structure predictions.

## Abstract

RNA properties, such as function and stability, are intricately tied to their two-dimensional conformations. This has spurred the development of computational models for predicting the RNA secondary structures, leveraging dynamic programming or machine learning (ML) techniques. These structures are governed by specific rules; for example, only Watson-Crick and Wobble pairs are allowed, and sequences must not form sharp bends. Recent efforts introduced a systematic approach to post-process the predictions made by ML algorithms, aiming to modify them to respect the constraints. However, we still observe instances violating the requirements, significantly reducing biological relevance. To address this challenge, we present a novel post-processing framework for ML-based predictions on RNA secondary structures, inspired by the assignment problem in integer linear programming. Our algorithm offers a theoretical guarantee, ensuring that the resulting predictions adhere to the fundamental constraints of RNAs. Empirical evidence supports the efficacy of our approach, demonstrating improved predictive performance with no constraint violation, while requiring less running time.