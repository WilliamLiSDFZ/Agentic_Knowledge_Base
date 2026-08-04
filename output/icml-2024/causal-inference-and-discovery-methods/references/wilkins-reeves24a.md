---
title: "Multiply Robust Estimation for Local Distribution Shifts with Multiple Domains"
source: "https://proceedings.mlr.press/v235/wilkins-reeves24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wilkins-reeves24a/wilkins-reeves24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'causal-inference-and-discovery-methods']
tags: ['distribution-shift', 'multiply-robust-estimation', 'multi-domain', 'covariate-shift']
venue: "ICML 2024"
tldr: "A multiply robust estimation framework handles local distribution shifts across multiple population segments with theoretical guarantees."
---

# Multiply Robust Estimation for Local Distribution Shifts with Multiple Domains

**Source**: [https://proceedings.mlr.press/v235/wilkins-reeves24a.html](https://proceedings.mlr.press/v235/wilkins-reeves24a.html)

**TLDR**: A multiply robust estimation framework handles local distribution shifts across multiple population segments with theoretical guarantees.

## Abstract

Distribution shifts are ubiquitous in real-world machine learning applications, posing a challenge to the generalization of models trained on one data distribution to another. We focus on scenarios where data distributions vary across multiple segments of the entire population and only make local assumptions about the differences between training and test (deployment) distributions within each segment. We propose a two-stage multiply robust estimation method to improve model performance on each individual segment for tabular data analysis. The method involves fitting a linear combination of the based models, learned using clusters of training data from multiple segments, followed by a refinement step for each segment. Our method is designed to be implemented with commonly used off-the-shelf machine learning models. We establish theoretical guarantees on the generalization bound of the method on the test risk. With extensive experiments on synthetic and real datasets, we demonstrate that the proposed method substantially improves over existing alternatives in prediction accuracy and robustness on both regression and classification tasks. We also assess its effectiveness on a user city prediction dataset from Meta.