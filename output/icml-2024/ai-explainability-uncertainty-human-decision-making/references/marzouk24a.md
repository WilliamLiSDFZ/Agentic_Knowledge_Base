---
title: "On the Tractability of SHAP Explanations under Markovian Distributions"
source: "https://proceedings.mlr.press/v235/marzouk24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/marzouk24a/marzouk24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making']
tags: ['SHAP', 'Markovian-distributions', 'tractability']
venue: "ICML 2024"
tldr: "Analyzes the tractability of exact SHAP explanations under Markovian feature distributions, identifying efficiently computable cases."
---

# On the Tractability of SHAP Explanations under Markovian Distributions

**Source**: [https://proceedings.mlr.press/v235/marzouk24a.html](https://proceedings.mlr.press/v235/marzouk24a.html)

**TLDR**: Analyzes the tractability of exact SHAP explanations under Markovian feature distributions, identifying efficiently computable cases.

## Abstract

Thanks to its solid theoretical foundation, the SHAP framework is arguably one the most widely utilized frameworks for local explainability of ML models. Despite its popularity, its exact computation is known to be very challenging, proven to be NP-Hard in various configurations. Recent works have unveiled positive complexity results regarding the computation of the SHAP score for specific model families, encompassing decision trees, random forests, and some classes of boolean circuits. Yet, all these positive results hinge on the assumption of feature independence, often simplistic in real-world scenarios. In this article, we investigate the computational complexity of the SHAP score by relaxing this assumption and introducing a Markovian perspective. We show that, under the Markovian assumption, computing the SHAP score for the class of Weighted automata, Disjoint DNFs and Decision Trees can be performed in polynomial time, offering a first positive complexity result for the problem of SHAP score computation that transcends the limitations of the feature independence assumption.