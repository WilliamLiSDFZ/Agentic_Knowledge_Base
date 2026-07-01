---
title: "Robust Contrastive Multi-view Clustering against Dual Noisy Correspondence"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/dbe81b08f7dc4dd8b43bc62dedfd9662-Abstract-Conference.html"
categories: ['multi-view-clustering-and-3d-perception', 'fairness-aware-machine-learning-methods']
tags: ['multi-view-clustering', 'contrastive-learning', 'noisy-correspondence']
venue: "NeurIPS 2024"
tldr: "A robust contrastive multi-view clustering method that handles dual noisy correspondences in both instance and pseudo-label spaces."
---

# Robust Contrastive Multi-view Clustering against Dual Noisy Correspondence

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/dbe81b08f7dc4dd8b43bc62dedfd9662-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/dbe81b08f7dc4dd8b43bc62dedfd9662-Abstract-Conference.html)

**TLDR**: A robust contrastive multi-view clustering method that handles dual noisy correspondences in both instance and pseudo-label spaces.

## Abstract

Recently, contrastive multi-view clustering (MvC) has emerged as a promising avenue for analyzing data from heterogeneous sources, typically leveraging the off-the-shelf instances as positives and randomly sampled ones as negatives. In practice, however, this paradigm would unavoidably suffer from the Dual Noisy Correspondence (DNC) problem, where noise compromises the constructions of both positive and negative pairs.Specifically, the complexity of data collection and transmission might mistake some unassociated pairs as positive (namely, false positive correspondence), while the intrinsic one-to-many contrast nature of contrastive MvC would sample some intra-cluster samples as negative (namely, false negative correspondence).To handle this daunting problem, we propose a novel method, dubbed Contextually-spectral based correspondence refinery (CANDY). CANDY dexterously exploits inter-view similarities as \textit{context} to uncover false negatives. Furthermore, it employs a spectral-based module to denoise correspondence, alleviating the negative influence of false positives. Extensive experiments on five widely-used multi-view benchmarks, in comparison with eight competitive multi-view clustering methods, verify the effectiveness of our method in addressing the DNC problem.The code is available at https://github.com/XLearning-SCU/2024-NeurIPS-CANDY.