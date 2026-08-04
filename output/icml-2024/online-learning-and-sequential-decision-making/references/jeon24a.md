---
title: "An Information-Theoretic Analysis of In-Context Learning"
source: "https://proceedings.mlr.press/v235/jeon24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jeon24a/jeon24a.pdf"
categories: ['online-learning-and-sequential-decision-making', 'large-language-model-alignment-and-capabilities']
tags: ['in-context-learning', 'information-theory', 'meta-learning', 'Bayes-optimal', 'error-decomposition']
venue: "ICML 2024"
tldr: "An information-theoretic framework decomposes in-context learning error into meta-learning and in-context components, yielding concise bounds without mixing time assumptions."
---

# An Information-Theoretic Analysis of In-Context Learning

**Source**: [https://proceedings.mlr.press/v235/jeon24a.html](https://proceedings.mlr.press/v235/jeon24a.html)

**TLDR**: An information-theoretic framework decomposes in-context learning error into meta-learning and in-context components, yielding concise bounds without mixing time assumptions.

## Abstract

Previous theoretical results pertaining to meta-learning on sequences build on contrived and convoluted mixing time assumptions. We introduce new information-theoretic tools that lead to a concise yet general decomposition of error for a Bayes optimal predictor into two components: meta-learning error and intra-task error. These tools unify analyses across many meta-learning challenges. To illustrate, we apply them to establish new results about in-context learning with transformers and corroborate existing results a simple linear setting. Our theoretical results characterize how error decays in both the number of training sequences and sequence lengths. Our results are very general; for example, they avoid contrived mixing time assumptions made by all prior results that establish decay of error with sequence length.