---
title: "TVE: Learning Meta-attribution for Transferable Vision Explainer"
source: "https://proceedings.mlr.press/v235/wang24j.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24j/wang24j.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'knowledge-distillation-methods-and-applications']
tags: ['explainability', 'meta-attribution', 'transferable-explanations', 'saliency', 'model-agnostic']
venue: "ICML 2024"
tldr: "TVE proposes a meta-attribution framework that learns transferable visual explanations across different models and tasks via amortized explainer training."
---

# TVE: Learning Meta-attribution for Transferable Vision Explainer

**Source**: [https://proceedings.mlr.press/v235/wang24j.html](https://proceedings.mlr.press/v235/wang24j.html)

**TLDR**: TVE proposes a meta-attribution framework that learns transferable visual explanations across different models and tasks via amortized explainer training.

## Abstract

Explainable machine learning significantly improves the transparency of deep neural networks. However, existing work is constrained to explaining the behavior of individual model predictions, and lacks the ability to transfer the explanation across various models and tasks. This limitation results in explaining various tasks being time- and resource-consuming. To address this problem, we introduce a Transferable Vision Explainer (TVE) that can effectively explain various vision models in downstream tasks. Specifically, the transferability of TVE is realized through a pre-training process on large-scale datasets towards learning the meta-attribution. This meta-attribution leverages the versatility of generic backbone encoders to comprehensively encode the attribution knowledge for the input instance, which enables TVE to seamlessly transfer to explaining various downstream tasks, without the need for training on task-specific data. Empirical studies involve explaining three different architectures of vision models across three diverse downstream datasets. The experiment results indicate TVE is effective in explaining these tasks without the need for additional training on downstream data.