---
title: "TabLog: Test-Time Adaptation for Tabular Data Using Logic Rules"
source: "https://proceedings.mlr.press/v235/ren24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ren24b/ren24b.pdf"
categories: ['test-time-adaptation-methods-and-evaluation', 'decision-tree-learning-algorithms-optimization']
tags: ['test-time-adaptation', 'tabular-data', 'logic-rules', 'domain-shift', 'unlabeled-target']
venue: "ICML 2024"
tldr: "TabLog adapts predictive models on tabular data at test time using logic rules derived from unlabeled target domain data without access to source data."
---

# TabLog: Test-Time Adaptation for Tabular Data Using Logic Rules

**Source**: [https://proceedings.mlr.press/v235/ren24b.html](https://proceedings.mlr.press/v235/ren24b.html)

**TLDR**: TabLog adapts predictive models on tabular data at test time using logic rules derived from unlabeled target domain data without access to source data.

## Abstract

We consider the problem of test-time adaptation of predictive models trained on tabular data. Effective solution of this problem requires adaptation of predictive models trained on the source domain to a target domain, using only unlabeled target domain data, without access to source domain data. Existing test-time adaptation methods for tabular data have difficulty coping with the heterogeneous features and their complex dependencies inherent in tabular data. To overcome these limitations, we consider test-time adaptation in the setting wherein the logical structure of the rules is assumed to remain invariant despite distribution shift between source and target domains whereas the numerical parameters associated with the rules and the weights assigned to them can vary to accommodate distribution shift. TabLog discretizes numerical features, models dependencies between heterogeneous features, introduces a novel contrastive loss for coping with distribution shift, and presents an end-to-end framework for efficient training and test-time adaptation by taking advantage of a logical neural network representation of a rule ensemble. We present results of experiments using several benchmark data sets that demonstrate TabLog is competitive with or improves upon the state-of-the-art methods for test-time adaptation of predictive models trained on tabular data. Our code is available at https://github.com/WeijieyingRen/TabLog.