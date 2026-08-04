---
title: "On Positivity Condition for Causal Inference"
source: "https://proceedings.mlr.press/v235/hwang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hwang24a/hwang24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['causal-inference', 'positivity', 'overlap', 'observational-study', 'identification']
venue: "ICML 2024"
tldr: "Analyzes the positivity condition for causal inference in observational studies and proposes relaxed alternatives for valid estimation."
---

# On Positivity Condition for Causal Inference

**Source**: [https://proceedings.mlr.press/v235/hwang24a.html](https://proceedings.mlr.press/v235/hwang24a.html)

**TLDR**: Analyzes the positivity condition for causal inference in observational studies and proposes relaxed alternatives for valid estimation.

## Abstract

Identifying and estimating a causal effect is a fundamental task when researchers want to infer a causal effect using an observational study without experiments. A conventional assumption is the strict positivity of the given distribution, or so called positivity (or overlap) under the unconfounded assumption that the probabilities of treatments are positive. However, there exist many environments where neither observational data exhibits strict positivity nor unconfounded assumption holds. Against this background, we examine the graphical counterpart of the conventional positivity condition so as to license the use of identification formula without strict positivity. In particular, we explore various approaches, including analysis in a post-hoc manner, do-calculus, $Q$-decomposition, and algorithmic, to yielding a positivity condition for an identification formula, where we relate them, providing a comprehensive view. We further discuss the design of a positivity-aware identification algorithm based on the theoretical characterization of identification formulas.