---
title: "Counterfactual Metarules for Local and Global Recourse"
source: "https://proceedings.mlr.press/v235/bewley24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bewley24a/bewley24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'causal-inference-and-discovery-methods']
tags: ['counterfactual-explanations', 'recourse', 'model-agnostic', 'rule-based', 'interpretability']
venue: "ICML 2024"
tldr: "Presents T-CREx, a tree-based model-agnostic method that generates counterfactual metarules for local and global recourse explanations."
---

# Counterfactual Metarules for Local and Global Recourse

**Source**: [https://proceedings.mlr.press/v235/bewley24a.html](https://proceedings.mlr.press/v235/bewley24a.html)

**TLDR**: Presents T-CREx, a tree-based model-agnostic method that generates counterfactual metarules for local and global recourse explanations.

## Abstract

We introduce T-CREx, a novel model-agnostic method for local and global counterfactual explanation (CE), which summarises recourse options for both individuals and groups in the form of generalised rules. It leverages tree-based surrogate models to learn the counterfactual rules, alongside metarules denoting their regimes of optimality, providing both a global analysis of model behaviour and diverse recourse options for users. Experiments indicate that T-CREx achieves superior aggregate performance over existing rule-based baselines on a range of CE desiderata, while being orders of magnitude faster to run.