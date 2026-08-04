---
title: "Representation Surgery: Theory and Practice of Affine Steering"
source: "https://proceedings.mlr.press/v235/singh24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/singh24d/singh24d.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'llm-geometry-and-interpretability-research']
tags: ['representation-steering', 'bias-mitigation', 'affine-transformations']
venue: "ICML 2024"
tldr: "Provides theory and practice of affine steering of language model representations to reduce undesirable behaviors like toxicity and bias."
---

# Representation Surgery: Theory and Practice of Affine Steering

**Source**: [https://proceedings.mlr.press/v235/singh24d.html](https://proceedings.mlr.press/v235/singh24d.html)

**TLDR**: Provides theory and practice of affine steering of language model representations to reduce undesirable behaviors like toxicity and bias.

## Abstract

Language models often exhibit undesirable behavior, e.g., generating toxic or gender-biased text. In the case of neural language models, an encoding of the undesirable behavior is often present in the model’s representations. Thus, one natural (and common) approach to prevent the model from exhibiting undesirable behavior is to steer the model’s representations in a manner that reduces the probability of it generating undesirable text. This paper investigates the formal and empirical properties of steering functions, i.e., transformation of the neural language model’s representations that alter its behavior. First, we derive two optimal, in the least-squares sense, affine steering functions under different constraints. Our theory provides justification for existing approaches and offers a novel, improved steering approach. Second, we offer a series of experiments that demonstrate the empirical effectiveness of the methods in mitigating bias and reducing toxic generation.