---
title: "Mapping the Multiverse of Latent Representations"
source: "https://proceedings.mlr.press/v235/wayland24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wayland24a/wayland24a.pdf"
categories: ['statistical-learning-robustness-uncertainty-quantification']
tags: ['multiverse-analysis', 'latent-representations', 'robustness']
venue: "ICML 2024"
tldr: "PRESTO is a framework for systematically mapping the multiverse of ML models built on latent representations to assess their reliability and variability."
---

# Mapping the Multiverse of Latent Representations

**Source**: [https://proceedings.mlr.press/v235/wayland24a.html](https://proceedings.mlr.press/v235/wayland24a.html)

**TLDR**: PRESTO is a framework for systematically mapping the multiverse of ML models built on latent representations to assess their reliability and variability.

## Abstract

Echoing recent calls to counter reliability and robustness concerns in machine learning via multiverse analysis, we present PRESTO, a principled framework for mapping the multiverse of machine-learning models that rely on latent representations. Although such models enjoy widespread adoption, the variability in their embeddings remains poorly understood, resulting in unnecessary complexity and untrustworthy representations. Our framework uses persistent homology to characterize the latent spaces arising from different combinations of diverse machine-learning methods, (hyper)parameter configurations, and datasets, allowing us to measure their pairwise (dis)similarity and statistically reason about their distributions. As we demonstrate both theoretically and empirically, our pipeline preserves desirable properties of collections of latent representations, and it can be leveraged to perform sensitivity analysis, detect anomalous embeddings, or efficiently and effectively navigate hyperparameter search spaces.