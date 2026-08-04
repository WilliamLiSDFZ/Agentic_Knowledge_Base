---
title: "Total Variation Floodgate for Variable Importance Inference in Classification"
source: "https://proceedings.mlr.press/v235/wang24ad.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24ad/wang24ad.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'ai-explainability-uncertainty-human-decision-making']
tags: ['variable-importance', 'total-variation', 'classification', 'inference']
venue: "ICML 2024"
tldr: "Expected total variation is proposed as an interpretable measure of variable importance in classification with a statistically valid inference procedure."
---

# Total Variation Floodgate for Variable Importance Inference in Classification

**Source**: [https://proceedings.mlr.press/v235/wang24ad.html](https://proceedings.mlr.press/v235/wang24ad.html)

**TLDR**: Expected total variation is proposed as an interpretable measure of variable importance in classification with a statistically valid inference procedure.

## Abstract

Inferring variable importance is the key goal of many scientific studies, where researchers seek to learn the effect of a feature $X$ on the outcome $Y$ in the presence of confounding variables $Z$. Focusing on classification problems, we define the expected total variation (ETV), which is an intuitive and deterministic measure of variable importance that does not rely on any model assumption. We then introduce algorithms for statistical inference on the ETV under design-based/model-X assumptions. We name our method Total Variation Floodgate in reference to its shared high-level structure with the Floodgate method of Zhang & Janson (2020). The algorithms we introduce can leverage any user-specified regression function and produce asymptotic lower confidence bounds for the ETV. We show the effectiveness of our algorithms with simulations and a case study in conjoint analysis on the US general election.