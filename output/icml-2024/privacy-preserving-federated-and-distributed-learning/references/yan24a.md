---
title: "Balancing Similarity and Complementarity for Federated Learning"
source: "https://proceedings.mlr.press/v235/yan24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yan24a/yan24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'clustering-methods-and-multi-view-learning']
tags: ['federated-learning', 'data-heterogeneity', 'client-selection']
venue: "ICML 2024"
tldr: "Proposes a client collaboration strategy in federated learning that balances similarity and complementarity to handle statistical heterogeneity."
---

# Balancing Similarity and Complementarity for Federated Learning

**Source**: [https://proceedings.mlr.press/v235/yan24a.html](https://proceedings.mlr.press/v235/yan24a.html)

**TLDR**: Proposes a client collaboration strategy in federated learning that balances similarity and complementarity to handle statistical heterogeneity.

## Abstract

In mobile and IoT systems, Federated Learning (FL) is increasingly important for effectively using data while maintaining user privacy. One key challenge in FL is managing statistical heterogeneity, such as non-i.i.d. data, arising from numerous clients and diverse data sources. This requires strategic cooperation, often with clients having similar characteristics. However, we are interested in a fundamental question: does achieving optimal cooperation necessarily entail cooperating with the most similar clients? Typically, significant model performance improvements are often realized not by partnering with the most similar models, but through leveraging complementary data. Our theoretical and empirical analyses suggest that optimal cooperation is achieved by enhancing complementarity in feature distribution while restricting the disparity in the correlation between features and targets. Accordingly, we introduce a novel framework, FedSaC, which balances similarity and complementarity in FL cooperation. Our framework aims to approximate an optimal cooperation network for each client by optimizing a weighted sum of model similarity and feature complementarity. The strength of FedSaC lies in its adaptability to various levels of data heterogeneity and multimodal scenarios. Our comprehensive unimodal and multimodal experiments demonstrate that FedSaC markedly surpasses other state-of-the-art FL methods.