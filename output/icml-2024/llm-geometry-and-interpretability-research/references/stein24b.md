---
title: "Towards Compositionality in Concept Learning"
source: "https://proceedings.mlr.press/v235/stein24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/stein24b/stein24b.pdf"
categories: ['llm-geometry-and-interpretability-research', 'clustering-methods-and-multi-view-learning']
tags: ['concept-learning', 'compositionality', 'interpretability', 'foundation-models', 'embeddings']
venue: "ICML 2024"
tldr: "A framework is proposed to learn compositional concept representations from foundation model embeddings to improve interpretability and explanation of samples."
---

# Towards Compositionality in Concept Learning

**Source**: [https://proceedings.mlr.press/v235/stein24b.html](https://proceedings.mlr.press/v235/stein24b.html)

**TLDR**: A framework is proposed to learn compositional concept representations from foundation model embeddings to improve interpretability and explanation of samples.

## Abstract

Concept-based interpretability methods offer a lens into the internals of foundation models by decomposing their embeddings into high-level concepts. These concept representations are most useful when they are compositional, meaning that the individual concepts compose to explain the full sample. We show that existing unsupervised concept extraction methods find concepts which are not compositional. To automatically discover compositional concept representations, we identify two salient properties of such representations, and propose Compositional Concept Extraction (CCE) for finding concepts which obey these properties. We evaluate CCE on five different datasets over image and text data. Our evaluation shows that CCE finds more compositional concept representations than baselines and yields better accuracy on four downstream classification tasks.