---
title: "Multiply-Robust Causal Change Attribution"
source: "https://proceedings.mlr.press/v235/quintas-martinez24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/quintas-martinez24a/quintas-martinez24a.pdf"
categories: ['causal-inference-and-discovery-methods', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['causal-inference', 'change-attribution', 'multiply-robust', 'distributional-change', 'reweighting']
venue: "ICML 2024"
tldr: "A multiply-robust estimation strategy for attributing distributional changes in outcomes to their causal sources."
---

# Multiply-Robust Causal Change Attribution

**Source**: [https://proceedings.mlr.press/v235/quintas-martinez24a.html](https://proceedings.mlr.press/v235/quintas-martinez24a.html)

**TLDR**: A multiply-robust estimation strategy for attributing distributional changes in outcomes to their causal sources.

## Abstract

Comparing two samples of data, we observe a change in the distribution of an outcome variable. In the presence of multiple explanatory variables, how much of the change can be explained by each possible cause? We develop a new estimation strategy that, given a causal model, combines regression and re-weighting methods to quantify the contribution of each causal mechanism. Our proposed methodology is multiply robust, meaning that it still recovers the target parameter under partial misspecification. We prove that our estimator is consistent and asymptotically normal. Moreover, it can be incorporated into existing frameworks for causal attribution, such as Shapley values, which will inherit the consistency and large-sample distribution properties. Our method demonstrates excellent performance in Monte Carlo simulations, and we show its usefulness in an empirical application. Our method is implemented as part of the Python library “DoWhy“ (Sharma & Kiciman, 2020; Blöbaum et al., 2022).