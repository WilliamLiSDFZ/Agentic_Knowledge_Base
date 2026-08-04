---
title: "Differentially Private Sum-Product Networks"
source: "https://proceedings.mlr.press/v235/heilmann24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/heilmann24a/heilmann24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'probabilistic-generating-circuits-research']
tags: ['differential-privacy', 'sum-product-networks', 'probabilistic-circuits']
venue: "ICML 2024"
tldr: "Introduces differentially private sum-product networks that allow repeated model releases without accumulating additional privacy costs."
---

# Differentially Private Sum-Product Networks

**Source**: [https://proceedings.mlr.press/v235/heilmann24a.html](https://proceedings.mlr.press/v235/heilmann24a.html)

**TLDR**: Introduces differentially private sum-product networks that allow repeated model releases without accumulating additional privacy costs.

## Abstract

Differentially private ML approaches seek to learn models which may be publicly released while guaranteeing that the input data is kept private. One issue with this construction is that further model releases based on the same training data (e.g. for a new task) incur a further privacy budget cost. Privacy-preserving synthetic data generation is one possible solution to this conundrum. However, models trained on synthetic private data struggle to approach the performance of private, ad-hoc models. In this paper, we present a novel method based on sum-product networks that is able to perform both privacy-preserving classification and privacy-preserving data generation with a single model. To the best of our knowledge, ours is the first approach that provides both discriminative and generative capabilities to differentially private ML. We show that our approach outperforms the state of the art in terms of stability (i.e. number of training runs required for convergence) and utility of the generated data.