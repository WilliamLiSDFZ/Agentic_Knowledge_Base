---
title: "Stochastic positional embeddings improve masked image modeling"
source: "https://proceedings.mlr.press/v235/bar24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/bar24a/bar24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'generative-models-and-variational-inference']
tags: ['masked-image-modeling', 'stochastic-positional-embeddings', 'self-supervised-learning']
venue: "ICML 2024"
tldr: "Stochastic positional embeddings are proposed to improve masked image modeling by better capturing semantic content and location."
---

# Stochastic positional embeddings improve masked image modeling

**Source**: [https://proceedings.mlr.press/v235/bar24a.html](https://proceedings.mlr.press/v235/bar24a.html)

**TLDR**: Stochastic positional embeddings are proposed to improve masked image modeling by better capturing semantic content and location.

## Abstract

Masked Image Modeling (MIM) is a promising self-supervised learning approach that enables learning from unlabeled images. Despite its recent success, learning good representations through MIM remains challenging because it requires predicting the right semantic content in accurate locations. For example, given an incomplete picture of a dog, we can guess that there is a tail, but we cannot determine its exact location. In this work, we propose to incorporate location uncertainty to MIM by using stochastic positional embeddings (StoP). Specifically, we condition the model on stochastic masked token positions drawn from a gaussian distribution. We show that using StoP reduces overfitting to location features and guides the model toward learning features that are more robust to location uncertainties. Quantitatively, using StoP improves downstream MIM performance on a variety of downstream tasks. For example, linear probing on ImageNet using ViT-B is improved by $+1.7%$, and by $2.5%$ for ViT-H using 1% of the data.