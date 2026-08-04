---
title: "Improved Modelling of Federated Datasets using Mixtures-of-Dirichlet-Multinomials"
source: "https://proceedings.mlr.press/v235/scott24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/scott24a/scott24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'clustering-methods-and-multi-view-learning']
tags: ['federated-learning', 'Dirichlet-multinomial', 'data-heterogeneity', 'proxy-data', 'mixture-models']
venue: "ICML 2024"
tldr: "Mixtures-of-Dirichlet-Multinomials better model federated dataset heterogeneity, improving server-side proxy data usage to accelerate federated learning."
---

# Improved Modelling of Federated Datasets using Mixtures-of-Dirichlet-Multinomials

**Source**: [https://proceedings.mlr.press/v235/scott24a.html](https://proceedings.mlr.press/v235/scott24a.html)

**TLDR**: Mixtures-of-Dirichlet-Multinomials better model federated dataset heterogeneity, improving server-side proxy data usage to accelerate federated learning.

## Abstract

In practice, training using federated learning can be orders of magnitude slower than standard centralized training. This severely limits the amount of experimentation and tuning that can be done, making it challenging to obtain good performance on a given task. Server-side proxy data can be used to run training simulations, for instance for hyperparameter tuning. This can greatly speed up the training pipeline by reducing the number of tuning runs to be performed overall on the true clients. However, it is challenging to ensure that these simulations accurately reflect the dynamics of the real federated training. In particular, the proxy data used for simulations often comes as a single centralized dataset without a partition into distinct clients, and partitioning this data in a naive way can lead to simulations that poorly reflect real federated training. In this paper we address the challenge of how to partition centralized data in a way that reflects the statistical heterogeneity of the true federated clients. We propose a fully federated, theoretically justified, algorithm that efficiently learns the distribution of the true clients and observe improved server-side simulations when using the inferred distribution to create simulated clients from the centralized data.