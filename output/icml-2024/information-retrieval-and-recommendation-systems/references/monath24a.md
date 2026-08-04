---
title: "A Fresh Take on Stale Embeddings: Improving Dense Retriever Training with Corrector Networks"
source: "https://proceedings.mlr.press/v235/monath24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/monath24a/monath24a.pdf"
categories: ['information-retrieval-and-recommendation-systems', 'data-selection-and-active-learning-methods']
tags: ['dense-retrieval', 'stale-embeddings', 'corrector-networks']
venue: "ICML 2024"
tldr: "Improves dense retriever training by introducing corrector networks that compensate for stale embeddings during large-scale contrastive learning."
---

# A Fresh Take on Stale Embeddings: Improving Dense Retriever Training with Corrector Networks

**Source**: [https://proceedings.mlr.press/v235/monath24a.html](https://proceedings.mlr.press/v235/monath24a.html)

**TLDR**: Improves dense retriever training by introducing corrector networks that compensate for stale embeddings during large-scale contrastive learning.

## Abstract

In dense retrieval, deep encoders provide embeddings for both inputs and targets, and the softmax function is used to parameterize a distribution over a large number of candidate targets (e.g., textual passages for information retrieval). Significant challenges arise in training such encoders in the increasingly prevalent scenario of (1) a large number of targets, (2) a computationally expensive target encoder model, (3) cached target embeddings that are out-of-date due to ongoing training of target encoder parameters. This paper presents a simple and highly scalable response to these challenges by training a small parametric corrector network that adjusts stale cached target embeddings, enabling an accurate softmax approximation and thereby sampling of up-to-date high scoring "hard negatives." We theoretically investigate the generalization properties of our proposed target corrector, relating the complexity of the network, staleness of cached representations, and the amount of training data. We present experimental results on large benchmark dense retrieval datasets as well as on QA with retrieval augmented language models. Our approach matches state-of-the-art results even when no target embedding updates are made during training beyond an initial cache from the unsupervised pre-trained model, providing a 4-80x reduction in re-embedding computational cost.