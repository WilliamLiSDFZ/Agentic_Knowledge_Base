---
title: "Sparser, Better, Deeper, Stronger: Improving Static Sparse Training with Exact Orthogonal Initialization"
source: "https://proceedings.mlr.press/v235/nowak24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/nowak24a/nowak24a.pdf"
categories: ['neural-network-learning-dynamics-theory']
tags: ['sparse-training', 'orthogonal-initialization', 'neural-network-pruning']
venue: "ICML 2024"
tldr: "Proposes exact orthogonal initialization for static sparse training to improve trainable subnetwork selection from scratch."
---

# Sparser, Better, Deeper, Stronger: Improving Static Sparse Training with Exact Orthogonal Initialization

**Source**: [https://proceedings.mlr.press/v235/nowak24a.html](https://proceedings.mlr.press/v235/nowak24a.html)

**TLDR**: Proposes exact orthogonal initialization for static sparse training to improve trainable subnetwork selection from scratch.

## Abstract

Static sparse training aims to train sparse models from scratch, achieving remarkable results in recent years. A key design choice is given by the sparse initialization, which determines the trainable sub-network through a binary mask. Existing methods mainly select such mask based on a predefined dense initialization. Such an approach may not efficiently leverage the mask’s potential impact on the optimization. An alternative direction, inspired by research into dynamical isometry, is to introduce orthogonality in the sparse subnetwork, which helps in stabilizing the gradient signal. In this work, we propose Exact Orthogonal Initialization (EOI), a novel sparse orthogonal initialization scheme based on composing random Givens rotations. Contrary to other existing approaches, our method provides exact (not approximated) orthogonality and enables the creation of layers with arbitrary densities. We demonstrate the superior effectiveness and efficiency of EOI through experiments, consistently outperforming common sparse initialization techniques. Our method enables training highly sparse 1000-layer MLP and CNN networks without residual connections or normalization techniques, emphasizing the crucial role of weight initialization in static sparse training alongside sparse mask selection.