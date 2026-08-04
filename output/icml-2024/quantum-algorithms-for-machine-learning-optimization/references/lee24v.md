---
title: "Binning as a Pretext Task: Improving Self-Supervised Learning in Tabular Domains"
source: "https://proceedings.mlr.press/v235/lee24v.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/lee24v/lee24v.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'quantum-algorithms-for-machine-learning-optimization']
tags: ['self-supervised-learning', 'tabular-data', 'binning', 'pretext-task']
venue: "ICML 2024"
tldr: "Proposes binning as a pretext task for self-supervised learning to improve representation learning on heterogeneous tabular data."
---

# Binning as a Pretext Task: Improving Self-Supervised Learning in Tabular Domains

**Source**: [https://proceedings.mlr.press/v235/lee24v.html](https://proceedings.mlr.press/v235/lee24v.html)

**TLDR**: Proposes binning as a pretext task for self-supervised learning to improve representation learning on heterogeneous tabular data.

## Abstract

The ability of deep networks to learn superior representations hinges on leveraging the proper inductive biases, considering the inherent properties of datasets. In tabular domains, it is critical to effectively handle heterogeneous features (both categorical and numerical) in a unified manner and to grasp irregular functions like piecewise constant functions. To address the challenges in the self-supervised learning framework, we propose a novel pretext task based on the classical binning method. The idea is straightforward: reconstructing the bin indices (either orders or classes) rather than the original values. This pretext task provides the encoder with an inductive bias to capture the irregular dependencies, mapping from continuous inputs to discretized bins, and mitigates the feature heterogeneity by setting all features to have category-type targets. Our empirical investigations ascertain several advantages of binning: capturing the irregular function, compatibility with encoder architecture and additional modifications, standardizing all features into equal sets, grouping similar values within a feature, and providing ordering information. Comprehensive evaluations across diverse tabular datasets corroborate that our method consistently improves tabular representation learning performance for a wide range of downstream tasks. The codes are available in https://github.com/kyungeun-lee/tabularbinning.