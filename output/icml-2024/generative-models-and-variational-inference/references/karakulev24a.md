---
title: "Adaptive Robust Learning using Latent Bernoulli Variables"
source: "https://proceedings.mlr.press/v235/karakulev24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/karakulev24a/karakulev24a.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'generative-models-and-variational-inference']
tags: ['robust-learning', 'corrupted-data', 'latent-variables', 'Bernoulli', 'EM']
venue: "ICML 2024"
tldr: "Presents an adaptive robust learning approach using latent Bernoulli variables to identify and down-weight corrupted training samples."
---

# Adaptive Robust Learning using Latent Bernoulli Variables

**Source**: [https://proceedings.mlr.press/v235/karakulev24a.html](https://proceedings.mlr.press/v235/karakulev24a.html)

**TLDR**: Presents an adaptive robust learning approach using latent Bernoulli variables to identify and down-weight corrupted training samples.

## Abstract

We present an adaptive approach for robust learning from corrupted training sets. We identify corrupted and non-corrupted samples with latent Bernoulli variables and thus formulate the learning problem as maximization of the likelihood where latent variables are marginalized. The resulting problem is solved via variational inference, using an efficient Expectation-Maximization based method. The proposed approach improves over the state-of-the-art by automatically inferring the corruption level, while adding minimal computational overhead. We demonstrate our robust learning method and its parameter-free nature on a wide variety of machine learning tasks including online learning and deep learning where it adapts to different levels of noise and maintains high prediction accuracy.