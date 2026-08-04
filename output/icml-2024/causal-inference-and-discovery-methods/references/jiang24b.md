---
title: "Conditional Common Entropy for Instrumental Variable Testing and Partial Identification"
source: "https://proceedings.mlr.press/v235/jiang24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jiang24b/jiang24b.pdf"
categories: ['causal-inference-and-discovery-methods', 'sampling-compression-and-dimensionality-reduction']
tags: ['instrumental-variables', 'causal-identification', 'conditional-common-entropy', 'partial-identification']
venue: "ICML 2024"
tldr: "Conditional common entropy is introduced as a tool for instrumental variable validity testing and partial identification of causal effects without linearity assumptions."
---

# Conditional Common Entropy for Instrumental Variable Testing and Partial Identification

**Source**: [https://proceedings.mlr.press/v235/jiang24b.html](https://proceedings.mlr.press/v235/jiang24b.html)

**TLDR**: Conditional common entropy is introduced as a tool for instrumental variable validity testing and partial identification of causal effects without linearity assumptions.

## Abstract

Instrumental variables (IVs) are widely used for estimating causal effects. There are two main challenges when using instrumental variables. First of all, using IV without additional assumptions such as linearity, the causal effect may still not be identifiable. Second, when selecting an IV, the validity of the selected IV is typically not testable since the causal graph is not identifiable from observational data. In this paper, we propose a method for bounding the causal effect with instrumental variables under weak confounding. In addition, we present a novel criterion to falsify the IV with side information about the confounder. We demonstrate the utility of the proposed method with simulated and real-world datasets.