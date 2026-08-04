---
title: "Feature Importance Disparities for Data Bias Investigations"
source: "https://proceedings.mlr.press/v235/chang24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chang24a/chang24a.pdf"
categories: ['fairness-aware-algorithmic-decision-making', 'ai-explainability-uncertainty-human-decision-making']
tags: ['feature-importance', 'data-bias', 'algorithmic-fairness', 'bias-investigation']
venue: "ICML 2024"
tldr: "Demonstrates how disparities in feature importance across demographic groups can reveal and diagnose data collection biases in classifiers."
---

# Feature Importance Disparities for Data Bias Investigations

**Source**: [https://proceedings.mlr.press/v235/chang24a.html](https://proceedings.mlr.press/v235/chang24a.html)

**TLDR**: Demonstrates how disparities in feature importance across demographic groups can reveal and diagnose data collection biases in classifiers.

## Abstract

It is widely held that one cause of downstream bias in classifiers is bias present in the training data. Rectifying such biases may involve context-dependent interventions such as training separate models on subgroups, removing features with bias in the collection process, or even conducting real-world experiments to ascertain sources of bias. Despite the need for such data bias investigations, few automated methods exist to assist practitioners in these efforts. In this paper, we present one such method that given a dataset $X$ consisting of protected and unprotected features, outcomes $y$, and a regressor $h$ that predicts $y$ given $X$, outputs a tuple $(f_j, g)$, with the following property: $g$ corresponds to a subset of the training dataset $(X, y)$, such that the $j^{th}$ feature $f_j$ has much larger (or smaller) influence in the subgroup $g$, than on the dataset overall, which we call feature importance disparity (FID). We show across $4$ datasets and $4$ common feature importance methods of broad interest to the machine learning community that we can efficiently find subgroups with large FID values even over exponentially large subgroup classes and in practice these groups correspond to subgroups with potentially serious bias issues as measured by standard fairness metrics.