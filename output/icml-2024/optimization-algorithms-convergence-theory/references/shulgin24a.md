---
title: "Towards a Better Theoretical Understanding of Independent Subnetwork Training"
source: "https://proceedings.mlr.press/v235/shulgin24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/shulgin24a/shulgin24a.pdf"
categories: ['optimization-algorithms-convergence-theory', 'privacy-preserving-federated-and-distributed-learning']
tags: ['distributed-learning', 'independent-subnetwork-training', 'communication-efficiency']
venue: "ICML 2024"
tldr: "Provides theoretical analysis of independent subnetwork training as a communication-efficient approach for distributed machine learning."
---

# Towards a Better Theoretical Understanding of Independent Subnetwork Training

**Source**: [https://proceedings.mlr.press/v235/shulgin24a.html](https://proceedings.mlr.press/v235/shulgin24a.html)

**TLDR**: Provides theoretical analysis of independent subnetwork training as a communication-efficient approach for distributed machine learning.

## Abstract

Modern advancements in large-scale machine learning would be impossible without the paradigm of data-parallel distributed computing. Since distributed computing with large-scale models imparts excessive pressure on communication channels, significant recent research has been directed toward co-designing communication compression strategies and training algorithms with the goal of reducing communication costs. While pure data parallelism allows better data scaling, it suffers from poor model scaling properties. Indeed, compute nodes are severely limited by memory constraints, preventing further increases in model size. For this reason, the latest achievements in training giant neural network models also rely on some form of model parallelism. In this work, we take a closer theoretical look at Independent Subnetwork Training (IST), which is a recently proposed and highly effective technique for solving the aforementioned problems. We identify fundamental differences between IST and alternative approaches, such as distributed methods with compressed communication, and provide a precise analysis of its optimization performance on a quadratic model.