---
title: "Overcoming Data and Model heterogeneities in Decentralized Federated Learning via Synthetic Anchors"
source: "https://proceedings.mlr.press/v235/huang24v.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/huang24v/huang24v.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'clustering-methods-and-multi-view-learning']
tags: ['federated-learning', 'decentralized', 'heterogeneity', 'synthetic-anchors', 'model-aggregation']
venue: "ICML 2024"
tldr: "Proposes synthetic anchor data to bridge data and model heterogeneities in decentralized federated learning without a central server."
---

# Overcoming Data and Model heterogeneities in Decentralized Federated Learning via Synthetic Anchors

**Source**: [https://proceedings.mlr.press/v235/huang24v.html](https://proceedings.mlr.press/v235/huang24v.html)

**TLDR**: Proposes synthetic anchor data to bridge data and model heterogeneities in decentralized federated learning without a central server.

## Abstract

Conventional Federated Learning (FL) involves collaborative training of a global model while maintaining user data privacy. One of its branches, decentralized FL, is a serverless network that allows clients to own and optimize different local models separately, which results in saving management and communication resources. Despite the promising advancements in decentralized FL, it may reduce model generalizability due to lacking a global model. In this scenario, managing data and model heterogeneity among clients becomes a crucial problem, which poses a unique challenge that must be overcome: How can every client’s local model learn generalizable representation in a decentralized manner? To address this challenge, we propose a novel Decentralized FL technique by introducing Synthetic Anchors, dubbed as DeSA. Based on the theory of domain adaptation and Knowledge Distillation (KD), we theoretically and empirically show that synthesizing global anchors based on raw data distribution facilitates mutual knowledge transfer. We further design two effective regularization terms for local training: 1) REG loss that regularizes the distribution of the client’s latent embedding with the anchors and 2) KD loss that enables clients to learn from others. Through extensive experiments on diverse client data distributions, we showcase the effectiveness of DeSA in enhancing both inter- and intra-domain accuracy of each client. The implementation of DeSA can be found at: https://github.com/ubc-tea/DESA