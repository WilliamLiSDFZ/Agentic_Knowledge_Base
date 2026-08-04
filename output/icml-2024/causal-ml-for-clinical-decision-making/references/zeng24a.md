---
title: "Continuous Treatment Effects with Surrogate Outcomes"
source: "https://proceedings.mlr.press/v235/zeng24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zeng24a/zeng24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'causal-ml-for-clinical-decision-making']
tags: ['causal-inference', 'surrogate-outcomes', 'continuous-treatment']
venue: "ICML 2024"
tldr: "A method for estimating continuous treatment effects when primary outcomes are partially missing by leveraging surrogate outcomes under covariate-dependent missingness."
---

# Continuous Treatment Effects with Surrogate Outcomes

**Source**: [https://proceedings.mlr.press/v235/zeng24a.html](https://proceedings.mlr.press/v235/zeng24a.html)

**TLDR**: A method for estimating continuous treatment effects when primary outcomes are partially missing by leveraging surrogate outcomes under covariate-dependent missingness.

## Abstract

In many real-world causal inference applications, the primary outcomes (labels) are often partially missing, especially if they are expensive or difficult to collect. If the missingness depends on covariates (i.e., missingness is not completely at random), analyses based on fully observed samples alone may be biased. Incorporating surrogates, which are fully observed post-treatment variables related to the primary outcome, can improve estimation in this case. In this paper, we study the role of surrogates in estimating continuous treatment effects and propose a doubly robust method to efficiently incorporate surrogates in the analysis, which uses both labeled and unlabeled data and does not suffer from the above selection bias problem. Importantly, we establish the asymptotic normality of the proposed estimator and show possible improvements on the variance compared with methods that solely use labeled data. Extensive simulations show our methods enjoy appealing empirical performance.