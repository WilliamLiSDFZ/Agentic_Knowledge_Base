---
title: "Regularizing with Pseudo-Negatives for Continual Self-Supervised Learning"
source: "https://proceedings.mlr.press/v235/cha24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cha24a/cha24a.pdf"
categories: ['continual-learning-memory-plasticity', 'generative-models-and-variational-inference']
tags: ['continual-learning', 'self-supervised-learning', 'pseudo-negatives', 'catastrophic-forgetting']
venue: "ICML 2024"
tldr: "Proposes a pseudo-negative regularization framework to prevent representation forgetting in continual self-supervised learning."
---

# Regularizing with Pseudo-Negatives for Continual Self-Supervised Learning

**Source**: [https://proceedings.mlr.press/v235/cha24a.html](https://proceedings.mlr.press/v235/cha24a.html)

**TLDR**: Proposes a pseudo-negative regularization framework to prevent representation forgetting in continual self-supervised learning.

## Abstract

We introduce a novel Pseudo-Negative Regularization (PNR) framework for effective continual self-supervised learning (CSSL). Our PNR leverages pseudo-negatives obtained through model-based augmentation in a way that newly learned representations may not contradict what has been learned in the past. Specifically, for the InfoNCE-based contrastive learning methods, we define symmetric pseudo-negatives obtained from current and previous models and use them in both main and regularization loss terms. Furthermore, we extend this idea to non-contrastive learning methods which do not inherently rely on negatives. For these methods, a pseudo-negative is defined as the output from the previous model for a differently augmented version of the anchor sample and is asymmetrically applied to the regularization term. Extensive experimental results demonstrate that our PNR framework achieves state-of-the-art performance in representation learning during CSSL by effectively balancing the trade-off between plasticity and stability.