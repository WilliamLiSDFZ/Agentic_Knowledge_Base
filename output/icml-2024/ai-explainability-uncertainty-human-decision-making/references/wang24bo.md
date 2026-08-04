---
title: "Probabilistic Conceptual Explainers: Trustworthy Conceptual Explanations for Vision Foundation Models"
source: "https://proceedings.mlr.press/v235/wang24bo.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24bo/wang24bo.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'llm-geometry-and-interpretability-research']
tags: ['concept-based-explanations', 'vision-transformers', 'probabilistic-explainability', 'foundation-models']
venue: "ICML 2024"
tldr: "Introduces probabilistic conceptual explainers providing trustworthy, uncertainty-aware concept-based explanations for vision transformer foundation models."
---

# Probabilistic Conceptual Explainers: Trustworthy Conceptual Explanations for Vision Foundation Models

**Source**: [https://proceedings.mlr.press/v235/wang24bo.html](https://proceedings.mlr.press/v235/wang24bo.html)

**TLDR**: Introduces probabilistic conceptual explainers providing trustworthy, uncertainty-aware concept-based explanations for vision transformer foundation models.

## Abstract

Vision transformers (ViTs) have emerged as a significant area of focus, particularly for their capacity to be jointly trained with large language models and to serve as robust vision foundation models. Yet, the development of trustworthy explanation methods for ViTs has lagged, particularly in the context of post-hoc interpretations of ViT predictions. Existing sub-image selection approaches, such as feature-attribution and conceptual models, fall short in this regard. This paper proposes five desiderata for explaining ViTs – faithfulness, stability, sparsity, multi-level structure, and parsimony – and demonstrates the inadequacy of current methods in meeting these criteria comprehensively. We introduce a variational Bayesian explanation framework, dubbed ProbAbilistic Concept Explainers (PACE), which models the distributions of patch embeddings to provide trustworthy post-hoc conceptual explanations. Our qualitative analysis reveals the distributions of patch-level concepts, elucidating the effectiveness of ViTs by modeling the joint distribution of patch embeddings and ViT’s predictions. Moreover, these patch-level explanations bridge the gap between image-level and dataset-level explanations, thus completing the multi-level structure of PACE. Through extensive experiments on both synthetic and real-world datasets, we demonstrate that PACE surpasses state-of-the-art methods in terms of the defined desiderata.