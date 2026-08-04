---
title: "FreeBind: Free Lunch in Unified Multimodal Space via Knowledge Fusion"
source: "https://proceedings.mlr.press/v235/wang24co.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24co/wang24co.pdf"
categories: ['generative-models-and-variational-inference']
tags: ['multimodal-representation', 'knowledge-fusion', 'unified-embedding']
venue: "ICML 2024"
tldr: "FreeBind proposes a training-free knowledge fusion approach to enhance unified multimodal representation spaces without retraining large models."
---

# FreeBind: Free Lunch in Unified Multimodal Space via Knowledge Fusion

**Source**: [https://proceedings.mlr.press/v235/wang24co.html](https://proceedings.mlr.press/v235/wang24co.html)

**TLDR**: FreeBind proposes a training-free knowledge fusion approach to enhance unified multimodal representation spaces without retraining large models.

## Abstract

Unified multi-model representation spaces are the foundation of multimodal understanding and generation. However, the billions of model parameters and catastrophic forgetting problems make it challenging to further enhance pre-trained unified spaces. In this work, we propose FreeBind, an idea that treats multimodal representation spaces as basic units, and freely augments pre-trained unified space by integrating knowledge from extra expert spaces via “space bonds". Specifically, we introduce two kinds of basic space bonds: 1) Space Displacement Bond and 2) Space Combination Bond. Based on these basic bonds, we design Complex Sequential & Parallel Bonds to effectively integrate multiple spaces simultaneously. Benefiting from the modularization concept, we further propose a coarse-to-fine customized inference strategy to flexibly adjust the enhanced unified space for different purposes. Experimentally, we bind ImageBind with extra image-text and audio-text expert spaces, resulting in three main variants: ImageBind++, InternVL_IB, and InternVL_IB++. These resulting spaces outperform ImageBind on 5 audio-image-text downstream tasks across 9 datasets. Moreover, via customized inference, it even surpasses the advanced audio-text and image-text expert spaces. Our code and checkpoints are released at https://github.com/zehanwang01/FreeBind