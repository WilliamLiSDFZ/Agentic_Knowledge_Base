---
title: "Bootstrap AutoEncoders With Contrastive Paradigm for Self-supervised Gaze Estimation"
source: "https://proceedings.mlr.press/v235/wang24ah.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/wang24ah/wang24ah.pdf"
categories: ['clustering-methods-and-multi-view-learning', 'generative-models-and-variational-inference']
tags: ['self-supervised-learning', 'gaze-estimation', 'contrastive-learning', 'autoencoders']
venue: "ICML 2024"
tldr: "A bootstrap autoencoder with a contrastive paradigm is proposed for self-supervised gaze estimation in full-face settings."
---

# Bootstrap AutoEncoders With Contrastive Paradigm for Self-supervised Gaze Estimation

**Source**: [https://proceedings.mlr.press/v235/wang24ah.html](https://proceedings.mlr.press/v235/wang24ah.html)

**TLDR**: A bootstrap autoencoder with a contrastive paradigm is proposed for self-supervised gaze estimation in full-face settings.

## Abstract

Existing self-supervised methods for gaze estimation using the dominant streams of contrastive and generative approaches are restricted to eye images and could fail in general full-face settings. In this paper, we reveal that contrastive methods are ineffective in data augmentation for self-supervised full-face gaze estimation, while generative methods are prone to trivial solutions due to the absence of explicit regularization on semantic representations. To address this challenge, we propose a novel approach called Bootstrap auto-encoders with Contrastive paradigm (BeCa), which combines the strengths of both generative and contrastive methods. Specifically, we revisit the Auto-Encoder used in generative approaches and incorporate the contrastive paradigm to introduce explicit regularization on gaze representation. Furthermore, we design the InfoMSE loss as an alternative to the vanilla MSE loss for Auto-Encoder to mitigate the inconsistency between reconstruction and representation learning. Experimental results demonstrate that the proposed approaches outperform state-of-the-art unsupervised gaze approaches on extensive datasets (including wild scenes) under both within-dataset and cross-dataset protocols.