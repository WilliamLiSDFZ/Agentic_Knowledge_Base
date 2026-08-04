---
title: "Delving into Differentially Private Transformer"
source: "https://proceedings.mlr.press/v235/ding24g.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ding24g/ding24g.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'transformer-architecture-efficiency-and-scaling']
tags: ['differential-privacy', 'transformer', 'deep-learning', 'DP-SGD', 'privacy-utility-tradeoff']
venue: "ICML 2024"
tldr: "Systematically investigates training Transformer models with differential privacy and proposes methods to improve accuracy and efficiency under DP constraints."
---

# Delving into Differentially Private Transformer

**Source**: [https://proceedings.mlr.press/v235/ding24g.html](https://proceedings.mlr.press/v235/ding24g.html)

**TLDR**: Systematically investigates training Transformer models with differential privacy and proposes methods to improve accuracy and efficiency under DP constraints.

## Abstract

Deep learning with differential privacy (DP) has garnered significant attention over the past years, leading to the development of numerous methods aimed at enhancing model accuracy and training efficiency. This paper delves into the problem of training Transformer models with differential privacy. Our treatment is modular: the logic is to ’reduce’ the problem of training DP Transformer to the more basic problem of training DP vanilla neural nets. The latter is better understood and amenable to many model-agnostic methods. Such ’reduction’ is done by first identifying the hardness unique to DP Transformer training: the attention distraction phenomenon and a lack of compatibility with existing techniques for efficient gradient clipping. To deal with these two issues, we propose the Re-Attention Mechanism and Phantom Clipping, respectively. We believe that our work not only casts new light on training DP Transformers but also promotes a modular treatment to advance research in the field of differentially private deep learning.