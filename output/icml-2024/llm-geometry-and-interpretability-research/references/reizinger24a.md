---
title: "Position: Understanding LLMs Requires More Than Statistical Generalization"
source: "https://proceedings.mlr.press/v235/reizinger24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/reizinger24a/reizinger24a.pdf"
categories: ['position-papers-on-ml-research-directions', 'llm-geometry-and-interpretability-research']
tags: ['LLM-understanding', 'statistical-generalization', 'deep-learning-theory', 'position-paper', 'overparameterization']
venue: "ICML 2024"
tldr: "This position paper argues that understanding LLMs requires perspectives beyond statistical generalization theory, calling for new theoretical frameworks."
---

# Position: Understanding LLMs Requires More Than Statistical Generalization

**Source**: [https://proceedings.mlr.press/v235/reizinger24a.html](https://proceedings.mlr.press/v235/reizinger24a.html)

**TLDR**: This position paper argues that understanding LLMs requires perspectives beyond statistical generalization theory, calling for new theoretical frameworks.

## Abstract

The last decade has seen blossoming research in deep learning theory attempting to answer, “Why does deep learning generalize?" A powerful shift in perspective precipitated this progress: the study of overparametrized models in the interpolation regime. In this paper, we argue that another perspective shift is due, since some of the desirable qualities of LLMs are not a consequence of good statistical generalization and require a separate theoretical explanation. Our core argument relies on the observation that AR probabilistic models are inherently non-identifiable: models zero or near-zero KL divergence apart—thus, equivalent test loss—can exhibit markedly different behaviors. We support our position with mathematical examples and empirical observations, illustrating why non-identifiability has practical relevance through three case studies: (1) the non-identifiability of zero-shot rule extrapolation; (2) the approximate non-identifiability of in-context learning; and (3) the non-identifiability of fine-tunability. We review promising research directions focusing on LLM-relevant generalization measures, transferability, and inductive biases.