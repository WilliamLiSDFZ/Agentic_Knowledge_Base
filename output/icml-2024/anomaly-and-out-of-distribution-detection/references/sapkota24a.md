---
title: "Meta Evidential Transformer for Few-Shot Open-Set Recognition"
source: "https://proceedings.mlr.press/v235/sapkota24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/sapkota24a/sapkota24a.pdf"
categories: ['anomaly-and-out-of-distribution-detection', 'uncertainty-calibration-and-distribution-shift-adaptation']
tags: ['few-shot-learning', 'open-set-recognition', 'evidential-learning', 'transformer', 'uncertainty']
venue: "ICML 2024"
tldr: "A Meta Evidential Transformer is proposed for few-shot open-set recognition, using evidential uncertainty to better reject instances from unseen classes."
---

# Meta Evidential Transformer for Few-Shot Open-Set Recognition

**Source**: [https://proceedings.mlr.press/v235/sapkota24a.html](https://proceedings.mlr.press/v235/sapkota24a.html)

**TLDR**: A Meta Evidential Transformer is proposed for few-shot open-set recognition, using evidential uncertainty to better reject instances from unseen classes.

## Abstract

Few-shot open-set recognition (FSOSR) aims to detect instances from unseen classes by utilizing a small set of labeled instances from closed-set classes. Accurately rejecting instances from open-set classes in the few-shot setting is fundamentally more challenging due to the weaker supervised signals resulting from fewer labels. Transformer-based few-shot methods exploit attention mapping to achieve a consistent representation. However, the softmax-generated attention map normalizes all the instances that assign unnecessary high attentive weights to those instances not close to the closed-set classes that negatively impact the detection performance. In addition, open-set samples that are similar to a certain closed-set class also pose a significant challenge to most existing FSOSR models. To address these challenges, we propose a novel Meta Evidential Transformer (MET) based FSOSR model that uses an evidential open-set loss to learn more compact closed-set class representations by effectively leveraging similar closed-set classes. MET further integrates an evidence-to-variance ratio to detect fundamentally challenging tasks and uses an evidence-guided cross-attention mechanism to better separate the difficult open-set samples. Experiments on real-world datasets demonstrate consistent improvement over existing competitive methods in unseen class recognition without deteriorating closed-set performance.