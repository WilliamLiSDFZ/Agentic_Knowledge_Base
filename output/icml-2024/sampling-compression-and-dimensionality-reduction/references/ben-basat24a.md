---
title: "Accelerating Federated Learning with Quick Distributed Mean Estimation"
source: "https://proceedings.mlr.press/v235/ben-basat24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ben-basat24a/ben-basat24a.pdf"
categories: ['privacy-preserving-federated-and-distributed-learning', 'sampling-compression-and-dimensionality-reduction']
tags: ['federated-learning', 'distributed-mean-estimation', 'communication-efficiency', 'quantization', 'compression']
venue: "ICML 2024"
tldr: "Proposes faster distributed mean estimation techniques to accelerate communication-efficient federated learning."
---

# Accelerating Federated Learning with Quick Distributed Mean Estimation

**Source**: [https://proceedings.mlr.press/v235/ben-basat24a.html](https://proceedings.mlr.press/v235/ben-basat24a.html)

**TLDR**: Proposes faster distributed mean estimation techniques to accelerate communication-efficient federated learning.

## Abstract

Distributed Mean Estimation (DME), in which $n$ clients communicate vectors to a parameter server that estimates their average, is a fundamental building block in communication-efficient federated learning. In this paper, we improve on previous DME techniques that achieve the optimal $O(1/n)$ Normalized Mean Squared Error (NMSE) guarantee by asymptotically improving the complexity for either encoding or decoding (or both). To achieve this, we formalize the problem in a novel way that allows us to use off-the-shelf mathematical solvers to design the quantization. Using various datasets and training tasks, we demonstrate how QUIC-FL achieves state of the art accuracy with faster encoding and decoding times compared to other DME methods.