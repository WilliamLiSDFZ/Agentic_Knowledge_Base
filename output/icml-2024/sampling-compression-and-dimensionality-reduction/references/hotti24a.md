---
title: "Efficient Mixture Learning in Black-Box Variational Inference"
source: "https://proceedings.mlr.press/v235/hotti24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hotti24a/hotti24a.pdf"
categories: ['generative-models-and-variational-inference', 'sampling-compression-and-dimensionality-reduction']
tags: ['variational-inference', 'mixture-models', 'bbvi', 'scalable-inference', 'density-estimation']
venue: "ICML 2024"
tldr: "Introduces an efficient mixture learning approach for black-box variational inference that avoids quadratic scaling costs with the number of mixture components."
---

# Efficient Mixture Learning in Black-Box Variational Inference

**Source**: [https://proceedings.mlr.press/v235/hotti24a.html](https://proceedings.mlr.press/v235/hotti24a.html)

**TLDR**: Introduces an efficient mixture learning approach for black-box variational inference that avoids quadratic scaling costs with the number of mixture components.

## Abstract

Mixture variational distributions in black box variational inference (BBVI) have demonstrated impressive results in challenging density estimation tasks. However, currently scaling the number of mixture components can lead to a linear increase in the number of learnable parameters and a quadratic increase in inference time due to the evaluation of the evidence lower bound (ELBO). Our two key contributions address these limitations. First, we introduce the novel Multiple Importance Sampling Variational Autoencoder (MISVAE), which amortizes the mapping from input to mixture-parameter space using one-hot encodings. Fortunately, with MISVAE, each additional mixture component incurs a negligible increase in network parameters. Second, we construct two new estimators of the ELBO for mixtures in BBVI, enabling a tremendous reduction in inference time with marginal or even improved impact on performance. Collectively, our contributions enable scalability to hundreds of mixture components and provide superior estimation performance in shorter time, with fewer network parameters compared to previous Mixture VAEs. Experimenting with MISVAE, we achieve astonishing, SOTA results on MNIST. Furthermore, we empirically validate our estimators in other BBVI settings, including Bayesian phylogenetic inference, where we improve inference times for the SOTA mixture model on eight data sets.