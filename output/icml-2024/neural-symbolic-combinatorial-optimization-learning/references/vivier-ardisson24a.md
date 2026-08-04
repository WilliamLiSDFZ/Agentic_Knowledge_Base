---
title: "CF-OPT: Counterfactual Explanations for Structured Prediction"
source: "https://proceedings.mlr.press/v235/vivier-ardisson24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/vivier-ardisson24a/vivier-ardisson24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'neural-symbolic-combinatorial-optimization-learning']
tags: ['counterfactual-explanations', 'structured-prediction', 'optimization-layers', 'interpretability', 'deep-learning']
venue: "ICML 2024"
tldr: "Introduces CF-OPT, a method to generate counterfactual explanations for structured prediction pipelines that include optimization layers."
---

# CF-OPT: Counterfactual Explanations for Structured Prediction

**Source**: [https://proceedings.mlr.press/v235/vivier-ardisson24a.html](https://proceedings.mlr.press/v235/vivier-ardisson24a.html)

**TLDR**: Introduces CF-OPT, a method to generate counterfactual explanations for structured prediction pipelines that include optimization layers.

## Abstract

Optimization layers in deep neural networks have enjoyed a growing popularity in structured learning, improving the state of the art on a variety of applications. Yet, these pipelines lack interpretability since they are made of two opaque layers: a highly non-linear prediction model, such as a deep neural network, and an optimization layer, which is typically a complex black-box solver. Our goal is to improve the transparency of such methods by providing counterfactual explanations. We build upon variational autoencoders a principled way of obtaining counterfactuals: working in the latent space leads to a natural notion of plausibility of explanations. We finally introduce a variant of the classic loss for VAE training that improves their performance in our specific structured context. These provide the foundations of CF-OPT, a first-order optimization algorithm that can find counterfactual explanations for a broad class of structured learning architectures. Our numerical results show that both close and plausible explanations can be obtained for problems from the recent literature.