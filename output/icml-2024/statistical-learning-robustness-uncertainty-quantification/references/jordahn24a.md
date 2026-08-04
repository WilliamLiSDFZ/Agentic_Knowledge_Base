---
title: "Decoupling Feature Extraction and Classification Layers for Calibrated Neural Networks"
source: "https://proceedings.mlr.press/v235/jordahn24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/jordahn24a/jordahn24a.pdf"
categories: ['uncertainty-calibration-and-distribution-shift-adaptation', 'statistical-learning-robustness-uncertainty-quantification']
tags: ['calibration', 'neural-networks', 'feature-extraction', 'classification']
venue: "ICML 2024"
tldr: "Proposes decoupling feature extraction and classification layers to improve calibration of deep neural networks without sacrificing accuracy."
---

# Decoupling Feature Extraction and Classification Layers for Calibrated Neural Networks

**Source**: [https://proceedings.mlr.press/v235/jordahn24a.html](https://proceedings.mlr.press/v235/jordahn24a.html)

**TLDR**: Proposes decoupling feature extraction and classification layers to improve calibration of deep neural networks without sacrificing accuracy.

## Abstract

Deep Neural Networks (DNN) have shown great promise in many classification applications, yet are widely known to have poorly calibrated predictions when they are over-parametrized. Improving DNN calibration without comprising on model accuracy is of extreme importance and interest in safety critical applications such as in the health-care sector. In this work, we show that decoupling the training of feature extraction layers and classification layers in over-parametrized DNN architectures such as Wide Residual Networks (WRN) and Vision Transformers (ViT) significantly improves model calibration whilst retaining accuracy, and at a low training cost. In addition, we show that placing a Gaussian prior on the last hidden layer outputs of a DNN, and training the model variationally in the classification training stage, even further improves calibration. We illustrate these methods improve calibration across ViT and WRN architectures for several image classification benchmark datasets.