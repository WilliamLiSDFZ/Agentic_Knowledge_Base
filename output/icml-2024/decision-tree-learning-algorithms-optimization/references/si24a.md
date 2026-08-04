---
title: "InterpreTabNet: Distilling Predictive Signals from Tabular Data by Salient Feature Interpretation"
source: "https://proceedings.mlr.press/v235/si24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/si24a/si24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'decision-tree-learning-algorithms-optimization']
tags: ['tabular-data', 'attention-mechanism', 'interpretability']
venue: "ICML 2024"
tldr: "Proposes InterpreTabNet, which distills salient feature signals from tabular data using sparse attention masks for improved interpretability."
---

# InterpreTabNet: Distilling Predictive Signals from Tabular Data by Salient Feature Interpretation

**Source**: [https://proceedings.mlr.press/v235/si24a.html](https://proceedings.mlr.press/v235/si24a.html)

**TLDR**: Proposes InterpreTabNet, which distills salient feature signals from tabular data using sparse attention masks for improved interpretability.

## Abstract

Tabular data are omnipresent in various sectors of industries. Neural networks for tabular data such as TabNet have been proposed to make predictions while leveraging the attention mechanism for interpretability. However, the inferred attention masks are often dense, making it challenging to come up with rationales about the predictive signal. To remedy this, we propose InterpreTabNet, a variant of the TabNet model that models the attention mechanism as a latent variable sampled from a Gumbel-Softmax distribution. This enables us to regularize the model to learn distinct concepts in the attention masks via a KL Divergence regularizer. It prevents overlapping feature selection by promoting sparsity which maximizes the model’s efficacy and improves interpretability to determine the important features when predicting the outcome. To assist in the interpretation of feature interdependencies from our model, we employ a large language model (GPT-4) and use prompt engineering to map from the learned feature mask onto natural language text describing the learned signal. Through comprehensive experiments on real-world datasets, we demonstrate that InterpreTabNet outperforms previous methods for interpreting tabular data while attaining competitive accuracy.