---
title: "Local Feature Selection without Label or Feature Leakage for Interpretable Machine Learning Predictions"
source: "https://proceedings.mlr.press/v235/oosterhuis24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/oosterhuis24a/oosterhuis24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making']
tags: ['local-feature-selection', 'interpretability', 'feature-leakage', 'instance-specific-explanations']
venue: "ICML 2024"
tldr: "Proposes a local feature selection method that avoids label and feature leakage for trustworthy model interpretability."
---

# Local Feature Selection without Label or Feature Leakage for Interpretable Machine Learning Predictions

**Source**: [https://proceedings.mlr.press/v235/oosterhuis24a.html](https://proceedings.mlr.press/v235/oosterhuis24a.html)

**TLDR**: Proposes a local feature selection method that avoids label and feature leakage for trustworthy model interpretability.

## Abstract

Local feature selection in machine learning provides instance-specific explanations by focusing on the most relevant features for each prediction, enhancing the interpretability of complex models. However, such methods tend to produce misleading explanations by encoding additional information in their selections. In this work, we attribute the problem of misleading selections by formalizing the concepts of label and feature leakage. We rigorously derive the necessary and sufficient conditions under which we can guarantee no leakage, and show existing methods do not meet these conditions. Furthermore, we propose the first local feature selection method that is proven to have no leakage called SUWR. Our experimental results indicate that SUWR is less prone to overfitting and combines state-of-the-art predictive performance with high feature-selection sparsity. Our generic and easily extendable formal approach provides a strong theoretical basis for future work on interpretability with reliable explanations.