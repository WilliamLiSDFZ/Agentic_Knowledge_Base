---
title: "Learning High-Order Relationships of Brain Regions"
source: "https://proceedings.mlr.press/v235/qiu24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/qiu24b/qiu24b.pdf"
categories: ['multi-region-brain-connectivity-modeling', 'graph-neural-networks-and-topology']
tags: ['brain-regions', 'fMRI', 'high-order-relationships', 'hypergraph', 'neuroscience', 'phenotypic-prediction']
venue: "ICML 2024"
tldr: "A method to capture high-order relationships among brain regions from fMRI data beyond pairwise interactions."
---

# Learning High-Order Relationships of Brain Regions

**Source**: [https://proceedings.mlr.press/v235/qiu24b.html](https://proceedings.mlr.press/v235/qiu24b.html)

**TLDR**: A method to capture high-order relationships among brain regions from fMRI data beyond pairwise interactions.

## Abstract

Discovering reliable and informative relationships among brain regions from functional magnetic resonance imaging (fMRI) signals is essential in phenotypic predictions in neuroscience. Most of the current methods fail to accurately characterize those interactions because they only focus on pairwise connections and overlook the high-order relationships of brain regions. We propose that these high-order relationships should be maximally informative and minimally redundant (MIMR). However, identifying such high-order relationships is challenging and under-explored due to the exponential search space and the absence of a tractable objective. In response to this gap, we propose a novel method named HyBRiD, which aims to extract MIMR high-order relationships from fMRI data. HyBRiD employs a Constructor to identify hyperedge structures, and a Weighter to compute a weight for each hyperedge, which avoids searching in exponential space. HyBRiD achieves the MIMR objective through an innovative information bottleneck framework named multi-head drop-bottleneck with theoretical guarantees. Our comprehensive experiments demonstrate the effectiveness of our model. Our model outperforms the state-of-the-art predictive model by an average of 11.2%, regarding the quality of hyperedges measured by CPM, a standard protocol for studying brain connections.