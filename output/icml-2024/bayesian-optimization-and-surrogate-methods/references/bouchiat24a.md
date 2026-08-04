---
title: "Improving Neural Additive Models with Bayesian Principles"
source: "https://proceedings.mlr.press/v235/bouchiat24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bouchiat24a/bouchiat24a.pdf"
categories: ['bayesian-optimization-and-surrogate-methods', 'ai-explainability-uncertainty-human-decision-making']
tags: ['neural-additive-models', 'Bayesian', 'uncertainty-quantification', 'feature-selection']
venue: "ICML 2024"
tldr: "This paper enhances neural additive models with Bayesian principles to provide calibrated uncertainties and enable principled feature and interaction selection."
---

# Improving Neural Additive Models with Bayesian Principles

**Source**: [https://proceedings.mlr.press/v235/bouchiat24a.html](https://proceedings.mlr.press/v235/bouchiat24a.html)

**TLDR**: This paper enhances neural additive models with Bayesian principles to provide calibrated uncertainties and enable principled feature and interaction selection.

## Abstract

Neural additive models (NAMs) enhance the transparency of deep neural networks by handling input features in separate additive sub-networks. However, they lack inherent mechanisms that provide calibrated uncertainties and enable selection of relevant features and interactions. Approaching NAMs from a Bayesian perspective, we augment them in three primary ways, namely by a) providing credible intervals for the individual additive sub-networks; b) estimating the marginal likelihood to perform an implicit selection of features via an empirical Bayes procedure; and c) facilitating the ranking of feature pairs as candidates for second-order interaction in fine-tuned models. In particular, we develop Laplace-approximated NAMs (LA-NAMs), which show improved empirical performance on tabular datasets and challenging real-world medical tasks.