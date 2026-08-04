---
title: "Combining Experimental and Historical Data for Policy Evaluation"
source: "https://proceedings.mlr.press/v235/li24bh.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bh/li24bh.pdf"
categories: ['difference-in-differences-based-policy-evaluation', 'causal-inference-and-discovery-methods']
tags: ['policy-evaluation', 'data-integration', 'experimental-historical-data']
venue: "ICML 2024"
tldr: "Proposes data integration methods combining experimental and historical datasets for improved policy evaluation under multiple data sources."
---

# Combining Experimental and Historical Data for Policy Evaluation

**Source**: [https://proceedings.mlr.press/v235/li24bh.html](https://proceedings.mlr.press/v235/li24bh.html)

**TLDR**: Proposes data integration methods combining experimental and historical datasets for improved policy evaluation under multiple data sources.

## Abstract

This paper studies policy evaluation with multiple data sources, especially in scenarios that involve one experimental dataset with two arms, complemented by a historical dataset generated under a single control arm. We propose novel data integration methods that linearly integrate base policy value estimators constructed based on the experimental and historical data, with weights optimized to minimize the mean square error (MSE) of the resulting combined estimator. We further apply the pessimistic principle to obtain more robust estimators, and extend these developments to sequential decision making. Theoretically, we establish non-asymptotic error bounds for the MSEs of our proposed estimators, and derive their oracle, efficiency and robustness properties across a broad spectrum of reward shift scenarios. Numerical experiments and real-data-based analyses from a ridesharing company demonstrate the superior performance of the proposed estimators.