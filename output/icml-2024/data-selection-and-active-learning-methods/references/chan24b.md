---
title: "Scribble-Supervised Semantic Segmentation with Prototype-based Feature Augmentation"
source: "https://proceedings.mlr.press/v235/chan24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chan24b/chan24b.pdf"
categories: ['learning-with-imperfect-data-and-bias', 'data-selection-and-active-learning-methods']
tags: ['semantic-segmentation', 'scribble-supervision', 'prototype-augmentation', 'weak-supervision']
venue: "ICML 2024"
tldr: "Proposes prototype-based feature augmentation to improve scribble-supervised semantic segmentation with minimal annotation cost."
---

# Scribble-Supervised Semantic Segmentation with Prototype-based Feature Augmentation

**Source**: [https://proceedings.mlr.press/v235/chan24b.html](https://proceedings.mlr.press/v235/chan24b.html)

**TLDR**: Proposes prototype-based feature augmentation to improve scribble-supervised semantic segmentation with minimal annotation cost.

## Abstract

Scribble-supervised semantic segmentation presents a cost-effective training method that utilizes annotations generated through scribbling. It is valued in attaining high performance while minimizing annotation costs, which has made it highly regarded among researchers. Scribble supervision propagates information from labeled pixels to the surrounding unlabeled pixels, enabling semantic segmentation for the entire image. However, existing methods often ignore the features of classified pixels during feature propagation. To address these limitations, this paper proposes a prototype-based feature augmentation method that leverages feature prototypes to augment scribble supervision. Experimental results demonstrate that our approach achieves state-of-the-art performance on the PASCAL VOC 2012 dataset in scribble-supervised semantic segmentation tasks. The code is available at https://github.com/TranquilChan/PFA.