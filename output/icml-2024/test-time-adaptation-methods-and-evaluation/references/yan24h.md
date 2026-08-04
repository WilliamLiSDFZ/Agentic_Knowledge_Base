---
title: "Retrieval Across Any Domains via Large-scale Pre-trained Model"
source: "https://proceedings.mlr.press/v235/yan24h.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yan24h/yan24h.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'test-time-adaptation-methods-and-evaluation']
tags: ['cross-domain-retrieval', 'data-free-adaptation', 'pretrained-models']
venue: "ICML 2024"
tldr: "Introduces a data-free adaptive cross-domain image retrieval approach leveraging large-scale pretrained models for generalization to unseen domains."
---

# Retrieval Across Any Domains via Large-scale Pre-trained Model

**Source**: [https://proceedings.mlr.press/v235/yan24h.html](https://proceedings.mlr.press/v235/yan24h.html)

**TLDR**: Introduces a data-free adaptive cross-domain image retrieval approach leveraging large-scale pretrained models for generalization to unseen domains.

## Abstract

In order to enhance the generalization ability towards unseen domains, universal cross-domain image retrieval methods require a training dataset encompassing diverse domains, which is costly to assemble. Given this constraint, we introduce a novel problem of data-free adaptive cross-domain retrieval, eliminating the need for real images during training. Towards this goal, we propose a novel Text-driven Knowledge Integration (TKI) method, which exclusively utilizes a pre-trained vision-language model to implement an “aggregation after expansion" training strategy. Specifically, we extract diverse implicit domain-specific information through a set of learnable domain word vectors. Subsequently, a domain-agnostic universal projection, equipped with a non-Euclidean multi-layer perceptron, can be optimized using these assorted text descriptions through the text-proxied domain aggregation. Leveraging the cross-modal transferability phenomenon of the shared latent space, we can integrate the trained domain-agnostic universal projection with the pre-trained visual encoder to extract the features of the input image for the following retrieval during testing. Extensive experimental results on several benchmark datasets demonstrate the superiority of our method.