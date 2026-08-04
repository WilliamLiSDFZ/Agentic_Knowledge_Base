---
title: "Trustworthy Actionable Perturbations"
source: "https://proceedings.mlr.press/v235/friedbaum24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/friedbaum24a/friedbaum24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'llm-geometry-and-interpretability-research']
tags: ['counterfactuals', 'actionable-recourse', 'trustworthy-explanations']
venue: "ICML 2024"
tldr: "Trustworthy actionable perturbations are proposed to ensure counterfactual explanations reflect true causal changes rather than classifier artifacts."
---

# Trustworthy Actionable Perturbations

**Source**: [https://proceedings.mlr.press/v235/friedbaum24a.html](https://proceedings.mlr.press/v235/friedbaum24a.html)

**TLDR**: Trustworthy actionable perturbations are proposed to ensure counterfactual explanations reflect true causal changes rather than classifier artifacts.

## Abstract

Counterfactuals, or modified inputs that lead to a different outcome, are an important tool for understanding the logic used by machine learning classifiers and how to change an undesirable classification. Even if a counterfactual changes a classifier’s decision, however, it may not affect the true underlying class probabilities, i.e. the counterfactual may act like an adversarial attack and “fool” the classifier. We propose a new framework for creating modified inputs that change the true underlying probabilities in a beneficial way which we call Trustworthy Actionable Perturbations (TAP). This includes a novel verification procedure to ensure that TAP change the true class probabilities instead of acting adversarially. Our framework also includes new cost, reward, and goal definitions that are better suited to effectuating change in the real world. We present PAC-learnability results for our verification procedure and theoretically analyze our new method for measuring reward. We also develop a methodology for creating TAP and compare our results to those achieved by previous counterfactual methods.