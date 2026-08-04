---
title: "Inverse-Variance Weighting for Estimation of Heterogeneous Treatment Effects"
source: "https://proceedings.mlr.press/v235/fisher24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/fisher24a/fisher24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'probabilistic-generating-circuits-research']
tags: ['causal-inference', 'CATE-estimation', 'pseudo-outcome-regression']
venue: "ICML 2024"
tldr: "Inverse-variance weighting in pseudo-outcome regression is identified as the key driver of performance in heterogeneous treatment effect estimation."
---

# Inverse-Variance Weighting for Estimation of Heterogeneous Treatment Effects

**Source**: [https://proceedings.mlr.press/v235/fisher24a.html](https://proceedings.mlr.press/v235/fisher24a.html)

**TLDR**: Inverse-variance weighting in pseudo-outcome regression is identified as the key driver of performance in heterogeneous treatment effect estimation.

## Abstract

Many methods for estimating conditional average treatment effects (CATEs) can be expressed as weighted pseudo-outcome regressions (PORs). Previous comparisons of POR techniques have paid careful attention to the choice of pseudo-outcome transformation. However, we argue that the dominant driver of performance is actually the choice of weights. For example, we point out that R-Learning implicitly performs a POR with inverse-variance weights (IVWs). In the CATE setting, IVWs mitigate the instability associated with inverse-propensity weights, and lead to convenient simplifications of bias terms. We demonstrate the superior performance of IVWs in simulations, and derive convergence rates for IVWs that are, to our knowledge, the fastest yet shown without assuming knowledge of the covariate distribution.