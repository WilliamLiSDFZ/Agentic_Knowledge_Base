---
title: "Learning Cognitive Maps from Transformer Representations for Efficient Planning in Partially Observed Environments"
source: "https://proceedings.mlr.press/v235/dedieu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dedieu24a/dedieu24a.pdf"
categories: ['large-language-model-alignment-and-capabilities', 'graph-clustering-and-matching-algorithms']
tags: ['transformers', 'cognitive-maps', 'planning', 'partial-observability', 'world-models']
venue: "ICML 2024"
tldr: "Extracts cognitive map representations from transformer models to enable efficient planning in partially observed environments."
---

# Learning Cognitive Maps from Transformer Representations for Efficient Planning in Partially Observed Environments

**Source**: [https://proceedings.mlr.press/v235/dedieu24a.html](https://proceedings.mlr.press/v235/dedieu24a.html)

**TLDR**: Extracts cognitive map representations from transformer models to enable efficient planning in partially observed environments.

## Abstract

Despite their stellar performance on a wide range of tasks, including in-context tasks only revealed during inference, vanilla transformers and variants trained for next-token predictions (a) do not learn an explicit world model of their environment which can be flexibly queried and (b) cannot be used for planning or navigation. In this paper, we consider partially observed environments (POEs), where an agent receives perceptually aliased observations as it navigates, which makes path planning hard. We introduce a transformer with (multiple) discrete bottleneck(s), TDB, whose latent codes learn a compressed representation of the history of observations and actions. After training a TDB to predict the future observation(s) given the history, we extract interpretable cognitive maps of the environment from its active bottleneck(s) indices. These maps are then paired with an external solver to solve (constrained) path planning problems. First, we show that a TDB trained on POEs (a) retains the near-perfect predictive performance of a vanilla transformer or an LSTM while (b) solving shortest path problems exponentially faster. Second, a TDB extracts interpretable representations from text datasets, while reaching higher in-context accuracy than vanilla sequence models. Finally, in new POEs, a TDB (a) reaches near-perfect in-context accuracy, (b) learns accurate in-context cognitive maps (c) solves in-context path planning problems.