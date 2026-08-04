---
title: "On the Embedding Collapse when Scaling up Recommendation Models"
source: "https://proceedings.mlr.press/v235/guo24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/guo24e/guo24e.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'transformer-architecture-efficiency-and-scaling']
tags: ['recommendation-systems', 'embedding-collapse', 'scaling', 'large-scale-models', 'representation-learning']
venue: "ICML 2024"
tldr: "Identifies embedding collapse as the key barrier to scaling recommendation models and proposes solutions to address it."
---

# On the Embedding Collapse when Scaling up Recommendation Models

**Source**: [https://proceedings.mlr.press/v235/guo24e.html](https://proceedings.mlr.press/v235/guo24e.html)

**TLDR**: Identifies embedding collapse as the key barrier to scaling recommendation models and proposes solutions to address it.

## Abstract

Recent advances in foundation models have led to a promising trend of developing large recommendation models to leverage vast amounts of available data. Still, mainstream models remain embarrassingly small in size and naive enlarging does not lead to sufficient performance gain, suggesting a deficiency in the model scalability. In this paper, we identify the embedding collapse phenomenon as the inhibition of scalability, wherein the embedding matrix tends to occupy a low-dimensional subspace. Through empirical and theoretical analysis, we demonstrate a two-sided effect of feature interaction specific to recommendation models. On the one hand, interacting with collapsed embeddings restricts embedding learning and exacerbates the collapse issue. On the other hand, interaction is crucial in mitigating the fitting of spurious features as a scalability guarantee. Based on our analysis, we propose a simple yet effective multi-embedding design incorporating embedding-set-specific interaction modules to learn embedding sets with large diversity and thus reduce collapse. Extensive experiments demonstrate that this proposed design provides consistent scalability and effective collapse mitigation for various recommendation models. Code is available at this repository: https://github.com/thuml/Multi-Embedding.