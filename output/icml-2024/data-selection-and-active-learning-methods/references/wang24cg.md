---
title: "Rethinking Data Shapley for Data Selection Tasks: Misleads and Merits"
source: "https://proceedings.mlr.press/v235/wang24cg.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24cg/wang24cg.pdf"
categories: ['data-selection-and-active-learning-methods']
tags: ['data-valuation', 'data-shapley', 'data-selection']
venue: "ICML 2024"
tldr: "This paper critiques Data Shapley for data selection tasks, identifying misleading behaviors and clarifying when it is and isn't effective."
---

# Rethinking Data Shapley for Data Selection Tasks: Misleads and Merits

**Source**: [https://proceedings.mlr.press/v235/wang24cg.html](https://proceedings.mlr.press/v235/wang24cg.html)

**TLDR**: This paper critiques Data Shapley for data selection tasks, identifying misleading behaviors and clarifying when it is and isn't effective.

## Abstract

Data Shapley provides a principled approach to data valuation and plays a crucial role in data-centric machine learning (ML) research. Data selection is considered a standard application of Data Shapley. However, its data selection performance has shown to be inconsistent across settings in the literature. This study aims to deepen our understanding of this phenomenon. We introduce a hypothesis testing framework and show that Data Shapley’s performance can be no better than random selection without specific constraints on utility functions. We identify a class of utility functions, monotonically transformed modular functions, within which Data Shapley optimally selects data. Based on this insight, we propose a heuristic for predicting Data Shapley’s effectiveness in data selection tasks. Our experiments corroborate these findings, adding new insights into when Data Shapley may or may not succeed.