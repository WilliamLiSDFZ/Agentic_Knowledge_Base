---
title: "Estimating Unknown Population Sizes Using the Hypergeometric Distribution"
source: "https://proceedings.mlr.press/v235/hodgson24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hodgson24a/hodgson24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification', 'sampling-compression-and-dimensionality-reduction']
tags: ['hypergeometric-distribution', 'population-estimation', 'discrete-distributions']
venue: "ICML 2024"
tldr: "Addresses estimation of discrete distributions when both population size and category counts are unknown using the hypergeometric distribution."
---

# Estimating Unknown Population Sizes Using the Hypergeometric Distribution

**Source**: [https://proceedings.mlr.press/v235/hodgson24a.html](https://proceedings.mlr.press/v235/hodgson24a.html)

**TLDR**: Addresses estimation of discrete distributions when both population size and category counts are unknown using the hypergeometric distribution.

## Abstract

The multivariate hypergeometric distribution describes sampling without replacement from a discrete population of elements divided into multiple categories. Addressing a gap in the literature, we tackle the challenge of estimating discrete distributions when both the total population size and the category sizes are unknown. Here, we propose a novel solution using the hypergeometric likelihood to solve this estimation problem, even in the presence of severe under-sampling. Our approach accounts for a data generating process where the ground-truth is a mixture of distributions conditional on a continuous latent variable, as seen in collaborative filtering, using the variational autoencoder framework. Empirical data simulation demonstrates that our method outperforms other likelihood functions used to model count data, both in terms of accuracy of population size estimate and learning an informative latent space. We showcase our method’s versatility through applications in NLP, by inferring and estimating the complexity of latent vocabularies in reading passage excerpts, and in biology, by accurately recovering the true number of gene transcripts from sparse single-cell genomics data.