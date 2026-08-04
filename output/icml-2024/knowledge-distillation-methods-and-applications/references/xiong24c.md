---
title: "Distilling Morphology-Conditioned Hypernetworks for Efficient Universal Morphology Control"
source: "https://proceedings.mlr.press/v235/xiong24c.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/xiong24c/xiong24c.pdf"
categories: ['knowledge-distillation-methods-and-applications']
tags: ['morphology-conditioned', 'hypernetworks', 'universal-policy']
venue: "ICML 2024"
tldr: "A distillation framework compresses transformer-based universal morphology control policies into efficient hypernetworks for multi-robot generalization."
---

# Distilling Morphology-Conditioned Hypernetworks for Efficient Universal Morphology Control

**Source**: [https://proceedings.mlr.press/v235/xiong24c.html](https://proceedings.mlr.press/v235/xiong24c.html)

**TLDR**: A distillation framework compresses transformer-based universal morphology control policies into efficient hypernetworks for multi-robot generalization.

## Abstract

Learning a universal policy across different robot morphologies can significantly improve learning efficiency and enable zero-shot generalization to unseen morphologies. However, learning a highly performant universal policy requires sophisticated architectures like transformers (TF) that have larger memory and computational cost than simpler multi-layer perceptrons (MLP). To achieve both good performance like TF and high efficiency like MLP at inference time, we propose HyperDistill, which consists of: (1) A morphology-conditioned hypernetwork (HN) that generates robot-wise MLP policies, and (2) A policy distillation approach that is essential for successful training. We show that on UNIMAL, a benchmark with hundreds of diverse morphologies, HyperDistill performs as well as a universal TF teacher policy on both training and unseen test robots, but reduces model size by 6-14 times, and computational cost by 67-160 times in different environments. Our analysis attributes the efficiency advantage of HyperDistill at inference time to knowledge decoupling, i.e., the ability to decouple inter-task and intra-task knowledge, a general principle that could also be applied to improve inference efficiency in other domains. The code is publicly available at https://github.com/MasterXiong/Universal-Morphology-Control.