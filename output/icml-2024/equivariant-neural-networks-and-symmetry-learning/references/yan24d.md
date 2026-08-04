---
title: "A Space Group Symmetry Informed Network for O(3) Equivariant Crystal Tensor Prediction"
source: "https://proceedings.mlr.press/v235/yan24d.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yan24d/yan24d.pdf"
categories: ['equivariant-neural-networks-and-symmetry-learning', 'algebraic-structures-in-machine-learning']
tags: ['crystal-property-prediction', 'space-group-symmetry', 'equivariant-networks']
venue: "ICML 2024"
tldr: "Proposes a symmetry-informed equivariant network for predicting tensor properties of crystalline materials respecting both O(3) and space group symmetries."
---

# A Space Group Symmetry Informed Network for O(3) Equivariant Crystal Tensor Prediction

**Source**: [https://proceedings.mlr.press/v235/yan24d.html](https://proceedings.mlr.press/v235/yan24d.html)

**TLDR**: Proposes a symmetry-informed equivariant network for predicting tensor properties of crystalline materials respecting both O(3) and space group symmetries.

## Abstract

We consider the prediction of general tensor properties of crystalline materials, including dielectric, piezoelectric, and elastic tensors. A key challenge here is how to make the predictions satisfy the unique tensor equivariance to both O(3) and crystal space groups. To this end, we propose a General Materials Tensor Network (GMTNet), which is carefully designed to satisfy the required symmetries. To evaluate our method, we curate a dataset and establish evaluation metrics that are tailored to the intricacies of crystal tensor predictions. Experimental results show that our GMTNet not only achieves promising performance on crystal tensors of various orders but also generates predictions fully consistent with the intrinsic crystal symmetries. Our code is publicly available as part of the AIRS library (https://github.com/divelab/AIRS).