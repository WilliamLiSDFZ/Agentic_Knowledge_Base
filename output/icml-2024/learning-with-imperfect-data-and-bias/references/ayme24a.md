---
title: "Random features models: a way to study the success of naive imputation"
source: "https://proceedings.mlr.press/v235/ayme24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ayme24a/ayme24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'fast-sketching-methods-for-large-scale-optimization']
tags: ['naive-imputation', 'missing-data', 'random-features', 'bias-analysis', 'prediction']
venue: "ICML 2024"
tldr: "Uses random feature models to theoretically explain why naive constant imputation works surprisingly well for prediction despite apparent bias."
---

# Random features models: a way to study the success of naive imputation

**Source**: [https://proceedings.mlr.press/v235/ayme24a.html](https://proceedings.mlr.press/v235/ayme24a.html)

**TLDR**: Uses random feature models to theoretically explain why naive constant imputation works surprisingly well for prediction despite apparent bias.

## Abstract

Constant (naive) imputation is still widely used in practice as this is a first easy-to-use technique to deal with missing data. Yet, this simple method could be expected to induce a large bias for prediction purposes, as the imputed input may strongly differ from the true underlying data. However, recent works suggest that this bias is low in the context of high-dimensional linear predictors when data is supposed to be missing completely at random (MCAR). This paper completes the picture for linear predictors by confirming the intuition that the bias is negligible and that surprisingly naive imputation also remains relevant in very low dimension. To this aim, we consider a unique underlying random features model, which offers a rigorous framework for studying predictive performances, whilst the dimension of the observed features varies. Building on these theoretical results, we establish finite-sample bounds on stochastic gradient (SGD) predictors applied to zero-imputed data, a strategy particularly well suited for large-scale learning. If the MCAR assumption appears to be strong, we show that similar favorable behaviors occur for more complex missing data scenarios.