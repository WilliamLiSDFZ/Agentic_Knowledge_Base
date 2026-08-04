---
title: "Outlier-Efficient Hopfield Layers for Large Transformer-Based Models"
source: "https://proceedings.mlr.press/v235/hu24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/hu24a/hu24a.pdf"
categories: ['transformer-architecture-efficiency-and-scaling', 'sequence-models-for-memory-and-state']
tags: ['hopfield-networks', 'transformers', 'outlier', 'associative-memory', 'large-models']
venue: "ICML 2024"
tldr: "Introduces an outlier-efficient Modern Hopfield Model to address outlier-related inefficiencies in training large transformer-based architectures."
---

# Outlier-Efficient Hopfield Layers for Large Transformer-Based Models

**Source**: [https://proceedings.mlr.press/v235/hu24a.html](https://proceedings.mlr.press/v235/hu24a.html)

**TLDR**: Introduces an outlier-efficient Modern Hopfield Model to address outlier-related inefficiencies in training large transformer-based architectures.

## Abstract

We introduce an Outlier-Efficient Modern Hopfield Model (termed OutEffHop) and use it to address the outlier inefficiency problem of training gigantic transformer-based models. Our main contribution is a novel associative memory model facilitating outlier-efficient associative memory retrievals. Interestingly, this memory model manifests a model-based interpretation of an outlier-efficient attention mechanism (Softmax_1): it is an approximation of the memory retrieval process of OutEffHop. Methodologically, this allows us to introduce novel outlier-efficient Hopfield layers as powerful alternatives to traditional attention mechanisms, with superior post-quantization performance. Theoretically, the Outlier-Efficient Modern Hopfield Model retains and improves the desirable properties of standard modern Hopfield models, including fixed point convergence and exponential storage capacity. Empirically, we demonstrate the efficacy of the proposed model across large-scale transformer-based and Hopfield-based models (including BERT, OPT, ViT, and STanHop-Net), benchmarking against state-of-the-art methods like Clipped_Softmax and Gated_Attention. Notably, OutEffHop achieves an average reduction of 22+% in average kurtosis and 26+% in the maximum infinity norm of model outputs across four models. Code is available at GitHub; future updates are on arXiv.