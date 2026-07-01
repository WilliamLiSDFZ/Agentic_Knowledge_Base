---
title: "SSA-Seg: Semantic and Spatial Adaptive Pixel-level Classifier for Semantic Segmentation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/aa5a581a221f1e431fcad9d7ccfedaa2-Abstract-Conference.html"
categories: ['transformer-based-learning-for-spatial-tasks']
tags: ['semantic-segmentation', 'adaptive-classifier', 'prototype-deviation']
venue: "NeurIPS 2024"
tldr: "A semantic and spatial adaptive pixel-level classifier is proposed to overcome fixed prototype limitations in semantic segmentation."
---

# SSA-Seg: Semantic and Spatial Adaptive Pixel-level Classifier for Semantic Segmentation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/aa5a581a221f1e431fcad9d7ccfedaa2-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/aa5a581a221f1e431fcad9d7ccfedaa2-Abstract-Conference.html)

**TLDR**: A semantic and spatial adaptive pixel-level classifier is proposed to overcome fixed prototype limitations in semantic segmentation.

## Abstract

Vanilla pixel-level classifiers for semantic segmentation are based on a certain paradigm, involving the inner product of fixed prototypes obtained from the training set and pixel features in the test image.  This approach, however, encounters significant limitations, i.e., feature deviation in the semantic domain and information loss in the spatial domain. The former struggles with large intra-class variance among pixel features from different images, while the latter fails to utilize the structured information of semantic objects effectively.  This leads to blurred mask boundaries as well as a deficiency of fine-grained recognition capability.  In this paper, we propose a novel Semantic and Spatial Adaptive Classifier (SSA-Seg) to address the above challenges.  Specifically, we employ the coarse masks obtained from the fixed prototypes as a guide to adjust the fixed prototype towards the center of the semantic and spatial domains in the test image.  The adapted prototypes in semantic and spatial domains are then simultaneously considered to accomplish classification decisions.  In addition, we propose an online multi-domain distillation learning strategy to improve the adaption process.  Experimental results on three publicly available benchmarks show that the proposed SSA-Seg significantly improves the segmentation performance of the baseline models with only a minimal increase in computational cost.