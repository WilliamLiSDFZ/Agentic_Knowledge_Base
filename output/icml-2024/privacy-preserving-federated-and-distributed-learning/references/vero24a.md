---
title: "CuTS: Customizable Tabular Synthetic Data Generation"
source: "https://proceedings.mlr.press/v235/vero24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/vero24a/vero24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'probabilistic-generating-circuits-research']
tags: ['synthetic-data', 'tabular-data', 'privacy', 'customizable-generation', 'data-sharing']
venue: "ICML 2024"
tldr: "Presents CuTS, a framework for generating customizable synthetic tabular data that satisfies user-defined constraints while preserving privacy."
---

# CuTS: Customizable Tabular Synthetic Data Generation

**Source**: [https://proceedings.mlr.press/v235/vero24a.html](https://proceedings.mlr.press/v235/vero24a.html)

**TLDR**: Presents CuTS, a framework for generating customizable synthetic tabular data that satisfies user-defined constraints while preserving privacy.

## Abstract

Privacy, data quality, and data sharing concerns pose a key limitation for tabular data applications. While generating synthetic data resembling the original distribution addresses some of these issues, most applications would benefit from additional customization on the generated data. However, existing synthetic data approaches are limited to particular constraints, e.g., differential privacy (DP) or fairness. In this work, we introduce CuTS, the first customizable synthetic tabular data generation framework. Customization in CuTS is achieved via declarative statistical and logical expressions, supporting a wide range of requirements (e.g., DP or fairness, among others). To ensure high synthetic data quality in the presence of custom specifications, CuTS is pre-trained on the original dataset and fine-tuned on a differentiable loss automatically derived from the provided specifications using novel relaxations. We evaluate CuTS over four datasets and on numerous custom specifications, outperforming state-of-the-art specialized approaches on several tasks while being more general. In particular, at the same fairness level, we achieve 2.3% higher downstream accuracy than the state-of-the-art in fair synthetic data generation on the Adult dataset.