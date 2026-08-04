---
title: "An amortized approach to non-linear mixed-effects modeling based on neural posterior estimation"
source: "https://proceedings.mlr.press/v235/arruda24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/arruda24a/arruda24a.pdf"
categories: ['generative-models-and-variational-inference', 'amortized-hybrid-dynamical-system-discovery']
tags: ['mixed-effects-models', 'neural-posterior-estimation', 'amortized-inference', 'heterogeneous-populations']
venue: "ICML 2024"
tldr: "Presents an amortized neural posterior estimation approach for efficient inference in non-linear mixed-effects models."
---

# An amortized approach to non-linear mixed-effects modeling based on neural posterior estimation

**Source**: [https://proceedings.mlr.press/v235/arruda24a.html](https://proceedings.mlr.press/v235/arruda24a.html)

**TLDR**: Presents an amortized neural posterior estimation approach for efficient inference in non-linear mixed-effects models.

## Abstract

Non-linear mixed-effects models are a powerful tool for studying heterogeneous populations in various fields, including biology, medicine, economics, and engineering. Here, the aim is to find a distribution over the parameters that describe the whole population using a model that can generate simulations for an individual of that population. However, fitting these distributions to data is computationally challenging if the description of individuals is complex and the population is large. To address this issue, we propose a novel machine learning-based approach: We exploit neural density estimation based on conditional normalizing flows to approximate individual-specific posterior distributions in an amortized fashion, thereby allowing for efficient inference of population parameters. Applying this approach to problems from cell biology and pharmacology, we demonstrate its unseen flexibility and scalability to large data sets compared to established methods.