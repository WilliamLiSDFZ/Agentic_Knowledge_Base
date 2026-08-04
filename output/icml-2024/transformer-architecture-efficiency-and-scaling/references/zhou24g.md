---
title: "MultiMax: Sparse and Multi-Modal Attention Learning"
source: "https://proceedings.mlr.press/v235/zhou24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/zhou24g/zhou24g.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'sampling-compression-and-dimensionality-reduction']
tags: ['sparse-attention', 'multi-modal-attention', 'softmax-alternatives']
venue: "ICML 2024"
tldr: "Introduces MultiMax, a sparse and multi-modal attention mechanism that goes beyond SoftMax by concentrating probability mass more selectively across input entries."
---

# MultiMax: Sparse and Multi-Modal Attention Learning

**Source**: [https://proceedings.mlr.press/v235/zhou24g.html](https://proceedings.mlr.press/v235/zhou24g.html)

**TLDR**: Introduces MultiMax, a sparse and multi-modal attention mechanism that goes beyond SoftMax by concentrating probability mass more selectively across input entries.

## Abstract

SoftMax is a ubiquitous ingredient of modern machine learning algorithms. It maps an input vector onto a probability simplex and reweights the input by concentrating the probability mass at large entries. Yet, as a smooth approximation to the Argmax function, a significant amount of probability mass is distributed to other, residual entries, leading to poor interpretability and noise. Although sparsity can be achieved by a family of SoftMax variants, they often require an alternative loss function and do not preserve multimodality. We show that this trade-off between multi-modality and sparsity limits the expressivity of SoftMax as well as its variants. We provide a solution to this tension between objectives by proposing a piece-wise differentiable function, termed MultiMax, which adaptively modulates the output distribution according to input entry range. Through comprehensive analysis and evaluation, we show that MultiMax successfully produces a distribution that supresses irrelevant entries while preserving multi-modality, with benefits in image classification, language modeling and machine translation.