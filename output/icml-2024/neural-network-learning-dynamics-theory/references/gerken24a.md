---
title: "Emergent Equivariance in Deep Ensembles"
source: "https://proceedings.mlr.press/v235/gerken24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/gerken24a/gerken24a.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'neural-network-learning-dynamics-theory']
tags: ['deep-ensembles', 'equivariance', 'data-augmentation']
venue: "ICML 2024"
tldr: "Shows that deep ensembles become emergently equivariant under data augmentation in the infinite-width limit."
---

# Emergent Equivariance in Deep Ensembles

**Source**: [https://proceedings.mlr.press/v235/gerken24a.html](https://proceedings.mlr.press/v235/gerken24a.html)

**TLDR**: Shows that deep ensembles become emergently equivariant under data augmentation in the infinite-width limit.

## Abstract

We show that deep ensembles become equivariant for all inputs and at all training times by simply using data augmentation. Crucially, equivariance holds off-manifold and for any architecture in the infinite width limit. The equivariance is emergent in the sense that predictions of individual ensemble members are not equivariant but their collective prediction is. Neural tangent kernel theory is used to derive this result and we verify our theoretical insights using detailed numerical experiments.