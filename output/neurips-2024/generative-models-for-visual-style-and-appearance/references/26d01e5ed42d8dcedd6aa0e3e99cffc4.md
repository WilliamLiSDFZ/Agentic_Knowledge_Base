---
title: "Transferring disentangled representations: bridging the gap between synthetic and real images"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/26d01e5ed42d8dcedd6aa0e3e99cffc4-Abstract-Conference.html"
categories: ['disentangled-representation-learning-cognitive-diagnosis', 'generative-models-for-visual-style-and-appearance']
tags: ['disentangled-representations', 'synthetic-to-real-transfer', 'generative-factors']
venue: "NeurIPS 2024"
tldr: "This work bridges the gap between synthetic and real images in disentangled representation learning by addressing correlated generative factors."
---

# Transferring disentangled representations: bridging the gap between synthetic and real images

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/26d01e5ed42d8dcedd6aa0e3e99cffc4-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/26d01e5ed42d8dcedd6aa0e3e99cffc4-Abstract-Conference.html)

**TLDR**: This work bridges the gap between synthetic and real images in disentangled representation learning by addressing correlated generative factors.

## Abstract

Developing meaningful and efficient representations that separate the fundamental structure of the data generation mechanism is crucial in representation learning. However, Disentangled Representation Learning has not fully shown its potential on real images, because of correlated generative factors, their resolution and limited access to ground truth labels. Specifically on the latter, we investigate the possibility of leveraging synthetic data to learn general-purpose disentangled representations applicable to real data, discussing the effect of fine-tuning and what properties of disentanglement are preserved after the transfer. We provide an extensive empirical study to address these issues. In addition, we propose a new interpretable intervention-based metric, to measure the quality of factors encoding in the representation. Our results indicate that some level of disentanglement, transferring a representation from synthetic to real data, is possible and effective.