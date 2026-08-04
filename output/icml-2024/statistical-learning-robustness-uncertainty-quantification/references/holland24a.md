---
title: "Criterion Collapse and Loss Distribution Control"
source: "https://proceedings.mlr.press/v235/holland24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/holland24a/holland24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'optimization-algorithms-convergence-theory']
tags: ['criterion-collapse', 'loss-distribution', 'DRO', 'CVaR', 'risk-minimization']
venue: "ICML 2024"
tldr: "Analyzes conditions under which optimizing one loss criterion implies optimality under another, focusing on collapse to error probability minimizers."
---

# Criterion Collapse and Loss Distribution Control

**Source**: [https://proceedings.mlr.press/v235/holland24a.html](https://proceedings.mlr.press/v235/holland24a.html)

**TLDR**: Analyzes conditions under which optimizing one loss criterion implies optimality under another, focusing on collapse to error probability minimizers.

## Abstract

In this work, we consider the notion of "criterion collapse," in which optimization of one metric implies optimality in another, with a particular focus on conditions for collapse into error probability minimizers under a wide variety of learning criteria, ranging from DRO and OCE risks (CVaR, tilted ERM) to non-monotonic criteria underlying recent ascent-descent algorithms explored in the literature (Flooding, SoftAD). We show how collapse in the context of losses with a Bernoulli distribution goes far beyond existing results for CVaR and DRO, then expand our scope to include surrogate losses, showing conditions where monotonic criteria such as tilted ERM cannot avoid collapse, whereas non-monotonic alternatives can.