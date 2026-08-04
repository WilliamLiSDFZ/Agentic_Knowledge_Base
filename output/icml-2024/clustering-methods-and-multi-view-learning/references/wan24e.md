---
title: "Decouple then Classify: A Dynamic Multi-view Labeling Strategy with Shared and Specific Information"
source: "https://proceedings.mlr.press/v235/wan24e.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wan24e/wan24e.pdf"
categories: ['data-selection-and-active-learning-methods', 'clustering-methods-and-multi-view-learning']
tags: ['semi-supervised-learning', 'multi-view-learning', 'active-labeling', 'shared-specific-information', 'dynamic-strategy']
venue: "ICML 2024"
tldr: "A dynamic multi-view labeling strategy that decouples shared and specific information to improve sample selection for semi-supervised learning."
---

# Decouple then Classify: A Dynamic Multi-view Labeling Strategy with Shared and Specific Information

**Source**: [https://proceedings.mlr.press/v235/wan24e.html](https://proceedings.mlr.press/v235/wan24e.html)

**TLDR**: A dynamic multi-view labeling strategy that decouples shared and specific information to improve sample selection for semi-supervised learning.

## Abstract

Sample labeling is the most primary and fundamental step of semi-supervised learning. In literature, most existing methods randomly label samples with a given ratio, but achieve unpromising and unstable results due to the randomness, especially in multi-view settings. To address this issue, we propose a Dynamic Multi-view Labeling Strategy with Shared and Specific Information. To be brief, by building two classifiers with existing labels to utilize decoupled shared and specific information, we select the samples of low classification confidence and label them in high priorities. The newly generated labels are also integrated to update the classifiers adaptively. The two processes are executed alternatively until a satisfying classification performance. To validate the effectiveness of the proposed method, we conduct extensive experiments on popular benchmarks, achieving promising performance. The code is publicly available at https://github.com/wanxinhang/ICML2024_decouple_then_classify.