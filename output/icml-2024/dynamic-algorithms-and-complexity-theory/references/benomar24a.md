---
title: "Non-clairvoyant Scheduling with Partial Predictions"
source: "https://proceedings.mlr.press/v235/benomar24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/benomar24a/benomar24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'dynamic-algorithms-and-complexity-theory']
tags: ['scheduling', 'learning-augmented-algorithms', 'predictions', 'non-clairvoyant', 'partial-information']
venue: "ICML 2024"
tldr: "Studies non-clairvoyant scheduling with partial predictions, extending learning-augmented algorithm frameworks to settings with limited prediction access."
---

# Non-clairvoyant Scheduling with Partial Predictions

**Source**: [https://proceedings.mlr.press/v235/benomar24a.html](https://proceedings.mlr.press/v235/benomar24a.html)

**TLDR**: Studies non-clairvoyant scheduling with partial predictions, extending learning-augmented algorithm frameworks to settings with limited prediction access.

## Abstract

The non-clairvoyant scheduling problem has gained new interest within learning-augmented algorithms, where the decision-maker is equipped with predictions without any quality guarantees. In practical settings, access to predictions may be reduced to specific instances, due to cost or data limitations. Our investigation focuses on scenarios where predictions for only $B$ job sizes out of $n$ are available to the algorithm. We first establish near-optimal lower bounds and algorithms in the case of perfect predictions. Subsequently, we present a learning-augmented algorithm satisfying the robustness, consistency, and smoothness criteria, and revealing a novel tradeoff between consistency and smoothness inherent in the scenario with a restricted number of predictions.