---
title: "Towards efficient deep spiking neural networks construction with spiking activity based pruning"
source: "https://proceedings.mlr.press/v235/li24bz.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/li24bz/li24bz.pdf"
categories: ['neuromorphic-computing-and-neural-dynamics-modeling', 'knowledge-distillation-methods-and-applications']
tags: ['spiking-neural-networks', 'pruning', 'energy-efficiency']
venue: "ICML 2024"
tldr: "Proposes a spiking activity-based pruning method to efficiently compress deep spiking neural networks while preserving performance."
---

# Towards efficient deep spiking neural networks construction with spiking activity based pruning

**Source**: [https://proceedings.mlr.press/v235/li24bz.html](https://proceedings.mlr.press/v235/li24bz.html)

**TLDR**: Proposes a spiking activity-based pruning method to efficiently compress deep spiking neural networks while preserving performance.

## Abstract

The emergence of deep and large-scale spiking neural networks (SNNs) exhibiting high performance across diverse complex datasets has led to a need for compressing network models due to the presence of a significant number of redundant structural units, aiming to more effectively leverage their low-power consumption and biological interpretability advantages. Currently, most model compression techniques for SNNs are based on unstructured pruning of individual connections, which requires specific hardware support. Hence, we propose a structured pruning approach based on the activity levels of convolutional kernels named Spiking Channel Activity-based (SCA) network pruning framework. Inspired by synaptic plasticity mechanisms, our method dynamically adjusts the network’s structure by pruning and regenerating convolutional kernels during training, enhancing the model’s adaptation to the current target task. While maintaining model performance, this approach refines the network architecture, ultimately reducing computational load and accelerating the inference process. This indicates that structured dynamic sparse learning methods can better facilitate the application of deep SNNs in low-power and high-efficiency scenarios.