---
title: "Few-Shot Unsupervised Implicit Neural Shape Representation Learning with Spatial Adversaries"
source: "https://proceedings.mlr.press/v235/ouasfi24a.html"
pdf_url: "https://raw.githubusercontent.com/mlresearch/v235/main/assets/ouasfi24a/ouasfi24a.pdf"
categories: ['3d-vision-and-scene-understanding']
tags: ['implicit-neural-representations', 'signed-distance-functions', 'few-shot-learning', '3D-shape']
venue: "ICML 2024"
tldr: "Introduces few-shot unsupervised learning of implicit neural shape representations using spatial adversarial training."
---

# Few-Shot Unsupervised Implicit Neural Shape Representation Learning with Spatial Adversaries

**Source**: [https://proceedings.mlr.press/v235/ouasfi24a.html](https://proceedings.mlr.press/v235/ouasfi24a.html)

**TLDR**: Introduces few-shot unsupervised learning of implicit neural shape representations using spatial adversarial training.

## Abstract

Implicit Neural Representations have gained prominence as a powerful framework for capturing complex data modalities, encompassing a wide range from 3D shapes to images and audio. Within the realm of 3D shape representation, Neural Signed Distance Functions (SDF) have demonstrated remarkable potential in faithfully encoding intricate shape geometry. However, learning SDFs from sparse 3D point clouds in the absence of ground truth supervision remains a very challenging task. While recent methods rely on smoothness priors to regularize the learning, our method introduces a regularization term that leverages adversarial samples around the shape to improve the learned SDFs. Through extensive experiments and evaluations, we illustrate the efficacy of our proposed method, highlighting its capacity to improve SDF learning with respect to baselines and the state-of-the-art using synthetic and real data.