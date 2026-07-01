---
title: "EAGLE: Efficient Adaptive Geometry-based Learning in Cross-view Understanding"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/f84ceafb242f0de36f8c49452fbae6de-Abstract-Conference.html"
categories: ['visual-language-multimodal-generation-reasoning', 'transformer-based-learning-for-spatial-tasks']
tags: ['unsupervised-domain-adaptation', 'semantic-segmentation', 'open-vocabulary', 'vision-language', 'cross-view']
venue: "NeurIPS 2024"
tldr: "EAGLE combines unsupervised domain adaptation with open-vocabulary vision-language models for efficient cross-view semantic scene understanding."
---

# EAGLE: Efficient Adaptive Geometry-based Learning in Cross-view Understanding

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/f84ceafb242f0de36f8c49452fbae6de-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/f84ceafb242f0de36f8c49452fbae6de-Abstract-Conference.html)

**TLDR**: EAGLE combines unsupervised domain adaptation with open-vocabulary vision-language models for efficient cross-view semantic scene understanding.

## Abstract

Unsupervised Domain Adaptation has been an efficient approach to transferring the semantic segmentation model across data distributions. Meanwhile, the recent Open-vocabulary Semantic Scene understanding based on large-scale vision language models is effective in open-set settings because it can learn diverse concepts and categories. However, these prior methods fail to generalize across different camera views due to the lack of cross-view geometric modeling. At present, there are limited studies analyzing cross-view learning. To address this problem, we introduce a novel Unsupervised Cross-view Adaptation Learning approach to modeling the geometric structural change across views in Semantic Scene Understanding. First, we introduce a novel Cross-view Geometric Constraint on Unpaired Data to model structural changes in images and segmentation masks across cameras. Second, we present a new Geodesic Flow-based Correlation Metric to efficiently measure the geometric structural changes across camera views. Third, we introduce a novel view-condition prompting mechanism to enhance the view-information modeling of the open-vocabulary segmentation network in cross-view adaptation learning. The experiments on different cross-view adaptation benchmarks have shown the effectiveness of our approach in cross-view modeling, demonstrating that we achieve State-of-the-Art (SOTA) performance compared to prior unsupervised domain adaptation and open-vocabulary semantic segmentation methods.