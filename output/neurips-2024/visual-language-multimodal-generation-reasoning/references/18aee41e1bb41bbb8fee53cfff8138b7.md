---
title: "$SE(3)$ Equivariant Ray Embeddings for Implicit Multi-View Depth Estimation"
source: "https://papers.nips.cc/paper_files/paper/2024/hash/18aee41e1bb41bbb8fee53cfff8138b7-Abstract-Conference.html"
categories: ['neural-geometric-shape-representation-learning', 'visual-language-multimodal-generation-reasoning']
tags: ['SE3-equivariance', 'multi-view-depth', 'ray-embeddings']
venue: "NeurIPS 2024"
tldr: "Proposes SE(3)-equivariant ray embeddings as geometric inductive biases for implicit multi-view depth estimation."
---

# $SE(3)$ Equivariant Ray Embeddings for Implicit Multi-View Depth Estimation

**Source**: [https://papers.nips.cc/paper_files/paper/2024/hash/18aee41e1bb41bbb8fee53cfff8138b7-Abstract-Conference.html](https://papers.nips.cc/paper_files/paper/2024/hash/18aee41e1bb41bbb8fee53cfff8138b7-Abstract-Conference.html)

**TLDR**: Proposes SE(3)-equivariant ray embeddings as geometric inductive biases for implicit multi-view depth estimation.

## Abstract

Incorporating inductive bias by embedding geometric entities (such as rays) as input has proven successful in multi-view learning. However, the methods adopting this technique typically lack equivariance, which is crucial for effective 3D learning. Equivariance serves as a valuable inductive prior, aiding in the generation of robust multi-view features for 3D scene understanding. In this paper, we explore the application of equivariant multi-view learning to depth estimation, not only recognizing its significance for computer vision and robotics but also addressing the limitations of previous research. Most prior studies have either overlooked equivariance in this setting or achieved only approximate equivariance through data augmentation, which often leads to inconsistencies across different reference frames. To address this issue, we propose to embed $SE(3)$ equivariance into the Perceiver IO architecture. We employ Spherical Harmonics for positional encoding to ensure 3D rotation equivariance, and develop a specialized equivariant encoder and decoder within the Perceiver IO architecture. To validate our model, we applied it to the task of stereo depth estimation, achieving state of the art results on real-world datasets without explicit geometric constraints or extensive data augmentation.