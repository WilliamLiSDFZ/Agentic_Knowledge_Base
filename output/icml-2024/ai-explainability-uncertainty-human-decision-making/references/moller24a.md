---
title: "Finding NEM-U: Explaining unsupervised representation learning through neural network generated explanation masks"
source: "https://proceedings.mlr.press/v235/moller24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/moller24a/moller24a.pdf"
categories: ['ai-explainability-uncertainty-human-decision-making', 'clustering-methods-and-multi-view-learning']
tags: ['explainability', 'unsupervised-representation-learning', 'explanation-masks']
venue: "ICML 2024"
tldr: "Proposes NEM-U, a method generating explanation masks to identify which input regions most influence unsupervised learned representations."
---

# Finding NEM-U: Explaining unsupervised representation learning through neural network generated explanation masks

**Source**: [https://proceedings.mlr.press/v235/moller24a.html](https://proceedings.mlr.press/v235/moller24a.html)

**TLDR**: Proposes NEM-U, a method generating explanation masks to identify which input regions most influence unsupervised learned representations.

## Abstract

Unsupervised representation learning has become an important ingredient of today’s deep learning systems. However, only a few methods exist that explain a learned vector embedding in the sense of providing information about which parts of an input are the most important for its representation. These methods generate the explanation for a given input after the model has been evaluated and tend to produce either inaccurate explanations or are slow, which limits their practical use. To address these limitations, we introduce the Neural Explanation Masks (NEM) framework, which turns a fixed representation model into a self-explaining model by augmenting it with a masking network. This network provides occlusion-based explanations in parallel to computing the representations during inference. We present an instance of this framework, the NEM-U (NEM using U-net structure) architecture, which leverages similarities between segmentation and occlusion-based masks. Our experiments show that NEM-U generates explanations faster and with lower complexity compared to the current state-of-the-art while maintaining high accuracy as measured by locality.