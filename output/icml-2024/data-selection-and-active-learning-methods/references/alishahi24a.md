---
title: "No Dimensional Sampling Coresets for Classification"
source: "https://proceedings.mlr.press/v235/alishahi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/alishahi24a/alishahi24a.pdf"
categories: ['sampling-compression-and-dimensionality-reduction', 'data-selection-and-active-learning-methods']
tags: ['coresets', 'classification', 'sensitivity-sampling']
venue: "ICML 2024"
tldr: "This paper refines and generalizes coreset constructions for classification problems using sensitivity sampling with improved dimension-independent bounds."
---

# No Dimensional Sampling Coresets for Classification

**Source**: [https://proceedings.mlr.press/v235/alishahi24a.html](https://proceedings.mlr.press/v235/alishahi24a.html)

**TLDR**: This paper refines and generalizes coreset constructions for classification problems using sensitivity sampling with improved dimension-independent bounds.

## Abstract

We refine and generalize what is known about coresets for classification problems via the sensitivity sampling framework. Such coresets seek the smallest possible subsets of input data, so one can optimize a loss function on the coreset and ensure approximation guarantees with respect to the original data. Our analysis provides the first no dimensional coresets, so the size does not depend on the dimension. Moreover, our results are general, apply for distributional input and can use iid samples, so provide sample complexity bounds, and work for a variety of loss functions. A key tool we develop is a Radamacher complexity version of the main sensitivity sampling approach, which can be of independent interest.