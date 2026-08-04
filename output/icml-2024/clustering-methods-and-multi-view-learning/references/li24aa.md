---
title: "Image Clustering with External Guidance"
source: "https://proceedings.mlr.press/v235/li24aa.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24aa/li24aa.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'data-selection-and-active-learning-methods']
tags: ['image-clustering', 'external-guidance', 'supervision-signals', 'self-supervised-learning']
venue: "ICML 2024"
tldr: "An image clustering method leverages external guidance to construct better supervision signals beyond traditional self-supervision."
---

# Image Clustering with External Guidance

**Source**: [https://proceedings.mlr.press/v235/li24aa.html](https://proceedings.mlr.press/v235/li24aa.html)

**TLDR**: An image clustering method leverages external guidance to construct better supervision signals beyond traditional self-supervision.

## Abstract

The core of clustering lies in incorporating prior knowledge to construct supervision signals. From classic k-means based on data compactness to recent contrastive clustering guided by self-supervision, the evolution of clustering methods intrinsically corresponds to the progression of supervision signals. At present, substantial efforts have been devoted to mining internal supervision signals from data. Nevertheless, the abundant external knowledge such as semantic descriptions, which naturally conduces to clustering, is regrettably overlooked. In this work, we propose leveraging external knowledge as a new supervision signal to guide clustering. To implement and validate our idea, we design an externally guided clustering method (Text-Aided Clustering, TAC), which leverages the textual semantics of WordNet to facilitate image clustering. Specifically, TAC first selects and retrieves WordNet nouns that best distinguish images to enhance the feature discriminability. Then, TAC collaborates text and image modalities by mutually distilling cross-modal neighborhood information. Experiments demonstrate that TAC achieves state-of-the-art performance on five widely used and three more challenging image clustering benchmarks, including the full ImageNet-1K dataset. The code can be accessed at https://github.com/XLearning-SCU/2024-ICML-TAC.