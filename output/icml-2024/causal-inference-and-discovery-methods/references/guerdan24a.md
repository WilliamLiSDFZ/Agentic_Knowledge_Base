---
title: "Predictive Performance Comparison of Decision Policies Under Confounding"
source: "https://proceedings.mlr.press/v235/guerdan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/guerdan24a/guerdan24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'fairness-aware-algorithmic-decision-making']
tags: ['confounding', 'decision-policy', 'predictive-performance', 'causal-inference', 'observational-data']
venue: "ICML 2024"
tldr: "A framework for comparing predictive model performance against existing decision-making policies under confounding."
---

# Predictive Performance Comparison of Decision Policies Under Confounding

**Source**: [https://proceedings.mlr.press/v235/guerdan24a.html](https://proceedings.mlr.press/v235/guerdan24a.html)

**TLDR**: A framework for comparing predictive model performance against existing decision-making policies under confounding.

## Abstract

Predictive models are often introduced to decision-making tasks under the rationale that they improve performance over an existing decision-making policy. However, it is challenging to compare predictive performance against an existing decision-making policy that is generally under-specified and dependent on unobservable factors. These sources of uncertainty are often addressed in practice by making strong assumptions about the data-generating mechanism. In this work, we propose a method to compare the predictive performance of decision policies under a variety of modern identification approaches from the causal inference and off-policy evaluation literatures (e.g., instrumental variable, marginal sensitivity model, proximal variable). Key to our method is the insight that there are regions of uncertainty that we can safely ignore in the policy comparison. We develop a practical approach for finite-sample estimation of regret intervals under no assumptions on the parametric form of the status quo policy. We verify our framework theoretically and via synthetic data experiments. We conclude with a real-world application using our framework to support a pre-deployment evaluation of a proposed modification to a healthcare enrollment policy.