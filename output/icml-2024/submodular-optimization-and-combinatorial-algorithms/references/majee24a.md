---
title: "SCoRe: Submodular Combinatorial Representation Learning"
source: "https://proceedings.mlr.press/v235/majee24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/majee24a/majee24a.pdf"
categories: ['submodular-optimization-and-combinatorial-algorithms', 'clustering-methods-and-multi-view-learning']
tags: ['submodular-optimization', 'representation-learning', 'inter-class-bias']
venue: "ICML 2024"
tldr: "A submodular combinatorial representation learning framework addressing inter-class bias and intra-class variance through combinatorial viewpoints."
---

# SCoRe: Submodular Combinatorial Representation Learning

**Source**: [https://proceedings.mlr.press/v235/majee24a.html](https://proceedings.mlr.press/v235/majee24a.html)

**TLDR**: A submodular combinatorial representation learning framework addressing inter-class bias and intra-class variance through combinatorial viewpoints.

## Abstract

In this paper we introduce the SCoRe (Submodular Combinatorial Representation Learning) framework, a novel approach in representation learning that addresses inter-class bias and intra-class variance. SCoRe provides a new combinatorial viewpoint to representation learning, by introducing a family of loss functions based on set-based submodular information measures. We develop two novel combinatorial formulations for loss functions, using the Total Information and Total Correlation, that naturally minimize intra-class variance and inter-class bias. Several commonly used metric/contrastive learning loss functions like supervised contrastive loss, orthogonal projection loss, and N-pairs loss, are all instances of SCoRe, thereby underlining the versatility and applicability of SCoRe in a broad spectrum of learning scenarios. Novel objectives in SCoRe naturally model class-imbalance with up to 7.6% improvement in classification on CIFAR-10-LT, CIFAR-100-LT, MedMNIST, 2.1% on ImageNet-LT, and 19.4% in object detection on IDD and LVIS (v1.0), demonstrating its effectiveness over existing approaches.