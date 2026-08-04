---
title: "Observable Propagation: Uncovering Feature Vectors in Transformers"
source: "https://proceedings.mlr.press/v235/dunefsky24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/dunefsky24a/dunefsky24a.pdf"
categories: ['llm-geometry-and-interpretability-research']
tags: ['mechanistic-interpretability', 'feature-vectors', 'transformers', 'linear-representations']
venue: "ICML 2024"
tldr: "Observable Propagation is a method to uncover linear feature vectors in transformers by tracking observable quantities through the computation graph."
---

# Observable Propagation: Uncovering Feature Vectors in Transformers

**Source**: [https://proceedings.mlr.press/v235/dunefsky24a.html](https://proceedings.mlr.press/v235/dunefsky24a.html)

**TLDR**: Observable Propagation is a method to uncover linear feature vectors in transformers by tracking observable quantities through the computation graph.

## Abstract

A key goal of current mechanistic interpretability research in NLP is to find linear features (also called "feature vectors") for transformers: directions in activation space corresponding to concepts that are used by a given model in its computation. Present state-of-the-art methods for finding linear features require large amounts of labelled data – both laborious to acquire and computationally expensive to utilize. In this work, we introduce a novel method, called "observable propagation" (in short: ObProp), for finding linear features used by transformer language models in computing a given task – using almost no data. Our paradigm centers on the concept of "observables", linear functionals corresponding to given tasks. We then introduce a mathematical theory for the analysis of feature vectors, including a similarity metric between feature vectors called the coupling coefficient which estimates the degree to which one feature’s output correlates with another’s. We use ObProp to perform extensive qualitative investigations into several tasks, including gendered occupational bias, political party prediction, and programming language detection. Our results suggest that ObProp surpasses traditional approaches for finding feature vectors in the low-data regime, and that ObProp can be used to better understand the mechanisms responsible for bias in large language models.