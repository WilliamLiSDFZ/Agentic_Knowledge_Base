---
title: "Layerwise Change of Knowledge in Neural Networks"
source: "https://proceedings.mlr.press/v235/cheng24b.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/cheng24b/cheng24b.pdf"
categories: ['neural-network-learning-dynamics-theory', 'llm-geometry-and-interpretability-research']
tags: ['knowledge-extraction', 'deep-neural-networks', 'layer-wise-analysis']
venue: "ICML 2024"
tldr: "An analysis of how deep neural networks progressively extract knowledge and discard noisy features across layers during forward propagation."
---

# Layerwise Change of Knowledge in Neural Networks

**Source**: [https://proceedings.mlr.press/v235/cheng24b.html](https://proceedings.mlr.press/v235/cheng24b.html)

**TLDR**: An analysis of how deep neural networks progressively extract knowledge and discard noisy features across layers during forward propagation.

## Abstract

This paper aims to explain how a deep neural network (DNN) gradually extracts new knowledge and forgets noisy features through layers in forward propagation. Up to now, although how to define knowledge encoded by the DNN has not reached a consensus so far, previous studies have derived a series of mathematical evidences to take interactions as symbolic primitive inference patterns encoded by a DNN. We extend the definition of interactions and, for the first time, extract interactions encoded by intermediate layers. We quantify and track the newly emerged interactions and the forgotten interactions in each layer during the forward propagation, which shed new light on the learning behavior of DNNs. The layer-wise change of interactions also reveals the change of the generalization capacity and instability of feature representations of a DNN.