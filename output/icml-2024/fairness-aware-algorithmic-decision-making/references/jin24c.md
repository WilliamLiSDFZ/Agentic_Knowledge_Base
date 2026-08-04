---
title: "On the Maximal Local Disparity of Fairness-Aware Classifiers"
source: "https://proceedings.mlr.press/v235/jin24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jin24c/jin24c.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['fairness', 'demographic-parity', 'local-disparity', 'classifier-fairness']
venue: "ICML 2024"
tldr: "Maximal local disparity is proposed as a finer-grained fairness metric that captures distributional differences between groups beyond average demographic parity violations."
---

# On the Maximal Local Disparity of Fairness-Aware Classifiers

**Source**: [https://proceedings.mlr.press/v235/jin24c.html](https://proceedings.mlr.press/v235/jin24c.html)

**TLDR**: Maximal local disparity is proposed as a finer-grained fairness metric that captures distributional differences between groups beyond average demographic parity violations.

## Abstract

Fairness has become a crucial aspect in the development of trustworthy machine learning algorithms. Current fairness metrics to measure the violation of demographic parity have the following drawbacks: (i) the average difference of model predictions on two groups cannot reflect their distribution disparity, and (ii) the overall calculation along all possible predictions conceals the extreme local disparity at or around certain predictions. In this work, we propose a novel fairness metric called Maximal Cumulative ratio Disparity along varying Predictions’ neighborhood (MCDP), for measuring the maximal local disparity of the fairness-aware classifiers. To accurately and efficiently calculate the MCDP, we develop a provably exact and an approximate calculation algorithm that greatly reduces the computational complexity with low estimation error. We further propose a bi-level optimization algorithm using a differentiable approximation of the MCDP for improving the algorithmic fairness. Extensive experiments on both tabular and image datasets validate that our fair training algorithm can achieve superior fairness-accuracy trade-offs.