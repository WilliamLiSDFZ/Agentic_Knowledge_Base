---
title: "Naive Bayes Classifiers over Missing Data: Decision and Poisoning"
source: "https://proceedings.mlr.press/v235/bian24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bian24b/bian24b.pdf"
categories: ['adversarial-robustness-and-model-security', 'learning-with-imperfect-data-and-bias']
tags: ['Naive-Bayes', 'missing-data', 'certifiable-robustness', 'poisoning-attacks']
venue: "ICML 2024"
tldr: "This paper studies the certifiable robustness and poisoning vulnerabilities of Naive Bayes classifiers trained on datasets with missing values."
---

# Naive Bayes Classifiers over Missing Data: Decision and Poisoning

**Source**: [https://proceedings.mlr.press/v235/bian24b.html](https://proceedings.mlr.press/v235/bian24b.html)

**TLDR**: This paper studies the certifiable robustness and poisoning vulnerabilities of Naive Bayes classifiers trained on datasets with missing values.

## Abstract

We study the certifiable robustness of ML classifiers on dirty datasets that could contain missing values. A test point is certifiably robust for an ML classifier if the classifier returns the same prediction for that test point, regardless of which cleaned version (among exponentially many) of the dirty dataset the classifier is trained on. In this paper, we show theoretically that for Naive Bayes Classifiers (NBC) over dirty datasets with missing values: (i) there exists an efficient polynomial time algorithm to decide whether multiple input test points are all certifiably robust over a dirty dataset; and (ii) the data poisoning attack, which aims to make all input test points certifiably non-robust by inserting missing cells to the clean dataset, is in polynomial time for single test points but NP-complete for multiple test points. Extensive experiments demonstrate that our algorithms are efficient and outperform existing baselines.