---
title: "ViP: A Differentially Private Foundation Model for Computer Vision"
source: "https://proceedings.mlr.press/v235/yu24k.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/yu24k/yu24k.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'learning-with-imperfect-data-and-bias']
tags: ['differential-privacy', 'foundation-model', 'computer-vision']
venue: "ICML 2024"
tldr: "ViP is a differentially private vision foundation model trained on internet-scale data to mitigate privacy and legal risks."
---

# ViP: A Differentially Private Foundation Model for Computer Vision

**Source**: [https://proceedings.mlr.press/v235/yu24k.html](https://proceedings.mlr.press/v235/yu24k.html)

**TLDR**: ViP is a differentially private vision foundation model trained on internet-scale data to mitigate privacy and legal risks.

## Abstract

Artificial intelligence (AI) has seen a tremendous surge in capabilities thanks to the use of foundation models trained on internet-scale data. On the flip side, the uncurated nature of internet-scale data also poses significant privacy and legal risks, as they often contain personal information or copyrighted material that should not be trained on without permission. In this work, we propose as a mitigation measure a recipe to train foundation vision models via self-supervised learning with differential privacy (DP) guarantee. We identify masked autoencoders as a suitable learning algorithm that aligns well with DP-SGD, and train ViP—a Vision transformer with differential Privacy—under a strict privacy budget of $\epsilon=8$ on the LAION400M dataset. We evaluate the quality of representation learned by ViP using standard downstream vision tasks; in particular, ViP achieves a (non-private) linear probing accuracy of 55.7% on ImageNet, comparable to that of end-to-end trained AlexNet (trained and evaluated on ImageNet). Our result suggests that scaling to internet-scale data can be practical for private learning. Code and DP pre-trained models are available at https://github.com/facebookresearch/ViP-MAE.