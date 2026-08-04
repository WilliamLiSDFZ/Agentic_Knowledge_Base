---
title: "Bidirectional Reciprocative Information Communication for Few-Shot Semantic Segmentation"
source: "https://proceedings.mlr.press/v235/liu24t.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24t/liu24t.pdf"
categories: ['clustering-methods-and-multi-view-learning']
tags: ['few-shot-segmentation', 'bidirectional-communication', 'semantic-segmentation']
venue: "ICML 2024"
tldr: "A bidirectional query-support communication mechanism is proposed for few-shot semantic segmentation to handle intra-class diversity."
---

# Bidirectional Reciprocative Information Communication for Few-Shot Semantic Segmentation

**Source**: [https://proceedings.mlr.press/v235/liu24t.html](https://proceedings.mlr.press/v235/liu24t.html)

**TLDR**: A bidirectional query-support communication mechanism is proposed for few-shot semantic segmentation to handle intra-class diversity.

## Abstract

Existing few-shot semantic segmentation methods typically rely on a one-way flow of category information from support to query, ignoring the impact of intra-class diversity. To address this, drawing inspiration from cybernetics, we introduce a Query Feedback Branch (QFB) to propagate query information back to support, generating a query-related support prototype that is more aligned with the query. Subsequently, a Query Amplifier Branch (QAB) is employed to amplify target objects in the query using the acquired support prototype. To further improve the model, we propose a Query Rectification Module (QRM), which utilizes the prediction disparity in the query before and after support activation to identify challenging positive and negative samples from ambiguous regions for query self-rectification. Furthermore, we integrate the QFB, QAB, and QRM into a feedback and rectification layer and incorporate it into an iterative pipeline. This configuration enables the progressive enhancement of bidirectional reciprocative flow of category information between query and support, effectively providing query-adaptive support information and addressing the intra-class diversity problem. Extensive experiments conducted on both PASCAL-5i and COCO-20i datasets validate the effectiveness of our approach. The code is available at https://github.com/LIUYUANWEI98/IFRNet .