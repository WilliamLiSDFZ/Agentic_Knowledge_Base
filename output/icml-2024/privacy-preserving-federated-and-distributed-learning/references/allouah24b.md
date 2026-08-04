---
title: "The Privacy Power of Correlated Noise in Decentralized Learning"
source: "https://proceedings.mlr.press/v235/allouah24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/allouah24b/allouah24b.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'adversarial-robustness-and-model-security']
tags: ['decentralized-learning', 'correlated-noise', 'differential-privacy']
venue: "ICML 2024"
tldr: "This paper shows that correlated noise in decentralized learning can provide strong privacy guarantees without sacrificing utility."
---

# The Privacy Power of Correlated Noise in Decentralized Learning

**Source**: [https://proceedings.mlr.press/v235/allouah24b.html](https://proceedings.mlr.press/v235/allouah24b.html)

**TLDR**: This paper shows that correlated noise in decentralized learning can provide strong privacy guarantees without sacrificing utility.

## Abstract

Decentralized learning is appealing as it enables the scalable usage of large amounts of distributed data and resources without resorting to any central entity, while promoting privacy since every user minimizes the direct exposure of their data. Yet, without additional precautions, curious users can still leverage models obtained from their peers to violate privacy. In this paper, we propose Decor, a variant of decentralized SGD with differential privacy (DP) guarantees. Essentially, in Decor, users securely exchange randomness seeds in one communication round to generate pairwise-canceling correlated Gaussian noises, which are injected to protect local models at every communication round. We theoretically and empirically show that, for arbitrary connected graphs, Decor matches the central DP optimal privacy-utility trade-off. We do so under SecLDP, our new relaxation of local DP, which protects all user communications against an external eavesdropper and curious users, assuming that every pair of connected users shares a secret, i.e., an information hidden to all others. The main theoretical challenge is to control the accumulation of non-canceling correlated noise due to network sparsity. We also propose a companion SecLDP privacy accountant for public use.