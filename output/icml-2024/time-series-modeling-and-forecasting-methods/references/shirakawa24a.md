---
title: "Longitudinal Targeted Minimum Loss-based Estimation with Temporal-Difference Heterogeneous Transformer"
source: "https://proceedings.mlr.press/v235/shirakawa24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shirakawa24a/shirakawa24a.pdf"
categories: ['causal-ml-for-clinical-decision-making', 'time-series-modeling-and-forecasting-methods']
tags: ['targeted-learning', 'counterfactual-estimation', 'transformer-architecture']
venue: "ICML 2024"
tldr: "Introduces Deep LTMLE, combining transformer architectures with targeted minimum loss-based estimation for causal inference in longitudinal settings."
---

# Longitudinal Targeted Minimum Loss-based Estimation with Temporal-Difference Heterogeneous Transformer

**Source**: [https://proceedings.mlr.press/v235/shirakawa24a.html](https://proceedings.mlr.press/v235/shirakawa24a.html)

**TLDR**: Introduces Deep LTMLE, combining transformer architectures with targeted minimum loss-based estimation for causal inference in longitudinal settings.

## Abstract

We propose Deep Longitudinal Targeted Minimum Loss-based Estimation (Deep LTMLE), a novel approach to estimate the counterfactual mean of outcome under dynamic treatment policies in longitudinal problem settings. Our approach utilizes a transformer architecture with heterogeneous type embedding trained using temporal-difference learning. After obtaining an initial estimate using the transformer, following the targeted minimum loss-based likelihood estimation (TMLE) framework, we statistically corrected for the bias commonly associated with machine learning algorithms. Furthermore, our method also facilitates statistical inference by enabling the provision of 95% confidence intervals grounded in asymptotic statistical theory. Simulation results demonstrate our method’s superior performance over existing approaches, particularly in complex, long time-horizon scenarios. It remains effective in small-sample, short-duration contexts, matching the performance of asymptotically efficient estimators. To demonstrate our method in practice, we applied our method to estimate counterfactual mean outcomes for standard versus intensive blood pressure management strategies in a real-world cardiovascular epidemiology cohort study.