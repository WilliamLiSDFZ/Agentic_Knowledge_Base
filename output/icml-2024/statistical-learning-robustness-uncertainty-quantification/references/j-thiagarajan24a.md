---
title: "PAGER: Accurate Failure Characterization in Deep Regression Models"
source: "https://proceedings.mlr.press/v235/j-thiagarajan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/j-thiagarajan24a/j-thiagarajan24a.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['failure-detection', 'deep-regression', 'uncertainty-estimation', 'anomaly-detection', 'AI-safety']
venue: "ICML 2024"
tldr: "PAGER characterizes and detects failures in deep regression models by identifying patterns beyond standard epistemic uncertainty estimates."
---

# PAGER: Accurate Failure Characterization in Deep Regression Models

**Source**: [https://proceedings.mlr.press/v235/j-thiagarajan24a.html](https://proceedings.mlr.press/v235/j-thiagarajan24a.html)

**TLDR**: PAGER characterizes and detects failures in deep regression models by identifying patterns beyond standard epistemic uncertainty estimates.

## Abstract

Safe deployment of AI models requires proactive detection of failures to prevent costly errors. To this end, we study the important problem of detecting failures in deep regression models. Existing approaches rely on epistemic uncertainty estimates or inconsistency w.r.t the training data to identify failure. Interestingly, we find that while uncertainties are necessary they are insufficient to accurately characterize failure in practice. Hence, we introduce PAGER (Principled Analysis of Generalization Errors in Regressors), a framework to systematically detect and characterize failures in deep regressors. Built upon the principle of anchored training in deep models, PAGER unifies both epistemic uncertainty and complementary manifold non-conformity scores to accurately organize samples into different risk regimes.