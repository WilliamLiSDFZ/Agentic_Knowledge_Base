---
title: "Beyond the Norms: Detecting Prediction Errors in Regression Models"
source: "https://proceedings.mlr.press/v235/altieri24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/altieri24a/altieri24a.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['anomaly-detection', 'regression', 'uncertainty-quantification']
venue: "ICML 2024"
tldr: "This paper formalizes unreliability detection in regression models by distinguishing aleatoric and model uncertainty to flag prediction errors."
---

# Beyond the Norms: Detecting Prediction Errors in Regression Models

**Source**: [https://proceedings.mlr.press/v235/altieri24a.html](https://proceedings.mlr.press/v235/altieri24a.html)

**TLDR**: This paper formalizes unreliability detection in regression models by distinguishing aleatoric and model uncertainty to flag prediction errors.

## Abstract

This paper tackles the challenge of detecting unreliable behavior in regression algorithms, which may arise from intrinsic variability (e.g., aleatoric uncertainty) or modeling errors (e.g., model uncertainty). First, we formally introduce the notion of unreliability in regression, i.e., when the output of the regressor exceeds a specified discrepancy (or error). Then, using powerful tools for probabilistic modeling, we estimate the discrepancy density, and we measure its statistical diversity using our proposed metric for statistical dissimilarity. In turn, this allows us to derive a data-driven score that expresses the uncertainty of the regression outcome. We show empirical improvements in error detection for multiple regression tasks, consistently outperforming popular baseline approaches, and contributing to the broader field of uncertainty quantification and safe machine learning systems.