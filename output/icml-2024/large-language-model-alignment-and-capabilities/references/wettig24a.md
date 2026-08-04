---
title: "QuRating: Selecting High-Quality Data for Training Language Models"
source: "https://proceedings.mlr.press/v235/wettig24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wettig24a/wettig24a.pdf"
categories: ['data-selection-and-active-learning-methods', 'large-language-model-alignment-and-capabilities']
tags: ['data-selection', 'pre-training', 'language-models', 'data-quality']
venue: "ICML 2024"
tldr: "QuRating selects high-quality pre-training data for language models by learning to score data according to human quality intuitions beyond simple heuristics."
---

# QuRating: Selecting High-Quality Data for Training Language Models

**Source**: [https://proceedings.mlr.press/v235/wettig24a.html](https://proceedings.mlr.press/v235/wettig24a.html)

**TLDR**: QuRating selects high-quality pre-training data for language models by learning to score data according to human quality intuitions beyond simple heuristics.

## Abstract

Selecting high-quality pre-training data is important for creating capable language models, but existing methods rely on simple heuristics. We introduce QuRating, a method for selecting pre-training data that can capture human intuitions about data quality. In this paper, we investigate four qualities - writing style, required expertise, facts & trivia, and educational value - and find that LLMs are able to discern these qualities, especially when making pairwise judgments of texts. We train a QuRater model to learn scalar ratings from pairwise judgments, and use it to annotate a 260B training corpus with quality ratings for each of the four criteria. In our experiments, we select 30B tokens according to the different quality ratings and train 1.3B-parameter language models on the selected data. We find that it is important to balance quality and diversity. When we sample using quality ratings as logits over documents, our models obtain lower perplexity and stronger in-context learning performance than baselines. Our best model is based on educational value and performs similarly to a model trained with uniform sampling for 50% more steps. Beyond data selection, we use the quality ratings to construct a training curriculum which improves performance without changing the training dataset. We extensively analyze the quality ratings and discuss their characteristics, biases, and wider implications.